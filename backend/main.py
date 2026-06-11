from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from sqlalchemy.orm import Session
from .models import Roadmap, Phase, Task, TaskUpdate
from .database import engine, Base, init_db, get_db, DBProject, DBPhase, DBTask
from typing import List

app = FastAPI(title="Roadmap API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database tables
init_db()

# Seed default data if database is empty
def seed_default_data():
    db = next(get_db())
    try:
        project_count = db.query(DBProject).count()
        if project_count == 0:
            default_proj = DBProject(project_name="Project Roadmap : Fortunasuite Malioboro", customer_name="Fortunasuite")
            db.add(default_proj)
            db.commit()
            db.refresh(default_proj)
            
            # Create default phases
            p1 = DBPhase(project_id=default_proj.id, phase_name="Project Preparation", code="1", sort_order=1)
            p2 = DBPhase(project_id=default_proj.id, phase_name="Implementation Cloud Full Version", code="2", sort_order=2)
            db.add_all([p1, p2])
            db.commit()
            db.refresh(p1)
            db.refresh(p2)
            
            # Create default tasks for Phase 1
            t1 = DBTask(phase_id=p1.id, code="1.PRP", task_name="1. Project Preparation", scheduled_start="07/06/2025", scheduled_finish="15/06/2025", actual_start="07/06/2025", actual_finish="15/06/2025", status="On Progress", note="Initial phase", is_active=True)
            t2 = DBTask(phase_id=p1.id, code="1.IMP", task_name="     1.1. Implementation Periode : 60 Days", scheduled_start="10/06/2025", scheduled_finish="10/06/2025", actual_start="10/06/2025", actual_finish="10/06/2025", status="Completed", note="60 days info", is_active=True)
            t3 = DBTask(phase_id=p1.id, code="1.SDS", task_name="     1.2. Setup Data Submission", scheduled_start="07/06/2025", scheduled_finish="07/06/2025", actual_start="07/06/2025", actual_finish="07/06/2025", status="Completed", note="Email sent", is_active=True)
            
            # Create default tasks for Phase 2
            t4 = DBTask(phase_id=p2.id, code="2.SIM", task_name="2. Implementation Cloud Full Version", scheduled_start="16/06/2025", scheduled_finish="15/08/2025", actual_start="22/06/2025", status="Scheduled", is_active=True)
            t5 = DBTask(phase_id=p2.id, code="2.KOM", task_name="     2.1. Kick Off Meeting", scheduled_start="16/06/2025", scheduled_finish="16/06/2025", actual_start="23/06/2025", actual_finish="23/06/2025", status="Completed", note="Completed kickoff", is_active=True)
            
            db.add_all([t1, t2, t3, t4, t5])
            db.commit()
    finally:
        db.close()

seed_default_data()

static_dir = Path(__file__).parent.parent / "frontend"
app.mount("/roadmap", StaticFiles(directory=str(static_dir), html=True), name="frontend")

@app.get("/", include_in_schema=False)
async def root_redirect():
    return RedirectResponse(url="/roadmap")

# Mock Indonesian Holidays
HOLIDAYS = [
    "2024-05-01",
    "2024-05-09",
    "2024-05-23",
    "2024-06-01",
    "2024-06-17",
]

@app.get("/api/holidays")
async def get_holidays():
    return HOLIDAYS

@app.get("/api/roadmap", response_model=Roadmap)
async def get_roadmap(db: Session = Depends(get_db)):
    proj = db.query(DBProject).first()
    if not proj:
        raise HTTPException(status_code=404, detail="Project not found")
        
    phases = []
    for db_phase in db.query(DBPhase).filter_by(project_id=proj.id).order_by(DBPhase.sort_order).all():
        tasks = []
        # Query root tasks first
        db_tasks = db.query(DBTask).filter_by(phase_id=db_phase.id, parent_code=None).all()
        for db_task in db_tasks:
            # Get subtasks
            sub_tasks = []
            db_subs = db.query(DBTask).filter_by(parent_code=db_task.code).all()
            for sub in db_subs:
                sub_tasks.append(Task(
                    code=sub.code,
                    name=sub.task_name,
                    start_date=sub.scheduled_start,
                    finish_date=sub.scheduled_finish,
                    status=sub.status,
                    progress=sub.progress,
                    note=sub.note,
                    is_active=sub.is_active,
                    scheduled_days=sub.scheduled_days,
                    actual_start=sub.actual_start,
                    actual_finish=sub.actual_finish,
                    actual_days=sub.actual_days,
                    sub_tasks=[]
                ))
                
            tasks.append(Task(
                code=db_task.code,
                name=db_task.task_name,
                start_date=db_task.scheduled_start,
                finish_date=db_task.scheduled_finish,
                status=db_task.status,
                progress=db_task.progress,
                note=db_task.note,
                is_active=db_task.is_active,
                scheduled_days=db_task.scheduled_days,
                actual_start=db_task.actual_start,
                actual_finish=db_task.actual_finish,
                actual_days=db_task.actual_days,
                sub_tasks=sub_tasks
            ))
            
        phases.append(Phase(
            name=db_phase.phase_name,
            code=db_phase.code,
            status=db_phase.status or "Scheduled",
            tasks=tasks
        ))
        
    return Roadmap(project_name=proj.project_name, phases=phases)

@app.post("/api/roadmap/update-task")
async def update_task(update: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(DBTask).filter_by(code=update.task_code).first()
    if not task:
        # If task does not exist, create it (e.g. dynamic/new task or custom subtask)
        # Find appropriate phase
        phase_code = update.task_code.split('.')[0] if '.' in update.task_code else "1"
        phase = db.query(DBPhase).filter_by(code=phase_code).first()
        if not phase:
            phase = db.query(DBPhase).first()
        
        parent_code = None
        # Check if it has a parent task code (e.g. 1.1.1 or 1.1.ABC)
        parts = update.task_code.split('.')
        if len(parts) > 2:
            parent_code = ".".join(parts[:-1])
            
        task = DBTask(
            code=update.task_code,
            phase_id=phase.id,
            parent_code=parent_code,
            task_name=update.task_code,  # Default name to code
            is_active=True
        )
        db.add(task)
        db.commit()
        db.refresh(task)

    if update.name is not None: task.task_name = update.name
    if update.start_date is not None: task.scheduled_start = update.start_date
    if update.finish_date is not None: task.scheduled_finish = update.finish_date
    if update.scheduled_days is not None: task.scheduled_days = update.scheduled_days
    if update.actual_start is not None: task.actual_start = update.actual_start
    if update.actual_finish is not None: task.actual_finish = update.actual_finish
    if update.actual_days is not None: task.actual_days = update.actual_days
    if update.status is not None: task.status = update.status
    if update.note is not None: task.note = update.note
    if update.is_active is not None: task.is_active = update.is_active

    
    db.commit()
    return {"message": "Updated successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
