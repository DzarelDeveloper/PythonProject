import argparse,re
from collections import Counter
from pathlib import Path
PATTERNS=[re.compile(r"Failed password for (?:invalid user )?\S+ from (?P<ip>[0-9a-fA-F:.]+)"),re.compile(r"authentication failure.*rhost=(?P<ip>[0-9a-fA-F:.]+)")]
def analyze(path,threshold):
 counts=Counter()
 with path.open(encoding="utf-8",errors="replace") as f:
  for line in f:
   for pattern in PATTERNS:
    match=pattern.search(line)
    if match: counts[match.group("ip")]+=1; break
 for ip,count in counts.most_common():
  if count>=threshold: print(f"{ip}: {count} failed authentications")
def main():
 p=argparse.ArgumentParser(); p.add_argument("logfile",type=Path); p.add_argument("--threshold",type=int,default=5); a=p.parse_args()
 if not a.logfile.is_file(): p.error("logfile not found")
 analyze(a.logfile,max(1,a.threshold))
if __name__=="__main__": main()
