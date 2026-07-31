# JOB TRACKER
 
A tool that fetches remote job listings daily, stores the latest as well as the histry of the data as snapshots using PostgreSQL, analyzes the trends and visualize it using Streamlit.

- The data comes from a site remoteok.com URL- https://remoteok.com/api
- The data fetched then is stored in neon database, using queries the data is filtered 
- The dashboard is shown using streamlit, pandas is used for tables and visuals
- For now, the dashboard shows total jobs tracked, the top companies ranked by the job postings along the job count, and a bargraph showing the trends and popular jobs
- The database is updated regularly where new vacant jobs are added and the positions which no longer exists are frozen
- The data fetched has been automated using github actions which runs daily at a specific time without any mannual effort

Architecture
- The database consists of two tables jobs and job_snapshots
- The jobs table contains the fresh data having the job position vacant updated regularly
- The job_snapshots table logs a row every day for every job still active, mainly to track salary and presence over time
