import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
from datetime import datetime, timedelta
import random

# Page configuration
st.set_page_config(
    page_title="🧠 AI-SOC Command Center",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🧠 AI-SOC Command Center")
st.caption("Dashboard loaded successfully!")

# Sidebar
st.sidebar.title("🛡️ SOC Command Center")
st.sidebar.subheader("Dashboard Controls")

# Section selection
sections = st.sidebar.multiselect(
    "Select Sections to Display",
    [
        "📡 Telemetry Ingestion",
        "🤖 AI Enrichment", 
        "⚖️ Risk Decision Engine",
        "🔧 Patch Management",
        "📊 Compliance Reporting",
        "⚙️ System Health"
    ],
    default=["📡 Telemetry Ingestion", "🤖 AI Enrichment"]
)

auto_refresh = st.sidebar.checkbox("Auto-refresh (10s)", value=False)

st.caption("Sidebar configured successfully!")

# Mock data generators
def generate_telemetry_data():
    """Generate mock telemetry data"""
    events = []
    severities = ["Critical", "High", "Medium", "Low"]
    event_types = ["Malware", "Phishing", "DDoS", "Data Breach", "Insider Threat"]
    
    for i in range(20):
        events.append({
            "timestamp": datetime.now() - timedelta(minutes=random.randint(1, 60)),
            "event_id": f"EVT-{random.randint(10000, 99999)}",
            "severity": random.choice(severities),
            "event_type": random.choice(event_types),
            "source_ip": f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}",
            "status": random.choice(["Validated", "Pending", "False Positive"])
        })
    
    return pd.DataFrame(events)

# Main content sections
if "📡 Telemetry Ingestion" in sections:
    st.header("📡 Telemetry Ingestion & Validation")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Events", "1,247", "+23")
    with col2:
        st.metric("Critical Alerts", "12", "+3")
    with col3:
        st.metric("Validation Rate", "94.2%", "+1.2%")
    with col4:
        st.metric("False Positives", "5.8%", "-0.8%")
    
    # Event table
    df_events = generate_telemetry_data()
    st.subheader("Recent Security Events")
    st.dataframe(df_events, use_container_width=True)
    
    # Severity distribution chart
    severity_counts = df_events['severity'].value_counts()
    fig = px.pie(values=severity_counts.values, names=severity_counts.index, 
                 title="Event Severity Distribution")
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")

if "🤖 AI Enrichment" in sections:
    st.header("🤖 AI Enrichment & Correlation Engine")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("MITRE ATT&CK Mapping")
        
        # Mock MITRE data
        mitre_data = {
            "Technique": ["T1566.001", "T1059.001", "T1055", "T1070.004", "T1083"],
            "Tactic": ["Initial Access", "Execution", "Defense Evasion", "Defense Evasion", "Discovery"],
            "Confidence": [0.95, 0.87, 0.92, 0.78, 0.83],
            "Count": [15, 12, 8, 6, 10]
        }
        
        df_mitre = pd.DataFrame(mitre_data)
        st.dataframe(df_mitre, use_container_width=True)
        
        # Confidence chart
        fig = px.bar(df_mitre, x='Technique', y='Confidence', 
                     title="MITRE Technique Confidence Scores")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Asset Risk Heatmap")
        
        # Generate heatmap data
        assets = ['Web Server', 'Database', 'Domain Controller', 'Workstation', 'Firewall']
        risk_levels = ['Low', 'Medium', 'High', 'Critical']
        
        heatmap_data = np.random.randint(0, 10, size=(len(assets), len(risk_levels)))
        
        fig = px.imshow(heatmap_data, 
                       x=risk_levels, 
                       y=assets,
                       color_continuous_scale='Reds',
                       title="Asset Risk Assessment")
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")

if "⚖️ Risk Decision Engine" in sections:
    st.header("⚖️ Autonomous Risk Decision Engine")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Auto-Remediated", "156", "+12")
        st.metric("Analyst Review", "23", "+5")
        st.metric("IR Escalated", "8", "+2")
    
    with col2:
        # Decision flow chart
        decisions = ['Auto-Remediate', 'Analyst Review', 'IR Escalation']
        values = [156, 23, 8]
        
        fig = px.funnel(y=decisions, x=values, title="Risk Decision Flow")
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")

if "🔧 Patch Management" in sections:
    st.header("🔧 Autonomous Patch Management")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Active Deployments", "47", "+8")
    with col2:
        st.metric("Success Rate", "96.2%", "+2.1%")
    with col3:
        st.metric("Rollbacks", "2", "-1")
    
    # Patch status chart
    patch_status = {
        'Status': ['Deployed', 'In Progress', 'Failed', 'Pending'],
        'Count': [142, 47, 8, 23]
    }
    
    df_patches = pd.DataFrame(patch_status)
    fig = px.bar(df_patches, x='Status', y='Count', title="Patch Deployment Status")
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")

if "📊 Compliance Reporting" in sections:
    st.header("📊 Governance & Compliance Reporting")
    
    # Compliance scores
    frameworks = ['NIST', 'ISO 27001', 'SOC 2', 'PCI DSS', 'GDPR']
    scores = [94, 91, 88, 96, 89]
    
    col1, col2 = st.columns(2)
    
    with col1:
        for framework, score in zip(frameworks, scores):
            st.metric(framework, f"{score}%", f"+{random.randint(1, 3)}%")
    
    with col2:
        fig = px.bar(x=frameworks, y=scores, title="Compliance Framework Scores")
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")

if "⚙️ System Health" in sections:
    st.header("⚙️ System Health & Performance")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("CPU Usage", "67%", "+5%")
    with col2:
        st.metric("Memory", "8.2GB", "+0.3GB")
    with col3:
        st.metric("Uptime", "99.9%", "0%")
    with col4:
        st.metric("Avg Latency", "23ms", "-2ms")
    
    # Performance chart
    times = pd.date_range(start='2024-01-01', periods=24, freq='H')
    cpu_data = np.random.normal(65, 10, 24)
    memory_data = np.random.normal(8, 1, 24)
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(x=times, y=cpu_data, name="CPU %"),
        secondary_y=False,
    )
    
    fig.add_trace(
        go.Scatter(x=times, y=memory_data, name="Memory GB"),
        secondary_y=True,
    )
    
    fig.update_layout(title="System Performance (24h)")
    fig.update_yaxes(title_text="CPU %", secondary_y=False)
    fig.update_yaxes(title_text="Memory GB", secondary_y=True)
    
    st.plotly_chart(fig, use_container_width=True)

# Auto-refresh logic
if auto_refresh:
    time.sleep(10)
    st.rerun()

st.caption("Dashboard rendering complete!")
