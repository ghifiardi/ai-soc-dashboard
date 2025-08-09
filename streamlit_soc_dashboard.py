import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
from datetime import datetime, timedelta
import random
import os
import sys

# Add current directory to path to import data_sources
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from data_sources import RealDataManager
    REAL_DATA_AVAILABLE = True
except ImportError:
    REAL_DATA_AVAILABLE = False
    st.warning("Real data sources not available. Using mock data only.")

# Page configuration
st.set_page_config(
    page_title="🧠 AI-SOC Command Center",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🧠 AI-SOC Command Center")
st.caption("Dashboard loaded successfully!")

# Initialize data manager
if REAL_DATA_AVAILABLE:
    if 'data_manager' not in st.session_state:
        st.session_state.data_manager = RealDataManager()

# Sidebar
st.sidebar.title("🛡️ SOC Command Center")
st.sidebar.subheader("Dashboard Controls")

# Data source selection
data_source = st.sidebar.radio(
    "Data Source",
    ["Mock Data", "Real Database", "Log Files", "API Integration"],
    help="Choose your data source for the dashboard"
)

# Database setup section
if data_source == "Real Database" and REAL_DATA_AVAILABLE:
    st.sidebar.subheader("🗄️ Database Setup")
    
    db_type = st.sidebar.selectbox("Database Type", ["SQLite", "PostgreSQL", "MySQL"])
    
    if db_type == "SQLite":
        if st.sidebar.button("Setup Sample Database"):
            with st.spinner("Creating sample database..."):
                if st.session_state.data_manager.setup_sample_database():
                    st.sidebar.success("Sample database created!")
                    st.rerun()
    
    elif db_type == "PostgreSQL":
        with st.sidebar.expander("PostgreSQL Settings"):
            pg_host = st.text_input("Host", value="localhost")
            pg_port = st.number_input("Port", value=5432)
            pg_db = st.text_input("Database")
            pg_user = st.text_input("Username")
            pg_pass = st.text_input("Password", type="password")
            
            if st.button("Connect PostgreSQL"):
                if st.session_state.data_manager.db_connector.connect_postgresql(
                    pg_host, pg_port, pg_db, pg_user, pg_pass
                ):
                    st.success("Connected to PostgreSQL!")
    
    elif db_type == "MySQL":
        with st.sidebar.expander("MySQL Settings"):
            my_host = st.text_input("Host", value="localhost")
            my_port = st.number_input("Port", value=3306)
            my_db = st.text_input("Database")
            my_user = st.text_input("Username")
            my_pass = st.text_input("Password", type="password")
            
            if st.button("Connect MySQL"):
                if st.session_state.data_manager.db_connector.connect_mysql(
                    my_host, my_port, my_db, my_user, my_pass
                ):
                    st.success("Connected to MySQL!")

# API Integration settings
elif data_source == "API Integration" and REAL_DATA_AVAILABLE:
    st.sidebar.subheader("🔗 API Settings")
    
    api_service = st.sidebar.selectbox("API Service", ["AbuseIPDB", "VirusTotal", "AlienVault OTX"])
    api_key = st.sidebar.text_input("API Key", type="password", 
                                   help="Enter your API key for threat intelligence")
    
    if api_key:
        st.sidebar.success(f"✅ {api_service} API configured")

# Log file settings
elif data_source == "Log Files" and REAL_DATA_AVAILABLE:
    st.sidebar.subheader("📄 Log File Settings")
    
    uploaded_file = st.sidebar.file_uploader(
        "Upload Log File",
        type=['json', 'csv', 'log', 'txt'],
        help="Upload your security log files"
    )
    
    if uploaded_file:
        st.sidebar.success(f"✅ File uploaded: {uploaded_file.name}")

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
    
    # Get data based on selected source
    if data_source == "Real Database" and REAL_DATA_AVAILABLE:
        try:
            df_events = st.session_state.data_manager.get_security_events()
            metrics = st.session_state.data_manager.get_real_time_metrics()
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Events", metrics.get('total_events', 0), "+Real Data")
            with col2:
                st.metric("Critical Alerts", metrics.get('critical_events', 0), "+Real Data")
            with col3:
                st.metric("High Risk Assets", metrics.get('high_risk_assets', 0), "+Real Data")
            with col4:
                st.metric("Database Status", "🟢 Connected", "Live")
                
        except Exception as e:
            st.error(f"Database error: {e}")
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
    
    elif data_source == "Log Files" and REAL_DATA_AVAILABLE and 'uploaded_file' in locals():
        try:
            # Process uploaded file
            if uploaded_file.name.endswith('.json'):
                # Save uploaded file temporarily
                with open("temp_log.json", "wb") as f:
                    f.write(uploaded_file.getvalue())
                df_events = st.session_state.data_manager.log_connector.parse_json_logs("temp_log.json")
                os.remove("temp_log.json")  # Clean up
            elif uploaded_file.name.endswith('.csv'):
                df_events = pd.read_csv(uploaded_file)
            else:
                st.warning("Unsupported file format. Using mock data.")
                df_events = generate_telemetry_data()
                
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Log Events", len(df_events), f"+{uploaded_file.name}")
            with col2:
                st.metric("File Size", f"{uploaded_file.size} bytes", "Uploaded")
            with col3:
                st.metric("File Type", uploaded_file.type, "Detected")
            with col4:
                st.metric("Status", "🟢 Processed", "Live")
                
        except Exception as e:
            st.error(f"File processing error: {e}")
            df_events = generate_telemetry_data()
    
    elif data_source == "API Integration" and REAL_DATA_AVAILABLE and 'api_key' in locals() and api_key:
        # Use mock data enriched with API data
        df_events = generate_telemetry_data()
        
        try:
            # Enrich with threat intelligence
            df_events = st.session_state.data_manager.enrich_with_threat_intel(df_events, api_key)
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Events", len(df_events), "+API Enhanced")
            with col2:
                st.metric("API Service", api_service, "🟢 Active")
            with col3:
                st.metric("Enriched IPs", len([x for x in df_events.get('ip_reputation_score', []) if pd.notna(x)]), "Threat Intel")
            with col4:
                malicious_count = len([x for x in df_events.get('is_malicious', []) if x])
                st.metric("Malicious IPs", malicious_count, "🔴 Detected")
        except Exception as e:
            st.error(f"API enrichment error: {e}")
    
    else:
        # Default to mock data
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
    if not df_events.empty:
        st.dataframe(df_events, use_container_width=True)
        
        # Severity distribution chart
        if 'severity' in df_events.columns:
            severity_counts = df_events['severity'].value_counts()
            fig = px.pie(values=severity_counts.values, names=severity_counts.index, 
                         title="Event Severity Distribution")
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No events found. Check your data source configuration.")
    
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
