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


st.subheader("Top Companies by Job Postings")
top_companies=pd.read_sql("""
select company,count(*) as job_count
from jobs group by company
order by job_count desc limit 10;""",conn)
st.dataframe(top_companies)

st.subheader("Most Common Words in Job Titles")
top_words=pd.read_sql("""
select trim(lower(word)) as word,count(*) as word_count
from jobs, unnest(string_to_array(position,' ')) as word
where length(trim(word)) >3
group by trim(lower(word)) 
order by word_count desc limit 15;""", conn)
st.bar_chart(top_words.set_index("word"))
