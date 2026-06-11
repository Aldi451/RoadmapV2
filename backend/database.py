import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "sqlite:///./roadmap.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class DBProject(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String(255), index=True)
    customer_name = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    phases = relationship("DBPhase", back_populates="project", cascade="all, delete-orphan")

class DBPhase(Base):
    __tablename__ = "phases"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    phase_name = Column(String(255))
    code = Column(String(50), unique=True, index=True)
    status = Column(String(50), default="Scheduled")
    sort_order = Column(Integer, default=0)
    
    project = relationship("DBProject", back_populates="phases")
    tasks = relationship("DBTask", back_populates="phase", cascade="all, delete-orphan")

class DBTask(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    phase_id = Column(Integer, ForeignKey("phases.id"))
    parent_code = Column(String(50), nullable=True)  # self-referencing to parent task's code
    code = Column(String(50), unique=True, index=True)
    task_name = Column(String(255))
    
    scheduled_start = Column(String(50), nullable=True)
    scheduled_finish = Column(String(50), nullable=True)
    scheduled_days = Column(Integer, nullable=True)
    
    actual_start = Column(String(50), nullable=True)
    actual_finish = Column(String(50), nullable=True)
    actual_days = Column(Integer, nullable=True)
    
    status = Column(String(50), default="Scheduled")
    progress = Column(Integer, default=0)
    note = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    
    phase = relationship("DBPhase", back_populates="tasks")

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
