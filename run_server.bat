@echo off
echo Starting local FastAPI server for Project Roadmap...
echo Opening browser at http://127.0.0.1:8000/
start http://127.0.0.1:8000/
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
pause
