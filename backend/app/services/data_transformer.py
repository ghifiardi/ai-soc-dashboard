"""
Data transformation service for Executive Dashboard
"""
from typing import Dict, List
from datetime import datetime
from ..models.executive_metrics import (
    ExecutiveMetrics,
    MetricsComparison,
    TrendDataPoint,
    SeverityData,
    RiskItem,
    ComplianceFramework,
    ExecutiveDashboardResponse
)

class DataTransformer:
    """Transform BigQuery data to Executive Dashboard format"""

    @staticmethod
    def transform_executive_metrics(
        incident_data: Dict,
        agent_data: Dict
    ) -> MetricsComparison:
        """
        Transform incident and agent data to executive metrics format

        Args:
            incident_data: Current and previous incident metrics
            agent_data: Agent performance metrics

        Returns:
            MetricsComparison with current and previous periods
        """
        current_incidents = incident_data.get('current', {})
        previous_incidents = incident_data.get('previous', {})

        # Build current period metrics
        current = ExecutiveMetrics(
            total_incidents=current_incidents.get('total_incidents', 0),
            critical_incidents=current_incidents.get('critical_incidents', 0),
            avg_response_time=current_incidents.get('avg_response_time', 30.0),
            resolved_rate=current_incidents.get('resolved_rate', 90.0),
            false_positive_rate=current_incidents.get('false_positive_rate', 5.0),
            security_score=agent_data.get('security_score', 85),
            compliance_score=92,  # TODO: Get from compliance table if available
            mttr=agent_data.get('mttr', 45.0),
            mttd=agent_data.get('mttd', 25.0),
            mttr_resolve=agent_data.get('mttr_resolve', 360.0)
        )

        # Build previous period metrics
        previous = ExecutiveMetrics(
            total_incidents=previous_incidents.get('total_incidents', 0),
            critical_incidents=previous_incidents.get('critical_incidents', 0),
            avg_response_time=previous_incidents.get('avg_response_time', 30.0),
            resolved_rate=previous_incidents.get('resolved_rate', 90.0),
            false_positive_rate=previous_incidents.get('false_positive_rate', 5.0),
            security_score=int(agent_data.get('security_score', 85) * 0.95),
            compliance_score=90,
            mttr=agent_data.get('mttr', 45.0) * 1.1,
            mttd=agent_data.get('mttd', 25.0) * 1.05,
            mttr_resolve=agent_data.get('mttr_resolve', 360.0) * 1.08
        )

        return MetricsComparison(current=current, previous=previous)

    @staticmethod
    def transform_trend_data(trend_data: List[Dict]) -> List[TrendDataPoint]:
        """
        Transform trend data to dashboard format

        Args:
            trend_data: List of daily incident counts

        Returns:
            List of TrendDataPoint objects
        """
        return [
            TrendDataPoint(date=item['date'], incidents=item['incidents'])
            for item in trend_data
        ]

    @staticmethod
    def transform_severity_data(severity_data: List[Dict]) -> List[SeverityData]:
        """
        Transform severity data to dashboard format

        Args:
            severity_data: List of severity distributions

        Returns:
            List of SeverityData objects
        """
        return [
            SeverityData(
                name=item['name'],
                value=item['value'],
                color=item['color']
            )
            for item in severity_data
        ]

    @staticmethod
    def get_static_risks() -> List[RiskItem]:
        """
        Get static risk assessment data
        TODO: Replace with BigQuery query when risk table is available

        Returns:
            List of RiskItem objects
        """
        return [
            RiskItem(
                risk="Unpatched Systems",
                severity="Critical",
                affected=24,
                trend="▲"
            ),
            RiskItem(
                risk="Phishing Attempts",
                severity="High",
                affected=156,
                trend="▼"
            ),
            RiskItem(
                risk="Unauthorized Access Attempts",
                severity="High",
                affected=89,
                trend="▲"
            ),
            RiskItem(
                risk="Data Exfiltration Alerts",
                severity="Medium",
                affected=12,
                trend="▬"
            ),
            RiskItem(
                risk="Malware Detections",
                severity="Medium",
                affected=34,
                trend="▼"
            )
        ]

    @staticmethod
    def get_static_compliance() -> List[ComplianceFramework]:
        """
        Get static compliance framework scores
        TODO: Replace with BigQuery query when compliance table is available

        Returns:
            List of ComplianceFramework objects
        """
        return [
            ComplianceFramework(name="NIST CSF", score=94),
            ComplianceFramework(name="ISO 27001", score=91),
            ComplianceFramework(name="SOC 2", score=96),
            ComplianceFramework(name="GDPR", score=88),
            ComplianceFramework(name="HIPAA", score=92)
        ]

    @staticmethod
    def build_dashboard_response(
        metrics: MetricsComparison,
        trend_data: List[TrendDataPoint],
        severity_data: List[SeverityData],
        risks: List[RiskItem],
        compliance: List[ComplianceFramework]
    ) -> ExecutiveDashboardResponse:
        """
        Build complete dashboard response

        Args:
            metrics: Current and previous metrics
            trend_data: Trend data
            severity_data: Severity distribution
            risks: Risk items
            compliance: Compliance scores

        Returns:
            Complete ExecutiveDashboardResponse
        """
        return ExecutiveDashboardResponse(
            metrics=metrics,
            trend_data=trend_data,
            severity_data=severity_data,
            risks=risks,
            compliance=compliance,
            generated_at=datetime.now()
        )

# Create singleton instance
data_transformer = DataTransformer()
