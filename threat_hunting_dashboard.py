#!/usr/bin/env python3
"""
🔍 AI-Powered Threat Hunting Dashboard
Advanced threat hunting with AI agents, behavioral analytics, and real-time detection
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import random
import json

# Configure page
st.set_page_config(
    page_title="🔍 Threat Hunting Dashboard",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    :root {
        --hunt-dark: #0A0E1F;
        --hunt-blue: #2563EB;
        --hunt-cyan: #06B6D4;
        --hunt-green: #10B981;
        --hunt-amber: #F59E0B;
        --hunt-red: #EF4444;
        --hunt-purple: #8B5CF6;
    }

    .main {
        background: linear-gradient(135deg, #0A0E1F 0%, #1E293B 100%);
    }

    .hunt-header {
        font-size: 2.8rem;
        font-weight: 800;
        color: var(--hunt-cyan);
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 20px rgba(6, 182, 212, 0.5);
    }

    .hunt-subtitle {
        text-align: center;
        color: rgba(255, 255, 255, 0.7);
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .metric-box {
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.1), rgba(6, 182, 212, 0.1));
        border: 2px solid rgba(6, 182, 212, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }

    .metric-box:hover {
        border-color: var(--hunt-cyan);
        box-shadow: 0 8px 24px rgba(6, 182, 212, 0.3);
        transform: translateY(-4px);
    }

    .metric-value {
        font-size: 2.5rem;
        font-weight: 800;
        color: white;
        margin: 0.5rem 0;
    }

    .metric-label {
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.7);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .alert-card {
        background: rgba(255, 255, 255, 0.05);
        border-left: 4px solid var(--hunt-red);
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }

    .alert-card:hover {
        background: rgba(255, 255, 255, 0.08);
        transform: translateX(4px);
    }

    .hunt-panel {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
    }

    .section-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--hunt-cyan);
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .threat-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
    }

    .badge-critical { background: #7F1D1D; color: #FEE2E2; }
    .badge-high { background: #92400E; color: #FED7AA; }
    .badge-medium { background: #1E40AF; color: #DBEAFE; }
    .badge-low { background: #065F46; color: #D1FAE5; }

    .hunt-mission {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(37, 99, 235, 0.1));
        border: 2px solid rgba(139, 92, 246, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
    }

    .timestamp-live {
        color: var(--hunt-green);
        font-weight: 600;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'last_refresh' not in st.session_state:
    st.session_state.last_refresh = datetime.now()

# Helper Functions
def generate_realtime_alerts(num_alerts=20):
    """Generate security alerts with CURRENT timestamps"""
    alerts = []

    alert_types = [
        "Malware Detection Alert",
        "Network Intrusion Alert",
        "Authentication Anomaly",
        "Advanced Persistent Threat Detection",
        "Suspicious Network Activity Detected",
        "Data Exfiltration Attempt",
        "Privilege Escalation Detected",
        "Lateral Movement Alert",
        "Command & Control Communication",
        "Zero-Day Exploit Detected"
    ]

    severities = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
    severity_weights = [0.15, 0.30, 0.40, 0.15]

    sources = [
        "Email Security Gateway",
        "Network Security Monitor",
        "Identity Management System",
        "Advanced Threat Detection System",
        "Endpoint Detection & Response",
        "SIEM Platform",
        "Firewall",
        "IDS/IPS"
    ]

    # Generate alerts with timestamps from the last few hours
    for i in range(num_alerts):
        # Generate timestamps within the last 24 hours
        minutes_ago = random.randint(1, 1440)  # Last 24 hours
        timestamp = datetime.now() - timedelta(minutes=minutes_ago)

        severity = random.choices(severities, weights=severity_weights)[0]

        alerts.append({
            'timestamp': timestamp,
            'title': random.choice(alert_types),
            'severity': severity,
            'source': random.choice(sources),
            'is_true_positive': random.choice([True, False, None]),
            'confidence': random.uniform(0.65, 0.99),
            'hunt_status': random.choice(['Active', 'Investigating', 'Resolved', 'False Positive'])
        })

    return pd.DataFrame(alerts).sort_values('timestamp', ascending=False)

def generate_social_media_threats(num_threats=50):
    """Generate social media threats with CURRENT timestamps"""
    threats = []

    keywords_list = [
        "IOH,mahal,paket,internet",
        "Indosat,IM3,down,gangguan,internet,jaringan",
        "XL,lemot,internet,down",
        "Telkomsel,gangguan,jaringan,down",
        "data,breach,leak,password",
        "malware,virus,ransomware",
        "phishing,scam,fraud",
        "DDoS,attack,down"
    ]

    texts = [
        "IOH paket internet mahal banget, mending pindah ke kompetitor aja",
        "Indosat jaringan down lagi nih, gak bisa internet! #IM3 #gangguan",
        "XL lemot banget hari ini, ada yang ngalamin juga?",
        "Telkomsel error terus, jaringan down di area Jakarta",
        "Ada data breach di perusahaan X, password leaked!",
        "Hati-hati malware baru menyebar via email phishing",
        "Website perusahaan Y kena DDoS attack, down total",
        "Ransomware attack hits major corporation, data encrypted"
    ]

    severities = ["High", "Medium", "Low"]
    severity_weights = [0.25, 0.50, 0.25]

    # Generate threats from last 48 hours
    for i in range(num_threats):
        minutes_ago = random.randint(1, 2880)  # Last 48 hours
        timestamp = datetime.now() - timedelta(minutes=minutes_ago)

        severity = random.choices(severities, weights=severity_weights)[0]
        text = random.choice(texts)
        keywords = random.choice(keywords_list)

        threats.append({
            'created_at': timestamp,
            'text': text,
            'threat_score': random.uniform(0.5, 0.9),
            'severity': severity,
            'keywords_found': keywords,
            'platform': random.choice(['Twitter', 'Facebook', 'Instagram', 'LinkedIn', 'Reddit']),
            'engagement': random.randint(10, 5000),
            'verified_threat': random.choice([True, False])
        })

    return pd.DataFrame(threats).sort_values('created_at', ascending=False)

def generate_hunt_missions(num_missions=10):
    """Generate active threat hunting missions"""
    missions = []

    hunt_types = [
        "Insider Threat Detection",
        "APT Campaign Tracking",
        "Credential Theft Investigation",
        "Lateral Movement Analysis",
        "Command & Control Hunt",
        "Data Exfiltration Search",
        "Malware Family Investigation",
        "Zero-Day Vulnerability Hunt"
    ]

    statuses = ["Active", "Investigating", "Completed", "On Hold"]
    status_weights = [0.30, 0.35, 0.25, 0.10]

    for i in range(num_missions):
        # Missions started within last 30 days
        days_ago = random.randint(0, 30)
        start_date = datetime.now() - timedelta(days=days_ago)

        status = random.choices(statuses, weights=status_weights)[0]

        missions.append({
            'mission_id': f"HUNT-{2026}{random.randint(1000, 9999)}",
            'hunt_type': random.choice(hunt_types),
            'start_date': start_date,
            'status': status,
            'iocs_found': random.randint(0, 50),
            'entities_analyzed': random.randint(100, 5000),
            'confidence': random.uniform(0.60, 0.95),
            'priority': random.choice(['Critical', 'High', 'Medium', 'Low']),
            'hunter': f"Analyst {random.randint(1, 10)}"
        })

    return pd.DataFrame(missions).sort_values('start_date', ascending=False)

def generate_ml_alert_analysis(num_classifications=30):
    """Generate ML-powered alert classifications"""
    classifications = []

    ml_models = [
        "Random Forest Classifier",
        "Neural Network",
        "Gradient Boosting",
        "Deep Learning CNN",
        "XGBoost Classifier",
        "Isolation Forest",
        "Autoencoder Anomaly"
    ]

    alert_categories = [
        "Malware",
        "Network Intrusion",
        "Data Breach",
        "Insider Threat",
        "DDoS Attack",
        "Phishing",
        "Ransomware",
        "Zero-Day"
    ]

    for i in range(num_classifications):
        confidence = random.uniform(0.70, 0.99)

        classifications.append({
            'model': random.choice(ml_models),
            'category': random.choice(alert_categories),
            'confidence': confidence,
            'true_positive_rate': random.uniform(0.75, 0.95),
            'false_positive_rate': random.uniform(0.02, 0.15),
            'predictions': random.randint(50, 500)
        })

    return pd.DataFrame(classifications)

# Sidebar
with st.sidebar:
    st.markdown("### 🔍 Hunt Controls")
    st.markdown("---")

    # Time range
    time_range = st.selectbox(
        "Time Range",
        options=["Last Hour", "Last 6 Hours", "Last 24 Hours", "Last 7 Days", "Last 30 Days"],
        index=2
    )

    # Hunt focus
    hunt_focus = st.multiselect(
        "Hunt Focus",
        options=["APT", "Insider Threat", "Malware", "Data Exfiltration", "Lateral Movement", "C2 Detection"],
        default=["APT", "Insider Threat", "Malware"]
    )

    st.markdown("---")

    # Confidence threshold
    confidence_threshold = st.slider(
        "Confidence Threshold",
        min_value=0.5,
        max_value=1.0,
        value=0.7,
        step=0.05
    )

    # Auto-refresh
    st.markdown("### 🔄 Auto-Refresh")
    auto_refresh = st.checkbox("Enable", value=False)

    if auto_refresh:
        refresh_interval = st.slider("Interval (seconds)", 10, 60, 30)

    st.markdown("---")

    # Hunt statistics
    st.markdown("### 📊 Hunt Stats")
    st.metric("Active Hunters", "8")
    st.metric("Missions Today", "12")
    st.metric("IOCs Discovered", "47")

# Main Header
st.markdown('<h1 class="hunt-header">🔍 THREAT HUNTING DASHBOARD</h1>', unsafe_allow_html=True)
st.markdown('<p class="hunt-subtitle">AI-Powered Proactive Threat Detection & Investigation</p>', unsafe_allow_html=True)

# Current timestamp display
current_time = datetime.now()
st.markdown(f'<div style="text-align: center; color: var(--hunt-green); font-size: 1.1rem; font-weight: 600; margin-bottom: 2rem;">🕐 Current Time: <span class="timestamp-live">{current_time.strftime("%Y-%m-%d %H:%M:%S")}</span></div>', unsafe_allow_html=True)

# Generate data
alerts_df = generate_realtime_alerts(20)
social_media_df = generate_social_media_threats(50)
missions_df = generate_hunt_missions(10)
ml_analysis_df = generate_ml_alert_analysis(30)

# Overview Metrics
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_hunts = len(missions_df[missions_df['status'] == 'Active'])
    st.markdown(f'''
    <div class="metric-box">
        <div class="metric-label">Total Hunts</div>
        <div class="metric-value">{total_hunts}</div>
        <div style="color: var(--hunt-green); font-size: 0.9rem;">Active Investigations</div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    critical_alerts = len(alerts_df[alerts_df['severity'] == 'CRITICAL'])
    st.markdown(f'''
    <div class="metric-box">
        <div class="metric-label">Critical</div>
        <div class="metric-value">{critical_alerts}</div>
        <div style="color: var(--hunt-red); font-size: 0.9rem;">High Priority Alerts</div>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    ml_processed = len(alerts_df)
    st.markdown(f'''
    <div class="metric-box">
        <div class="metric-label">ML Processed</div>
        <div class="metric-value">{ml_processed}</div>
        <div style="color: var(--hunt-purple); font-size: 0.9rem;">AI Analyzed</div>
    </div>
    ''', unsafe_allow_html=True)

with col4:
    social_threats = len(social_media_df[social_media_df['severity'] == 'High'])
    st.markdown(f'''
    <div class="metric-box">
        <div class="metric-label">Social Media</div>
        <div class="metric-value">{social_threats}</div>
        <div style="color: var(--hunt-amber); font-size: 0.9rem;">Threats Detected</div>
    </div>
    ''', unsafe_allow_html=True)

# Threat Hunting Overview Section
st.markdown('<div class="hunt-panel">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📊 Threat Hunting Overview</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Hunt missions status
    mission_status = missions_df['status'].value_counts()

    fig = go.Figure(data=[
        go.Pie(
            labels=mission_status.index,
            values=mission_status.values,
            hole=0.4,
            marker=dict(colors=['#06B6D4', '#F59E0B', '#10B981', '#6B7280']),
            textinfo='label+percent'
        )
    ])

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        height=300,
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=True,
        legend=dict(orientation='h', yanchor='bottom', y=-0.2)
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Priority distribution
    priority_counts = missions_df['priority'].value_counts()

    fig = go.Figure(data=[
        go.Bar(
            x=priority_counts.index,
            y=priority_counts.values,
            marker=dict(
                color=priority_counts.values,
                colorscale='Reds',
                showscale=False
            ),
            text=priority_counts.values,
            textposition='auto'
        )
    ])

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(title='Priority Level', gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(title='Count', gridcolor='rgba(255,255,255,0.1)'),
        height=300
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Security Alerts Section
st.markdown('<div class="hunt-panel">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🚨 Security Alerts</div>', unsafe_allow_html=True)

# Display alerts with proper formatting
st.markdown(f"**Showing {len(alerts_df)} most recent alerts**")

# Create expandable table
display_alerts = alerts_df.head(10).copy()
display_alerts['timestamp'] = display_alerts['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')

st.dataframe(
    display_alerts[['timestamp', 'title', 'severity', 'source', 'confidence', 'hunt_status']],
    use_container_width=True,
    height=400
)

st.markdown('</div>', unsafe_allow_html=True)

# ML-Powered Alert Analysis
st.markdown('<div class="hunt-panel">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🤖 ML-Powered Alert Analysis</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # ML model confidence distribution
    fig = px.box(
        ml_analysis_df,
        x='model',
        y='confidence',
        color='model',
        title='ML Model Confidence Distribution'
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(title='', tickangle=-45, gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(title='Confidence Score', gridcolor='rgba(255,255,255,0.1)'),
        height=350,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Alert category distribution
    category_stats = ml_analysis_df.groupby('category').agg({
        'confidence': 'mean',
        'predictions': 'sum'
    }).reset_index()

    fig = go.Figure(data=[
        go.Bar(
            x=category_stats['category'],
            y=category_stats['predictions'],
            marker=dict(
                color=category_stats['confidence'],
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title='Avg Confidence')
            ),
            text=category_stats['predictions'],
            textposition='auto'
        )
    ])

    fig.update_layout(
        title='Alert Categories by ML Predictions',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(title='Category', tickangle=-45, gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(title='Predictions', gridcolor='rgba(255,255,255,0.1)'),
        height=350
    )

    st.plotly_chart(fig, use_container_width=True)

# Display ML stats
col1, col2, col3 = st.columns(3)

with col1:
    avg_confidence = ml_analysis_df['confidence'].mean()
    st.metric("Avg ML Confidence", f"{avg_confidence:.1%}")

with col2:
    avg_tpr = ml_analysis_df['true_positive_rate'].mean()
    st.metric("True Positive Rate", f"{avg_tpr:.1%}")

with col3:
    avg_fpr = ml_analysis_df['false_positive_rate'].mean()
    st.metric("False Positive Rate", f"{avg_fpr:.1%}")

st.markdown('</div>', unsafe_allow_html=True)

# Social Media Threat Monitoring
st.markdown('<div class="hunt-panel">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📱 Social Media Threat Monitoring</div>', unsafe_allow_html=True)

# Threat score distribution over time
social_media_df['hour'] = social_media_df['created_at'].dt.floor('H')
hourly_threats = social_media_df.groupby('hour').agg({
    'threat_score': 'mean',
    'text': 'count'
}).reset_index()
hourly_threats.columns = ['hour', 'avg_threat_score', 'count']

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(
        x=hourly_threats['hour'],
        y=hourly_threats['count'],
        name='Threat Count',
        line=dict(color='#06B6D4', width=3),
        fill='tozeroy'
    ),
    secondary_y=False
)

fig.add_trace(
    go.Scatter(
        x=hourly_threats['hour'],
        y=hourly_threats['avg_threat_score'],
        name='Avg Threat Score',
        line=dict(color='#F59E0B', width=3)
    ),
    secondary_y=True
)

fig.update_layout(
    title='Social Media Threat Timeline',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    xaxis=dict(title='Time', gridcolor='rgba(255,255,255,0.1)'),
    height=350,
    hovermode='x unified'
)

fig.update_yaxes(title_text='Threat Count', secondary_y=False, gridcolor='rgba(255,255,255,0.1)')
fig.update_yaxes(title_text='Avg Threat Score', secondary_y=True, gridcolor='rgba(255,255,255,0.1)')

st.plotly_chart(fig, use_container_width=True)

# Top threat keywords
st.markdown("#### Top Threat Keywords")

keyword_freq = {}
for keywords in social_media_df['keywords_found']:
    for keyword in keywords.split(','):
        keyword = keyword.strip()
        keyword_freq[keyword] = keyword_freq.get(keyword, 0) + 1

top_keywords = pd.DataFrame(
    sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)[:10],
    columns=['Keyword', 'Frequency']
)

fig = px.bar(
    top_keywords,
    x='Frequency',
    y='Keyword',
    orientation='h',
    color='Frequency',
    color_continuous_scale='Reds'
)

fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    height=300,
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

# Recent social media threats table
st.markdown("#### Recent Social Media Threats")

display_social = social_media_df.head(15).copy()
display_social['created_at'] = display_social['created_at'].dt.strftime('%Y-%m-%d %H:%M:%S')

st.dataframe(
    display_social[['created_at', 'text', 'threat_score', 'severity', 'platform', 'engagement']],
    use_container_width=True,
    height=400
)

st.markdown('</div>', unsafe_allow_html=True)

# Active Hunt Missions
st.markdown('<div class="hunt-panel">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🎯 Active Hunt Missions</div>', unsafe_allow_html=True)

for idx, mission in missions_df.head(5).iterrows():
    status_color = {
        'Active': '#06B6D4',
        'Investigating': '#F59E0B',
        'Completed': '#10B981',
        'On Hold': '#6B7280'
    }.get(mission['status'], '#6B7280')

    priority_badge = f"badge-{mission['priority'].lower()}"

    st.markdown(f'''
    <div class="hunt-mission">
        <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
            <div>
                <strong style="color: white; font-size: 1.2rem;">{mission['mission_id']}: {mission['hunt_type']}</strong>
                <div style="margin-top: 0.5rem;">
                    <span class="threat-badge {priority_badge}">{mission['priority']}</span>
                    <span style="background: {status_color}; color: white; padding: 0.3rem 0.8rem; border-radius: 12px; font-size: 0.75rem; font-weight: 700; margin-left: 0.5rem;">
                        {mission['status']}
                    </span>
                </div>
            </div>
            <div style="text-align: right;">
                <div style="color: var(--hunt-cyan); font-weight: 600;">Confidence: {mission['confidence']:.0%}</div>
                <div style="color: rgba(255,255,255,0.7); font-size: 0.9rem; margin-top: 0.3rem;">
                    Started: {mission['start_date'].strftime('%Y-%m-%d %H:%M')}
                </div>
            </div>
        </div>
        <div style="display: flex; gap: 2rem; color: rgba(255,255,255,0.8); font-size: 0.9rem;">
            <div>📊 IOCs Found: <strong>{mission['iocs_found']}</strong></div>
            <div>🔍 Entities Analyzed: <strong>{mission['entities_analyzed']:,}</strong></div>
            <div>👤 Hunter: <strong>{mission['hunter']}</strong></div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div style="text-align: center; margin-top: 3rem; padding: 2rem; border-top: 1px solid rgba(255,255,255,0.1); color: rgba(255,255,255,0.7);">
    <div style="font-weight: 600; margin-bottom: 0.5rem;">
        🔍 Threat Hunting Dashboard | Last Updated: <span class="timestamp-live">{current_time.strftime('%Y-%m-%d %H:%M:%S')}</span>
    </div>
    <div style="font-size: 0.85rem;">
        {len(missions_df)} Active Hunts | {len(alerts_df)} Alerts Processed | {len(social_media_df)} Social Threats Monitored
    </div>
</div>
""", unsafe_allow_html=True)

# Auto-refresh logic
if auto_refresh:
    import time
    time.sleep(refresh_interval)
    st.rerun()
