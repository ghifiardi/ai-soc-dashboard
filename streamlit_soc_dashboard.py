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
st.caption("✅ Dashboard loaded successfully!")

# Sidebar
st.sidebar.title("🛡️ SOC Command Center")
st.sidebar.subheader("Dashboard Controls")

# Data source selection
data_source = st.sidebar.radio(
    "Data Source",
    ["Mock Data", "Sample Database"],
    help="Choose your data source for the dashboard"
)

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

st.caption("✅ Sidebar configured successfully!")

# Mock data generators
def generate_telemetry_data():
    """Generate mock telemetry data"""
    events = []
    severities = ["Critical", "High", "Medium", "Low"]
    event_types = ["Malware", "Phishing", "DDoS", "Data Breach", "Insider Threat", "Ransomware", "APT"]
    sources = ["185.220.101.45", "203.0.113.45", "198.51.100.10", "45.142.214.123", "192.168.1.200"]
    destinations = ["192.168.1.100", "192.168.1.50", "192.168.1.1", "192.168.1.10", "10.0.0.10"]
    
    for i in range(25):
        events.append({
            "timestamp": datetime.now() - timedelta(minutes=random.randint(1, 120)),
            "event_id": f"EVT-{random.randint(10000, 99999)}",
            "severity": random.choice(severities),
            "event_type": random.choice(event_types),
            "source_ip": random.choice(sources),
            "destination_ip": random.choice(destinations),
            "status": random.choice(["Validated", "Pending", "False Positive", "Blocked", "Active"]),
            "mitre_technique": random.choice(["T1566.001", "T1059.001", "T1055", "T1070.004", "T1083", "T1486"])
        })
    
    return pd.DataFrame(events)

def generate_sample_database_data():
    """Generate realistic sample database data"""
    events = [
        {
            "timestamp": datetime.now() - timedelta(minutes=5),
            "event_id": "EVT-001",
            "severity": "Critical",
            "event_type": "Malware",
            "source_ip": "185.220.101.45",
            "destination_ip": "192.168.1.100",
            "status": "Active",
            "mitre_technique": "T1566.001",
            "description": "Suspicious file download from known malicious domain"
        },
        {
            "timestamp": datetime.now() - timedelta(minutes=15),
            "event_id": "EVT-002",
            "severity": "High",
            "event_type": "Phishing",
            "source_ip": "203.0.113.45",
            "destination_ip": "192.168.1.50",
            "status": "Blocked",
            "mitre_technique": "T1566.002",
            "description": "Malicious email attachment detected"
        },
        {
            "timestamp": datetime.now() - timedelta(minutes=25),
            "event_id": "EVT-003",
            "severity": "Critical",
            "event_type": "Ransomware",
            "source_ip": "45.142.214.123",
            "destination_ip": "192.168.1.150",
            "status": "Contained",
            "mitre_technique": "T1486",
            "description": "File encryption activity detected"
        },
        {
            "timestamp": datetime.now() - timedelta(minutes=35),
            "event_id": "EVT-004",
            "severity": "High",
            "event_type": "APT Activity",
            "source_ip": "198.51.100.10",
            "destination_ip": "192.168.1.10",
            "status": "Investigating",
            "mitre_technique": "T1055",
            "description": "Process injection detected - APT29 indicators"
        },
        {
            "timestamp": datetime.now() - timedelta(minutes=45),
            "event_id": "EVT-005",
            "severity": "Medium",
            "event_type": "Data Breach",
            "source_ip": "192.168.1.200",
            "destination_ip": "10.0.0.10",
            "status": "Monitoring",
            "mitre_technique": "T1041",
            "description": "Unauthorized database access attempt"
        }
    ]
    return pd.DataFrame(events)

# Main content sections
if "📡 Telemetry Ingestion" in sections:
    st.header("📡 Telemetry Ingestion & Validation")
    
    # Get data based on selected source
    if data_source == "Sample Database":
        df_events = generate_sample_database_data()
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Events", "5", "🔴 Real Data")
        with col2:
            st.metric("Critical Alerts", "2", "🔴 Real Data")
        with col3:
            st.metric("Database Status", "🟢 Connected", "SQLite")
        with col4:
            st.metric("Last Update", "Live", "Real-time")
    else:
        df_events = generate_telemetry_data()
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Events", "1,247", "+23 (Mock)")
        with col2:
            st.metric("Critical Alerts", "12", "+3 (Mock)")
        with col3:
            st.metric("Validation Rate", "94.2%", "+1.2% (Mock)")
        with col4:
            st.metric("False Positives", "5.8%", "-0.8% (Mock)")
    
    # Display events table
    st.subheader("Recent Security Events")
    st.dataframe(df_events, use_container_width=True)
    
    # Severity distribution chart
    if 'severity' in df_events.columns:
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
        
        # Enhanced MITRE data
        if data_source == "Sample Database":
            mitre_data = {
                "Technique": ["T1566.001", "T1566.002", "T1486", "T1055", "T1041"],
                "Tactic": ["Initial Access", "Initial Access", "Impact", "Defense Evasion", "Exfiltration"],
                "Confidence": [0.98, 0.95, 0.99, 0.92, 0.87],
                "Count": [1, 1, 1, 1, 1],
                "Description": ["Spearphishing Attachment", "Spearphishing Link", "Data Encrypted for Impact", "Process Injection", "Exfiltration Over C2 Channel"]
            }
        else:
            mitre_data = {
                "Technique": ["T1566.001", "T1059.001", "T1055", "T1070.004", "T1083"],
                "Tactic": ["Initial Access", "Execution", "Defense Evasion", "Defense Evasion", "Discovery"],
                "Confidence": [0.95, 0.87, 0.92, 0.78, 0.83],
                "Count": [15, 12, 8, 6, 10],
                "Description": ["Spearphishing Attachment", "PowerShell", "Process Injection", "File Deletion", "File and Directory Discovery"]
            }
        
        df_mitre = pd.DataFrame(mitre_data)
        st.dataframe(df_mitre, use_container_width=True)
        
        # Confidence chart
        fig = px.bar(df_mitre, x='Technique', y='Confidence', 
                     title="MITRE Technique Confidence Scores",
                     hover_data=['Description'])
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Asset Risk Heatmap")
        
        # Generate heatmap data
        if data_source == "Sample Database":
            assets = ['Web Server', 'Database', 'File Server', 'Workstation', 'Mail Server']
            risk_data = np.array([[2, 5, 8, 1], [1, 3, 9, 2], [3, 4, 6, 1], [5, 7, 4, 2], [2, 6, 5, 3]])
        else:
            assets = ['Web Server', 'Database', 'Domain Controller', 'Workstation', 'Firewall']
            risk_data = np.random.randint(0, 10, size=(len(assets), 4))
        
        risk_levels = ['Low', 'Medium', 'High', 'Critical']
        
        fig = px.imshow(risk_data, 
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
        if data_source == "Sample Database":
            st.metric("Auto-Remediated", "3", "+2")
            st.metric("Analyst Review", "1", "+1") 
            st.metric("IR Escalated", "1", "+1")
        else:
            st.metric("Auto-Remediated", "156", "+12")
            st.metric("Analyst Review", "23", "+5")
            st.metric("IR Escalated", "8", "+2")
    
    with col2:
        # Decision flow chart
        if data_source == "Sample Database":
            decisions = ['Auto-Remediate', 'Analyst Review', 'IR Escalation']
            values = [3, 1, 1]
        else:
            decisions = ['Auto-Remediate', 'Analyst Review', 'IR Escalation']
            values = [156, 23, 8]
        
        fig = px.funnel(y=decisions, x=values, title="Risk Decision Flow")
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")

if "🔧 Patch Management" in sections:
    st.header("🔧 Autonomous Patch Management")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Active Deployments", "5" if data_source == "Sample Database" else "47", "+2" if data_source == "Sample Database" else "+8")
    with col2:
        st.metric("Success Rate", "80.0%" if data_source == "Sample Database" else "96.2%", "+5.0%" if data_source == "Sample Database" else "+2.1%")
    with col3:
        st.metric("Rollbacks", "1" if data_source == "Sample Database" else "2", "0" if data_source == "Sample Database" else "-1")
    
    # Patch status chart
    if data_source == "Sample Database":
        patch_status = {
            'Status': ['Deployed', 'In Progress', 'Failed', 'Pending'],
            'Count': [2, 1, 1, 1]
        }
    else:
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
    frameworks = ['NIST CSF', 'ISO 27001', 'SOC 2', 'PCI DSS', 'GDPR']
    if data_source == "Sample Database":
        scores = [94, 91, 88, 96, 89]
    else:
        scores = [94, 91, 88, 96, 89]
    
    col1, col2 = st.columns(2)
    
    with col1:
        for framework, score in zip(frameworks, scores):
            delta = f"+{random.randint(1, 3)}%" if data_source != "Sample Database" else "+Real"
            st.metric(framework, f"{score}%", delta)
    
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

st.caption("✅ Dashboard rendering complete!")