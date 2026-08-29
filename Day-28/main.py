from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
app=FastAPI(title="Task API"); tasks={}; next_id=1
class Task(BaseModel): title:str=Field(min_length=1,max_length=120); done:bool=False
@app.get("/tasks")
def all_tasks(): return list(tasks.values())
@app.post("/tasks",status_code=201)
def add(task:Task):
 global next_id
 item={"id":next_id,**task.model_dump()}; tasks[next_id]=item; next_id+=1; return item
@app.patch("/tasks/{task_id}")
def edit(task_id:int,task:Task):
 if task_id not in tasks: raise HTTPException(404,"Task not found")
 tasks[task_id]={"id":task_id,**task.model_dump()}; return tasks[task_id]
@app.delete("/tasks/{task_id}",status_code=204)
def remove(task_id:int):
 if tasks.pop(task_id,None) is None: raise HTTPException(404,"Task not found")
