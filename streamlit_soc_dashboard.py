#!/usr/bin/env python3
"""
AI-SOC Command Center (Enhanced Streamlit Dashboard)
- Mock telemetry with optional BigQuery live feed
- Robust error display to avoid blank/empty pages
"""

from typing import Any, Dict, List
from datetime import datetime
import importlib
import time
import uuid

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# Page setup and visible diagnostics
st.set_page_config(page_title="🧠 AI-SOC Command Center", page_icon="🛡️", layout="wide")
st.set_option("client.showErrorDetails", True)
st.caption(f"App initialized at {datetime.utcnow().isoformat()}Z")

# Simple styling
st.markdown(
    """
<style>
  .main-header { background: linear-gradient(135deg,#667eea,#764ba2); padding: 1.25rem; border-radius: 12px; color: #fff; text-align:center; margin: 1rem 0 1.25rem; }
  .telemetry-card { border: 1px solid rgba(102,126,234,.35); border-radius: 10px; padding: .9rem; margin: .5rem 0; background: rgba(102,126,234,.06); }
  .metric-highlight { background: rgba(118,75,162,.08); padding: 1rem; border-left: 4px solid #667eea; border-radius: 8px; }
  .patch-status { background: rgba(33,150,243,.1); border: 1px solid rgba(33,150,243,.3); border-radius: 8px; padding: .9rem; margin: .5rem 0; }
</style>
""",
    unsafe_allow_html=True,
)


def secret_get(key: str, default: Any = None) -> Any:
    try:
        if hasattr(st, "secrets") and key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass
    return default


class Dashboard:
    def __init__(self) -> None:
        self.data_source: str = "Mock"
        self.bigquery_cfg: Dict[str, Any] = {
            "project": None,
            "dataset": None,
            "table": None,
            "window_minutes": 5,
            "limit": 20,
        }
        self._bq_mod = None
        self.bq_client = None
        self.bq_available = False
        self._setup_bigquery()

    # BigQuery setup (optional)
    def _setup_bigquery(self) -> None:
        try:
            self._bq_mod = importlib.import_module("google.cloud.bigquery")
        except Exception:
            self._bq_mod = None
            return
        try:
            creds = secret_get("bigquery_credentials")
            if creds:
                self.bq_client = self._bq_mod.Client.from_service_account_info(creds)
            else:
                project = secret_get("bq_project")
                self.bq_client = self._bq_mod.Client(project=project)
            self.bq_available = True
        except Exception:
            self.bq_client = None
            self.bq_available = False

    def _default_table_sql(self) -> str:
        project = self.bigquery_cfg.get("project") or secret_get("bq_project") or "chronicle-dev-2be9"
        dataset = self.bigquery_cfg.get("dataset") or secret_get("bq_dataset") or "soc_data"
        table = self.bigquery_cfg.get("table") or secret_get("bq_table") or "processed_alerts"
        return f"`{project}.{dataset}.{table}`"

    def fetch_bq_events(self) -> List[Dict[str, Any]]:
        if not (self.bq_available and self.bq_client and self._bq_mod):
            return []
        table_sql = self._default_table_sql()
        minutes = int(self.bigquery_cfg.get("window_minutes", 5))
        limit = int(self.bigquery_cfg.get("limit", 20))
        query = f"""
            SELECT * FROM {table_sql}
            WHERE timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL {minutes} MINUTE)
            ORDER BY timestamp DESC
            LIMIT {limit}
        """
        try:
            df = self.bq_client.query(query).to_dataframe()
        except Exception:
            return []
        events: List[Dict[str, Any]] = []
        for _, row in df.iterrows():
            rd = row.to_dict()
            events.append(
                {
                    "id": rd.get("alert_id") or rd.get("id") or str(uuid.uuid4())[:8],
                    "timestamp": rd.get("timestamp") or datetime.utcnow(),
                    "type": rd.get("classification") or rd.get("type") or "network",
                    "severity": self._infer_severity(rd.get("classification"), rd.get("confidence_score")),
                    "source_ip": rd.get("source_ip", "N/A"),
                    "destination_ip": rd.get("destination_ip", "N/A"),
                    "mitre_technique": rd.get("mitre_technique", "N/A"),
                    "confidence_score": float(rd.get("confidence_score")) if rd.get("confidence_score") is not None else float(np.random.uniform(0.4, 0.95)),
                    "cisa_validated": bool(rd.get("cisa_validated")) if "cisa_validated" in rd else None,
                    "classification": rd.get("classification"),
                }
            )
        return events

    @staticmethod
    def _infer_severity(classification: Any, confidence: Any) -> str:
        try:
            conf = float(confidence) if confidence is not None else 0.5
        except Exception:
            conf = 0.5
        if classification in ("anomaly", "critical", "high") or conf >= 0.85:
            return "high"
        if classification in ("benign", "low") or conf < 0.5:
            return "low"
        return "medium"

    # Generators
    def generate_event(self) -> Dict[str, Any]:
        event_types = ["network", "endpoint", "authentication", "application", "cloud"]
        severity = ["low", "medium", "high", "critical"]
        return {
            "id": str(uuid.uuid4())[:8],
            "timestamp": datetime.utcnow(),
            "type": np.random.choice(event_types),
            "severity": np.random.choice(severity, p=[0.6, 0.25, 0.12, 0.03]),
            "source_ip": f"192.168.{np.random.randint(1,255)}.{np.random.randint(1,255)}",
            "destination_ip": f"10.0.{np.random.randint(1,255)}.{np.random.randint(1,255)}",
            "cisa_validated": np.random.choice([True, False], p=[0.97, 0.03]),
            "confidence_score": float(np.random.uniform(0.3, 0.99)),
            "mitre_technique": np.random.choice([
                "T1595 - Active Scanning",
                "T1190 - Exploit Public-Facing Application",
                "T1055 - Process Injection",
                "T1003 - OS Credential Dumping",
                "T1486 - Data Encrypted for Impact",
            ]),
            "risk_score": float(np.random.uniform(0, 100)),
            "classification": np.random.choice(["anomaly", "benign", "suspicious"], p=[0.25, 0.6, 0.15]),
        }

    # Renderers
    def render_header(self) -> None:
        st.markdown(
            """
        <div class="main-header">
          <h2>🧠 AI-SOC Command Center</h2>
          <p>Autonomous Security Operations powered by Advanced AI Agents</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    def render_telemetry(self) -> None:
        st.header("📡 Telemetry Ingestion & Validation")
        if self.data_source == "BigQuery" and self.bq_available:
            events = self.fetch_bq_events()
            window_minutes = int(self.bigquery_cfg.get("window_minutes", 5))
        else:
            events = [self.generate_event() for _ in range(10)]
            window_minutes = 1

        total = len(events)
        eps = total / max(window_minutes * 60, 1)
        cisa_vals = [e.get("cisa_validated") for e in events if e.get("cisa_validated") is not None]
        cisa_rate = (sum(1 for v in cisa_vals if v) / len(cisa_vals) * 100) if cisa_vals else None
        ioc_matches = sum(1 for e in events if e.get("classification") == "anomaly")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Events/sec", f"{eps:,.2f}")
        with c2:
            st.metric("CISA Validation", f"{cisa_rate:.1f}%" if cisa_rate is not None else "—")
        with c3:
            st.metric("IoC Matches", f"{ioc_matches:,}")

        st.subheader("🔴 Live Telemetry Stream")
        sev_icon = {"low": "🟢", "medium": "🟡", "high": "🟠", "critical": "🔴"}
        for e in events[:3]:
            sev = e.get("severity") or self._infer_severity(e.get("classification"), e.get("confidence_score"))
            val_status = (
                "✅ CISA Validated" if e.get("cisa_validated") else ("⚠️ Validation Failed" if e.get("cisa_validated") is False else "—")
            )
            st.markdown(
                f"""
            <div class="telemetry-card">
              <strong>{sev_icon.get(sev,'🟡')} Event ID:</strong> {e.get('id')}<br>
              <strong>Type:</strong> {str(e.get('type','N/A')).upper()} | <strong>Severity:</strong> {str(sev).upper()}<br>
              <strong>Source:</strong> {e.get('source_ip','N/A')} → {e.get('destination_ip','N/A')}<br>
              <strong>MITRE:</strong> {e.get('mitre_technique','N/A')}<br>
              <strong>Confidence:</strong> {float(e.get('confidence_score',0.0)):.1%} | <strong>Status:</strong> {val_status}
            </div>
            """,
                unsafe_allow_html=True,
            )

    def render_enrichment(self) -> None:
        st.header("🤖 AI Enrichment & Correlation")
        data = {
            "Technique": ["Recon", "Initial Access", "Execution", "Persistence", "Priv Esc"],
            "Count": [45, 23, 67, 34, 12],
            "Severity": ["Medium", "High", "Critical", "High", "Critical"],
        }
        fig = px.bar(data, x="Technique", y="Count", color="Severity")
        st.plotly_chart(fig, use_container_width=True)

    def render_system(self) -> None:
        st.header("⚙️ System Health & Performance")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("CPU Usage", f"{np.random.randint(20,45)}%")
        with c2:
            st.metric("Memory", f"{np.random.randint(50,75)}%")
        with c3:
            st.metric("Uptime", "99.99%")
        with c4:
            st.metric("Latency", f"{np.random.randint(50,150)}ms")


def main() -> None:
    dash = Dashboard()
    dash.render_header()

    st.sidebar.title("🛡️ SOC Command Center")
    source = st.sidebar.radio("Telemetry Source", ["Mock", "BigQuery"], horizontal=True)
    dash.data_source = source
    if source == "BigQuery":
        with st.sidebar.expander("BigQuery Settings", expanded=False):
            project = st.text_input("GCP Project", value=secret_get("bq_project", "chronicle-dev-2be9"))
            dataset = st.text_input("Dataset", value=secret_get("bq_dataset", "soc_data"))
            table = st.text_input("Table", value=secret_get("bq_table", "processed_alerts"))
            window = st.slider("Time Window (minutes)", 1, 120, 5)
            limit = st.slider("Max Events", 5, 200, 20)
        dash.bigquery_cfg.update({"project": project, "dataset": dataset, "table": table, "window_minutes": window, "limit": limit})

    sections = st.sidebar.multiselect(
        "Select Dashboard Sections",
        ["📡 Telemetry", "🤖 Enrichment", "⚙️ System"],
        default=["📡 Telemetry", "🤖 Enrichment"],
    )
    auto_refresh = st.sidebar.checkbox("🔄 Auto-refresh (10s)", value=True)

    if "📡 Telemetry" in sections:
        try:
            dash.render_telemetry()
        except Exception as e:
            st.error("Telemetry section error")
            st.exception(e)
        st.markdown("---")

    if "🤖 Enrichment" in sections:
        try:
            dash.render_enrichment()
        except Exception as e:
            st.error("Enrichment section error")
            st.exception(e)
        st.markdown("---")

    if "⚙️ System" in sections:
        try:
            dash.render_system()
        except Exception as e:
            st.error("System section error")
            st.exception(e)

    if auto_refresh:
        time.sleep(10)
        st.rerun()


try:
    main()
except Exception as e:
    st.error("App failed to start")
    st.exception(e)


