import argparse, sqlite3
from datetime import date
DB="expenses.db"
def setup(db): db.execute("CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY,spent_on TEXT,category TEXT,amount REAL,note TEXT)")
def main():
 p=argparse.ArgumentParser(); s=p.add_subparsers(dest="cmd",required=True)
 a=s.add_parser("add"); a.add_argument("category"); a.add_argument("amount",type=float); a.add_argument("--note",default="")
 s.add_parser("list"); x=p.parse_args()
 with sqlite3.connect(DB) as db:
  setup(db)
  if x.cmd=="add": db.execute("INSERT INTO expenses(spent_on,category,amount,note) VALUES(?,?,?,?)",(date.today().isoformat(),x.category,x.amount,x.note))
  else:
   rows=db.execute("SELECT * FROM expenses ORDER BY id DESC").fetchall()
   for r in rows: print(f"{r[0]} | {r[1]} | {r[2]} | Rp{r[3]:,.0f} | {r[4]}")
   print(f"Total: Rp{sum(r[3] for r in rows):,.0f}")
if __name__=="__main__": main()
