#!/usr/bin/env python3
import streamlit as st
import pandas as pd
from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPIError

st.set_page_config(page_title="AI-SOC Local BQ Test", page_icon="🛡️", layout="wide")

st.title("🛡️ AI-SOC Local BigQuery Connectivity Test")
st.write("This minimal app uses Application Default Credentials (ADC) via your local gcloud setup.")

# Sidebar inputs
st.sidebar.header("BigQuery Settings")
project_id = st.sidebar.text_input("Project ID", value="chronicle-dev-2be9")
dataset_id = st.sidebar.text_input("Dataset", value="gatra_database")
table_id = st.sidebar.text_input("Table", value="siem_events")
row_limit = st.sidebar.number_input("Row limit", min_value=1, max_value=1000, value=50)

st.sidebar.info("Make sure you've run: gcloud auth application-default login")

def try_connect_and_query(project: str, dataset: str, table: str, limit: int):
    try:
        st.info("🔍 Initializing BigQuery client using ADC...")
        client = bigquery.Client(project=project)
        st.success("✅ BigQuery client initialized")

        metrics_sql = f"""
        SELECT 
          COUNT(*) AS total_events,
          COUNT(DISTINCT alarmId) AS unique_alarms
        FROM `{project}.{dataset}.{table}`
        """
        st.code(metrics_sql, language="sql")
        st.info("📊 Running metrics query...")
        metrics_rows = list(client.query(metrics_sql).result())
        if not metrics_rows:
            st.warning("No metrics returned.")
            return
        m = metrics_rows[0]
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Events", f"{m.total_events:,}")
        col2.metric("Unique Alarms", f"{m.unique_alarms:,}")
        col3.metric("Status", "LIVE", "BigQuery")

        sample_sql = f"""
        SELECT alarmId, events, processed_by_ada
        FROM `{project}.{dataset}.{table}`
        ORDER BY alarmId DESC
        LIMIT {limit}
        """
        st.code(sample_sql, language="sql")
        st.info("📥 Fetching sample rows...")
        df = client.query(sample_sql).to_dataframe()
        st.success(f"✅ Retrieved {len(df)} rows")
        st.dataframe(df if len(df) <= 200 else df.head(200), use_container_width=True)
    except GoogleAPIError as ge:
        st.error("❌ Google API Error while querying BigQuery")
        st.exception(ge)
    except Exception as e:
        st.error("❌ Unexpected error")
        st.exception(e)

if st.button("Run BigQuery Test", type="primary"):
    try_connect_and_query(project_id, dataset_id, table_id, int(row_limit))
