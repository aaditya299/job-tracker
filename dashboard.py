import os
import pandas as pd
import psycopg2
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
conn=psycopg2.connect(os.environ["DATABASE_URL"])
st.title("Job Tracker Dashboard")
total_jobs=pd.read_sql("select count(*) as total from jobs;",conn)
st.metric("Total jobs tracked",total_jobs["total"][0])
