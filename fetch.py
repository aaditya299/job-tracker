import html
import os 
import requests
import psycopg2
from datetime import date
from dotenv import load_dotenv

load_dotenv()
today=date.today()

url="https://remoteok.com/api"
response=requests.get(url)
data=response.json()
jobs=data[1:]
conn=psycopg2.connect(os.environ["DATABASE_URL"])
cur=conn.cursor()

for job in jobs:
    job_id=job.get("id")
    if not job_id:
        continue
    slug=job.get("slug")
    position=html.unescape(job.get("position")or "")
    company=html.unescape(job.get("company") or "")
    tags=", ".join(job.get("tags",[]))
    apply_url=job.get("apply_url")
    salary_min=job.get("salary_min") or None
    salary_max=job.get("salary_max") or None
    
    cur.execute("""
    insert into jobs (id,slug,position,company,tags,apply_url,first_seen,last_seen)
    values(%s,%s,%s,%s,%s,%s,%s,%s)
    on conflict (id) do update
    set last_seen=EXCLUDED.last_seen;""",(job_id,slug,position,company,tags,apply_url,today,today))
    cur.execute("""
    insert into job_snapshots (job_id,scraped_at, salary_min, salary_max)
    values(%s,%s,%s,%s);""",(job_id, today, salary_min, salary_max))

conn.commit()
cur.close()
conn.close()
print(f"Processed {len(jobs)} jobs on {today}.")
