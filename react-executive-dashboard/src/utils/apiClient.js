/**
 * API client for fetching data from FastAPI backend
 */

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

export const fetchExecutiveDashboard = async (days = 30) => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/executive/dashboard?days=${days}`);

    if (!response.ok) {
      throw new Error(`API Error: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();
    return transformAPIResponse(data);
  } catch (error) {
    console.error('Error fetching dashboard data:', error);
    // Return null to trigger fallback to mock data
    return null;
  }
};

/**
 * Transform API response to match the format expected by React components
 */
const transformAPIResponse = (apiData) => {
  return {
    metrics: {
      current: {
        totalIncidents: apiData.metrics.current.total_incidents,
        criticalIncidents: apiData.metrics.current.critical_incidents,
        avgResponseTime: apiData.metrics.current.avg_response_time,
        resolvedRate: apiData.metrics.current.resolved_rate,
        falsePositiveRate: apiData.metrics.current.false_positive_rate,
        securityScore: apiData.metrics.current.security_score,
        complianceScore: apiData.metrics.current.compliance_score,
        mttr: apiData.metrics.current.mttr,
        mttd: apiData.metrics.current.mttd,
        mttrResolve: apiData.metrics.current.mttr_resolve,
      },
      previous: {
        totalIncidents: apiData.metrics.previous.total_incidents,
        criticalIncidents: apiData.metrics.previous.critical_incidents,
        avgResponseTime: apiData.metrics.previous.avg_response_time,
        resolvedRate: apiData.metrics.previous.resolved_rate,
        falsePositiveRate: apiData.metrics.previous.false_positive_rate,
        securityScore: apiData.metrics.previous.security_score,
        complianceScore: apiData.metrics.previous.compliance_score,
        mttr: apiData.metrics.previous.mttr,
        mttd: apiData.metrics.previous.mttd,
        mttrResolve: apiData.metrics.previous.mttr_resolve,
      },
    },
    trendData: apiData.trend_data,
    severityData: apiData.severity_data,
    risks: apiData.risks,
    compliance: apiData.compliance,
    generatedAt: apiData.generated_at,
  };
};

export const checkAPIHealth = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/executive/health`);
    return response.ok;
  } catch (error) {
    return false;
  }
};
