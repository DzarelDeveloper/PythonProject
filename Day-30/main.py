import sqlite3
from flask import Flask,redirect,render_template_string,request,url_for
app=Flask(__name__); DB="tasks.db"
PAGE="""<h1>Task Manager</h1><form method=post action=/add><input name=title required maxlength=120><button>Add</button></form><ul>{% for t in tasks %}<li>{{t['title']}} <form style="display:inline" method=post action="/toggle/{{t['id']}}"><button>Toggle</button></form> <form style="display:inline" method=post action="/delete/{{t['id']}}"><button>Delete</button></form></li>{% endfor %}</ul>"""
def connect():
 db=sqlite3.connect(DB); db.row_factory=sqlite3.Row; db.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY,title TEXT NOT NULL,done INTEGER DEFAULT 0)"); return db
@app.get("/")
def index():
 with connect() as db: tasks=db.execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
 return render_template_string(PAGE,tasks=tasks)
@app.post("/add")
def add():
 title=request.form.get("title","").strip()
 if title:
  with connect() as db: db.execute("INSERT INTO tasks(title) VALUES(?)",(title,))
 return redirect(url_for("index"))
@app.post("/toggle/<int:i>")
def toggle(i):
 with connect() as db: db.execute("UPDATE tasks SET done=NOT done WHERE id=?",(i,))
 return redirect(url_for("index"))
@app.post("/delete/<int:i>")
def delete(i):
 with connect() as db: db.execute("DELETE FROM tasks WHERE id=?",(i,))
 return redirect(url_for("index"))
if __name__=="__main__": app.run(debug=True)
