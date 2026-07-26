import os 
import psycopg2
from dotenv import load_dotenv
load_dotenv()
conn=psycopg2.connect(os.environ["DATABASE_URL"])
cur=conn.cursor()
cur.execute("""
create table if not exists jobs(
    id  text primary key,
    slug text,
    position text,
    company text,
    tags text,
    apply_url text,
    first_seen date,
    last_seen date);
""")
cur.execute("""
create table if not exists job_snapshots(
    id serial primary key,
    job_id text references jobs(id),
    scraped_at date,
    salary_min integer,
    salary_max integer
);
""")
conn.commit()
cur.close()
conn.close()
print("Tables created successfully")