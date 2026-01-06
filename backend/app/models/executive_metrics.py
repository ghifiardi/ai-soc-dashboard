"""
Pydantic models for Executive Dashboard data
"""
from typing import List, Dict, Optional
from pydantic import BaseModel
from datetime import datetime

class ExecutiveMetrics(BaseModel):
    """Executive-level KPI metrics"""
    total_incidents: int
    critical_incidents: int
    avg_response_time: float
    resolved_rate: float
    false_positive_rate: float
    security_score: int
    compliance_score: int
    mttr: float  # Mean Time To Respond (minutes)
    mttd: float  # Mean Time To Detect (minutes)
    mttr_resolve: float  # Mean Time To Resolve (minutes)

class MetricsComparison(BaseModel):
    """Current vs previous period metrics"""
    current: ExecutiveMetrics
    previous: ExecutiveMetrics

class TrendDataPoint(BaseModel):
    """Single data point for trend charts"""
    date: str
    incidents: int

class SeverityData(BaseModel):
    """Severity distribution data"""
    name: str
    value: int
    color: str

class RiskItem(BaseModel):
    """Security risk item"""
    risk: str
    severity: str
    affected: int
    trend: str

class ComplianceFramework(BaseModel):
    """Compliance framework score"""
    name: str
    score: int

class ExecutiveDashboardResponse(BaseModel):
    """Complete executive dashboard data"""
    metrics: MetricsComparison
    trend_data: List[TrendDataPoint]
    severity_data: List[SeverityData]
    risks: List[RiskItem]
    compliance: List[ComplianceFramework]
    generated_at: datetime
