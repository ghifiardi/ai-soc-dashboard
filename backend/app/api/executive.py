"""
API endpoints for Executive Dashboard
"""
from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from datetime import datetime
from ..models.executive_metrics import ExecutiveDashboardResponse
from ..services.bigquery_service import bigquery_service
from ..services.data_transformer import data_transformer

router = APIRouter(prefix="/api/executive", tags=["Executive Dashboard"])

@router.get("/dashboard", response_model=ExecutiveDashboardResponse)
async def get_executive_dashboard(
    days: Optional[int] = Query(default=30, ge=1, le=365, description="Number of days to analyze")
):
    """
    Get complete executive dashboard data

    Args:
        days: Number of days to look back (default: 30)

    Returns:
        Complete executive dashboard metrics and visualizations
    """
    try:
        # Fetch data from BigQuery
        incident_data = bigquery_service.get_incident_metrics(days=days)
        agent_data = bigquery_service.get_agent_metrics()
        trend_data_raw = bigquery_service.get_trend_data(days=days)
        severity_data_raw = bigquery_service.get_severity_distribution(days=days)

        # Transform data
        metrics = data_transformer.transform_executive_metrics(
            incident_data=incident_data,
            agent_data=agent_data
        )
        trend_data = data_transformer.transform_trend_data(trend_data_raw)
        severity_data = data_transformer.transform_severity_data(severity_data_raw)
        risks = data_transformer.get_static_risks()
        compliance = data_transformer.get_static_compliance()

        # Build response
        dashboard_response = data_transformer.build_dashboard_response(
            metrics=metrics,
            trend_data=trend_data,
            severity_data=severity_data,
            risks=risks,
            compliance=compliance
        )

        return dashboard_response

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching executive dashboard data: {str(e)}"
        )

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Executive Dashboard API",
        "timestamp": str(datetime.now())
    }
