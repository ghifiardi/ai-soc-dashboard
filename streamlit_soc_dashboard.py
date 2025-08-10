import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="AI-SOC Dashboard", page_icon="🧠", layout="wide")

st.markdown("# 🧠 AI-SOC Command Center")
st.success("✅ Dashboard loaded successfully!")

# Try BigQuery connection
@st.cache_data(ttl=300)
def try_bigquery():
    try:
        from google.cloud import bigquery
        client = bigquery.Client(project="chronicle-dev-2be9")
        
        query = """
        SELECT COUNT(*) as total_events
        FROM `chronicle-dev-2be9.gatra_database.siem_events`
        LIMIT 1
        """
        
        result = client.query(query).result()
        for row in result:
            return row.total_events, True
    except Exception as e:
        st.error(f"BigQuery failed: {str(e)}")
        return 0, False

# Get data
total_events, bigquery_success = try_bigquery()

st.markdown("## 📡 Telemetry Ingestion & Validation")

col1, col2, col3, col4 = st.columns(4)

if bigquery_success:
    with col1:
        st.metric("Total Events", f"{total_events:,}", "🔥 REAL BigQuery Data")
    with col2:
        st.metric("Data Source", "BigQuery", "🟢 Connected")
    with col3:
        st.metric("Project", "chronicle-dev-2be9", "✅ Authenticated")
    with col4:
        st.metric("Status", "Live", "🔥 Real SIEM Data")
    
    st.success(f"🎉 SUCCESS! Connected to BigQuery with {total_events:,} real events!")
    
else:
    with col1:
        st.metric("Total Events", "1,247", "+23 (Mock)")
    with col2:
        st.metric("Critical Alerts", "12", "+3 (Mock)")
    with col3:
        st.metric("Validation Rate", "94.2%", "+1.2% (Mock)")
    with col4:
        st.metric("False Positives", "5.8%", "-0.8% (Mock)")
    
    st.warning("Using mock data - BigQuery connection failed")

# Generate some sample events
events = []
for i in range(10):
    events.append({
        "timestamp": datetime.now() - timedelta(minutes=random.randint(1, 60)),
        "event_id": f"EVT-{random.randint(10000, 99999)}",
        "severity": random.choice(["Critical", "High", "Medium", "Low"]),
        "event_type": random.choice(["Malware", "Phishing", "DDoS", "Data Breach"]),
        "source_ip": f"192.168.1.{random.randint(1, 255)}",
        "status": random.choice(["Active", "Investigating", "Resolved"])
    })

df = pd.DataFrame(events)

st.subheader("Recent Security Events")
st.dataframe(df, use_container_width=True)

# Sidebar
st.sidebar.markdown("## 📊 Connection Status")
if bigquery_success:
    st.sidebar.success("🔥 BigQuery Connected!")
    st.sidebar.info(f"Events: {total_events:,}")
else:
    st.sidebar.error("❌ BigQuery Failed")
    st.sidebar.info("Using mock data")

st.sidebar.markdown("## ⚙️ Configuration")
st.sidebar.info("Project: chronicle-dev-2be9")
st.sidebar.info("Dataset: gatra_database")
st.sidebar.info("Table: siem_events")
