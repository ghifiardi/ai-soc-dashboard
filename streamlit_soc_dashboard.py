#!/usr/bin/env python3
"""
🧠 Enhanced AI-Driven SOC Dashboard
Next-Generation Security Operations with Autonomous Response Capabilities
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import asyncio
import json
import time
from typing import Dict, Any
import uuid

# Configure Streamlit page
st.set_page_config(
    page_title="🧠 AI-SOC Command Center",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS for modern dark theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    }
    
    .telemetry-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        backdrop-filter: blur(10px);
        border: 1px solid rgba(102, 126, 234, 0.3);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        transition: transform 0.3s ease;
    }
    
    .telemetry-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.3);
    }
    
    .risk-low {
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.1), rgba(76, 175, 80, 0.05));
        border: 1px solid rgba(76, 175, 80, 0.3);
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .risk-medium {
        background: linear-gradient(135deg, rgba(255, 193, 7, 0.1), rgba(255, 193, 7, 0.05));
        border: 1px solid rgba(255, 193, 7, 0.3);
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .risk-high {
        background: linear-gradient(135deg, rgba(244, 67, 54, 0.1), rgba(244, 67, 54, 0.05));
        border: 1px solid rgba(244, 67, 54, 0.3);
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem 0;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(244, 67, 54, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(244, 67, 54, 0); }
        100% { box-shadow: 0 0 0 0 rgba(244, 67, 54, 0); }
    }
    
    .live-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        background: #4caf50;
        border-radius: 50%;
        animation: blink 1s infinite;
        margin-right: 5px;
    }
    
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.3; }
    }
    
    .metric-highlight {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.2));
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .patch-status {
        background: rgba(33, 150, 243, 0.1);
        border: 1px solid rgba(33, 150, 243, 0.3);
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .compliance-card {
        background: linear-gradient(135deg, rgba(156, 39, 176, 0.1), rgba(156, 39, 176, 0.05));
        border: 1px solid rgba(156, 39, 176, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
    }
    
    .stMetric {
        background: rgba(255, 255, 255, 0.05);
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    div[data-testid="stMarkdownContainer"] p {
        color: var(--text-color) !important;
    }
</style>
""", unsafe_allow_html=True)


class EnhancedSOCDashboard:
    """Enhanced SOC Dashboard with autonomous capabilities"""
    
    def __init__(self):
        self.initialize_state()
        self.setup_mock_data()
        
    def initialize_state(self):
        """Initialize session state"""
        if 'telemetry_events' not in st.session_state:
            st.session_state.telemetry_events = []
        if 'risk_decisions' not in st.session_state:
            st.session_state.risk_decisions = []
        if 'patch_queue' not in st.session_state:
            st.session_state.patch_queue = []
        if 'compliance_score' not in st.session_state:
            st.session_state.compliance_score = 94.5
            
    def setup_mock_data(self):
        """Setup mock data generators"""
        self.threat_narratives = [
            "Potential APT activity detected: Multiple reconnaissance attempts followed by lateral movement",
            "Ransomware precursor behavior: Unusual encryption library calls detected",
            "Data exfiltration attempt: Large volume transfer to unknown external IP",
            "Privilege escalation detected: Service account attempting admin operations",
            "Supply chain attack indicator: Compromised package detected in build pipeline"
        ]
        
        self.mitre_techniques = [
            "T1595 - Active Scanning",
            "T1190 - Exploit Public-Facing Application", 
            "T1055 - Process Injection",
            "T1003 - OS Credential Dumping",
            "T1486 - Data Encrypted for Impact"
        ]
    
    def generate_telemetry_event(self) -> Dict[str, Any]:
        """Generate realistic telemetry event"""
        event_types = ['network', 'endpoint', 'authentication', 'application', 'cloud']
        severity_levels = ['low', 'medium', 'high', 'critical']
        
        event = {
            'id': str(uuid.uuid4())[:8],
            'timestamp': datetime.now(),
            'type': np.random.choice(event_types),
            'severity': np.random.choice(severity_levels, p=[0.6, 0.25, 0.12, 0.03]),
            'source_ip': f"192.168.{np.random.randint(1, 255)}.{np.random.randint(1, 255)}",
            'destination_ip': f"10.0.{np.random.randint(1, 255)}.{np.random.randint(1, 255)}",
            'cisa_validated': np.random.choice([True, False], p=[0.97, 0.03]),
            'confidence_score': np.random.uniform(0.3, 0.99),
            'mitre_technique': np.random.choice(self.mitre_techniques),
            'asset_criticality': np.random.choice(['low', 'medium', 'high', 'critical'], p=[0.3, 0.4, 0.25, 0.05]),
            'risk_score': np.random.uniform(0, 100)
        }
        return event
    
    def calculate_risk_decision(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """AI-driven risk decision logic"""
        risk_score = event['risk_score']
        
        if risk_score < 30:
            decision = 'AUTO_REMEDIATE'
            action = 'Isolating endpoint and blocking IoCs'
            status = 'COMPLETED'
            color = 'risk-low'
        elif 30 <= risk_score < 70:
            decision = 'ANALYST_APPROVAL'
            action = 'Queued for analyst review'
            status = 'PENDING'
            color = 'risk-medium'
        else:
            decision = 'ESCALATE_IR'
            action = 'Escalated to incident response team'
            status = 'CRITICAL'
            color = 'risk-high'
        
        return {
            'event_id': event['id'],
            'timestamp': datetime.now(),
            'risk_score': risk_score,
            'decision': decision,
            'action': action,
            'status': status,
            'color': color,
            'remediation_time': np.random.randint(5, 300) if decision == 'AUTO_REMEDIATE' else None
        }
    
    def generate_patch_status(self) -> Dict[str, Any]:
        """Generate patch management status"""
        return {
            'vulnerability_id': f"CVE-2025-{np.random.randint(1000, 9999)}",
            'severity': np.random.choice(['low', 'medium', 'high', 'critical'], p=[0.2, 0.3, 0.35, 0.15]),
            'affected_systems': np.random.randint(1, 50),
            'patch_available': np.random.choice([True, False], p=[0.85, 0.15]),
            'auto_patch_eligible': np.random.choice([True, False], p=[0.7, 0.3]),
            'deployment_status': np.random.choice(['pending', 'testing', 'deploying', 'completed'], p=[0.2, 0.2, 0.1, 0.5]),
            'deployment_time': f"{np.random.randint(1, 30)} min"
        }
    
    def render_header(self):
        """Render main header"""
        st.markdown("""
        <div class="main-header">
            <h1>🧠 AI-SOC Command Center</h1>
            <p>Autonomous Security Operations powered by Advanced AI Agents</p>
            <p style="font-size: 0.9rem; opacity: 0.9;">
                <span class="live-indicator"></span> LIVE • 
                Telemetry: ACTIVE • CISA Model: ONLINE • Risk Engine: OPERATIONAL
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    def render_telemetry_ingestion(self):
        """Render telemetry ingestion section"""
        st.header("📡 Telemetry Ingestion & Validation")
        
        # Real-time metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            events_per_sec = np.random.randint(7000, 12000)
            st.metric("Events/sec", f"{events_per_sec:,}", f"↑ {np.random.randint(5, 15)}%")
        
        with col2:
            validation_rate = 99.7 + np.random.uniform(-0.5, 0.3)
            st.metric("CISA Validation", f"{validation_rate:.1f}%", f"↑ {np.random.uniform(0.1, 0.5):.1f}%")
        
        with col3:
            st.metric("IoC Matches", np.random.randint(15, 35), f"↑ {np.random.randint(1, 8)}")
        
        with col4:
            st.metric("Quarantined", np.random.randint(3, 12), f"↓ {np.random.randint(1, 5)}")
        
        with col5:
            st.metric("False Positives", f"{np.random.uniform(0.5, 2.5):.1f}%", "↓ 0.3%")
        
        # Live telemetry stream
        st.subheader("🔴 Live Telemetry Stream")
        
        telemetry_container = st.container()
        with telemetry_container:
            # Generate and display recent events
            for _ in range(3):
                event = self.generate_telemetry_event()
                
                severity_emoji = {
                    'low': '🟢',
                    'medium': '🟡', 
                    'high': '🟠',
                    'critical': '🔴'
                }
                
                validation_status = "✅ CISA Validated" if event['cisa_validated'] else "⚠️ Validation Failed"
                
                st.markdown(f"""
                <div class="telemetry-card">
                    <strong>{severity_emoji[event['severity']]} Event ID: {event['id']}</strong><br>
                    <strong>Type:</strong> {event['type'].upper()} | 
                    <strong>Severity:</strong> {event['severity'].upper()}<br>
                    <strong>Source:</strong> {event['source_ip']} → {event['destination_ip']}<br>
                    <strong>MITRE:</strong> {event['mitre_technique']}<br>
                    <strong>Confidence:</strong> {event['confidence_score']:.1%} | 
                    <strong>Status:</strong> {validation_status}
                </div>
                """, unsafe_allow_html=True)
    
    def render_ai_enrichment(self):
        """Render AI enrichment section"""
        st.header("🤖 AI Enrichment & Correlation Engine")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 MITRE ATT&CK Mapping")
            
            # MITRE techniques distribution
            techniques_data = {
                'Technique': ['Reconnaissance', 'Initial Access', 'Execution', 'Persistence', 'Privilege Escalation'],
                'Count': [45, 23, 67, 34, 12],
                'Severity': ['Medium', 'High', 'Critical', 'High', 'Critical']
            }
            
            fig = px.bar(techniques_data, x='Technique', y='Count', color='Severity',
                        color_discrete_map={'Medium': '#FFA726', 'High': '#FF7043', 'Critical': '#E53935'})
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                height=300
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("🎯 Asset Risk Scoring")
            
            # Asset risk heatmap
            assets = ['Web Servers', 'Database', 'Workstations', 'Network Devices', 'Cloud Resources']
            risk_scores = np.random.uniform(20, 95, len(assets))
            
            fig = go.Figure(data=go.Heatmap(
                z=[risk_scores],
                x=assets,
                y=['Risk Score'],
                colorscale='RdYlGn_r',
                text=[[f"{score:.1f}" for score in risk_scores]],
                texttemplate="%{text}",
                textfont={"size": 12}
            ))
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                height=300
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Threat Narrative
        st.subheader("📝 AI-Generated Threat Narrative")
        narrative = np.random.choice(self.threat_narratives)
        st.markdown(f"""
        <div class="metric-highlight">
            <h4>🔍 Current Threat Analysis</h4>
            <p>{narrative}</p>
            <p><strong>Recommended Actions:</strong></p>
            <ul>
                <li>Immediate: Isolate affected endpoints</li>
                <li>Short-term: Deploy detection signatures</li>
                <li>Long-term: Review security architecture</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    def render_risk_decision_engine(self):
        """Render risk decision engine"""
        st.header("⚖️ Autonomous Risk Decision Engine")
        
        # Generate sample decisions
        decisions = []
        for _ in range(5):
            event = self.generate_telemetry_event()
            decision = self.calculate_risk_decision(event)
            decisions.append(decision)
        
        # Decision metrics
        col1, col2, col3, col4 = st.columns(4)
        
        auto_remediated = sum(1 for d in decisions if d['decision'] == 'AUTO_REMEDIATE')
        analyst_review = sum(1 for d in decisions if d['decision'] == 'ANALYST_APPROVAL')
        escalated = sum(1 for d in decisions if d['decision'] == 'ESCALATE_IR')
        
        with col1:
            st.metric("Total Decisions", len(decisions))
        with col2:
            st.metric("Auto-Remediated", auto_remediated, "🟢")
        with col3:
            st.metric("Analyst Review", analyst_review, "🟡")
        with col4:
            st.metric("Escalated", escalated, "🔴")
        
        # Decision flow visualization
        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=["Incoming Events", "Low Risk", "Medium Risk", "High Risk",
                       "Auto-Remediate", "Analyst Review", "Escalate to IR"],
                color=["blue", "green", "yellow", "red", "green", "yellow", "red"]
            ),
            link=dict(
                source=[0, 0, 0, 1, 2, 3],
                target=[1, 2, 3, 4, 5, 6],
                value=[auto_remediated, analyst_review, escalated, 
                       auto_remediated, analyst_review, escalated]
            )
        )])
        
        fig.update_layout(
            title="Risk-Based Decision Flow",
            font_size=10,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Recent decisions
        st.subheader("📋 Recent Risk Decisions")
        for decision in decisions[:3]:
            st.markdown(f"""
            <div class="{decision['color']}">
                <strong>Event: {decision['event_id']}</strong> | Risk Score: {decision['risk_score']:.1f}<br>
                <strong>Decision:</strong> {decision['decision']}<br>
                <strong>Action:</strong> {decision['action']}<br>
                <strong>Status:</strong> {decision['status']}
                {f" | Remediation Time: {decision['remediation_time']}s" if decision['remediation_time'] else ""}
            </div>
            """, unsafe_allow_html=True)
    
    def render_patch_management(self):
        """Render autonomous patch management"""
        st.header("🔧 Autonomous Patch Management")
        
        # Patch metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Vulnerabilities", np.random.randint(30, 60))
        with col2:
            st.metric("Patches Available", np.random.randint(25, 55))
        with col3:
            st.metric("Auto-Deployed", np.random.randint(20, 45))
        with col4:
            st.metric("Success Rate", f"{np.random.uniform(94, 99):.1f}%")
        
        # Patch status
        st.subheader("🔄 Active Patch Deployments")
        
        for _ in range(3):
            patch = self.generate_patch_status()
            
            severity_color = {
                'low': '🟢',
                'medium': '🟡',
                'high': '🟠',
                'critical': '🔴'
            }
            
            st.markdown(f"""
            <div class="patch-status">
                <strong>{severity_color[patch['severity']]} {patch['vulnerability_id']}</strong><br>
                <strong>Severity:</strong> {patch['severity'].upper()} | 
                <strong>Affected Systems:</strong> {patch['affected_systems']}<br>
                <strong>Patch Available:</strong> {'✅ Yes' if patch['patch_available'] else '❌ No'} | 
                <strong>Auto-Deploy:</strong> {'✅ Eligible' if patch['auto_patch_eligible'] else '⚠️ Manual Required'}<br>
                <strong>Status:</strong> {patch['deployment_status'].upper()} | 
                <strong>Est. Time:</strong> {patch['deployment_time']}
            </div>
            """, unsafe_allow_html=True)
    
    def render_compliance_reporting(self):
        """Render compliance reporting"""
        st.header("📊 Governance & Compliance Reporting")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            frameworks = ['SOC 2', 'ISO 27001', 'NIST', 'GDPR', 'HIPAA']
            scores = [94.5, 92.3, 96.1, 89.7, 91.2]
            
            fig = go.Figure(data=[
                go.Bar(x=frameworks, y=scores, 
                      marker_color=['green' if s >= 90 else 'orange' for s in scores])
            ])
            fig.update_layout(
                title="Compliance Framework Scores",
                yaxis_title="Compliance %",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="compliance-card">
                <h4>📋 Latest Compliance Report</h4>
                <p><strong>Generated:</strong> 2 hours ago</p>
                <p><strong>Period:</strong> Q1 2025</p>
                <p><strong>Overall Score:</strong> 93.2%</p>
                <p><strong>Critical Gaps:</strong> 2</p>
                <p><strong>Recommendations:</strong> 8</p>
                <br>
                <p>✅ SOC 2 Type II Ready</p>
                <p>✅ ISO 27001 Compliant</p>
                <p>⚠️ GDPR Review Needed</p>
            </div>
            """, unsafe_allow_html=True)
    
    def render_system_health(self):
        """Render system health dashboard"""
        st.header("⚙️ System Health & Performance")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("CPU Usage", f"{np.random.randint(20, 45)}%")
            st.metric("Memory", f"{np.random.randint(50, 75)}%")
        
        with col2:
            st.metric("Network I/O", f"{np.random.randint(100, 500)} MB/s")
            st.metric("Disk Usage", f"{np.random.randint(40, 60)}%")
        
        with col3:
            st.metric("Agent Status", "All Online", "✅")
            st.metric("Model Accuracy", f"{np.random.uniform(94, 98):.1f}%")
        
        with col4:
            st.metric("Uptime", "99.99%")
            st.metric("Latency", f"{np.random.randint(50, 150)}ms")


def main():
    # Initialize dashboard
    dashboard = EnhancedSOCDashboard()
    
    # Render header
    dashboard.render_header()
    
    # Sidebar navigation
    st.sidebar.title("🛡️ SOC Command Center")
    
    sections = st.sidebar.multiselect(
        "Select Dashboard Sections",
        ["📡 Telemetry Ingestion", "🤖 AI Enrichment", "⚖️ Risk Decisions", 
         "🔧 Patch Management", "📊 Compliance", "⚙️ System Health"],
        default=["📡 Telemetry Ingestion", "🤖 AI Enrichment", "⚖️ Risk Decisions"]
    )
    
    # Auto-refresh
    auto_refresh = st.sidebar.checkbox("🔄 Auto-refresh (10s)", value=True)
    
    if st.sidebar.button("🚨 Simulate Critical Event"):
        st.sidebar.error("Critical threat detected! Check Risk Decisions panel.")
    
    # Render selected sections
    if "📡 Telemetry Ingestion" in sections:
        dashboard.render_telemetry_ingestion()
        st.markdown("---")
    
    if "🤖 AI Enrichment" in sections:
        dashboard.render_ai_enrichment()
        st.markdown("---")
    
    if "⚖️ Risk Decisions" in sections:
        dashboard.render_risk_decision_engine()
        st.markdown("---")
    
    if "🔧 Patch Management" in sections:
        dashboard.render_patch_management()
        st.markdown("---")
    
    if "📊 Compliance" in sections:
        dashboard.render_compliance_reporting()
        st.markdown("---")
    
    if "⚙️ System Health" in sections:
        dashboard.render_system_health()
    
    # Auto-refresh logic
    if auto_refresh:
        time.sleep(10)
        st.rerun()


if __name__ == "__main__":
    main()


