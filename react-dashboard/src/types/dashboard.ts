export interface SecurityEvent {
  id: string;
  timestamp: Date;
  eventId: string;
  severity: 'Critical' | 'High' | 'Medium' | 'Low';
  eventType: string;
  sourceIp: string;
  destinationIp: string;
  sourceCountry?: string;
  status: 'Active' | 'Investigating' | 'Contained' | 'Resolved' | 'False Positive';
  mitreTechnique?: string;
  confidence: number;
  packets?: number;
  bytesTransferred?: number;
  protocol?: string;
  threatActor?: string;
  affectedAsset?: string;
  analystAssigned?: string;
  responseTimeMin?: number;
  falsePositiveScore?: number;
}

export interface ThreatHunt {
  missionId: string;
  huntType: string;
  startDate: Date;
  status: 'Active' | 'Investigating' | 'Completed' | 'On Hold';
  iocsFound: number;
  entitiesAnalyzed: number;
  confidence: number;
  priority: 'Critical' | 'High' | 'Medium' | 'Low';
  hunter: string;
}

export interface SocialMediaThreat {
  id: string;
  createdAt: Date;
  text: string;
  threatScore: number;
  severity: 'High' | 'Medium' | 'Low';
  keywordsFound: string[];
  platform: 'Twitter' | 'Facebook' | 'Instagram' | 'LinkedIn' | 'Reddit';
  engagement: number;
  verifiedThreat: boolean;
}

export interface MLClassification {
  model: string;
  category: string;
  confidence: number;
  truePositiveRate: number;
  falsePositiveRate: number;
  predictions: number;
}

export interface ComplianceFramework {
  name: string;
  score: number;
  controlsTotal: number;
  controlsPassed: number;
  controlsFailed: number;
  lastAudit: Date;
  nextAudit: Date;
  categories: Record<string, number>;
}

export interface AuditEntry {
  id: string;
  timestamp: Date;
  eventType: 'Access Control' | 'Data Modification' | 'Configuration Change' | 'Policy Update' | 'Compliance Check';
  severity: 'Critical' | 'High' | 'Medium' | 'Low' | 'Info';
  user: string;
  action: string;
  resource: string;
  description: string;
  ipAddress: string;
  status: 'Success' | 'Failed' | 'Pending';
}

export interface MetricData {
  label: string;
  value: number | string;
  delta?: string;
  deltaType?: 'positive' | 'negative' | 'neutral';
  icon?: string;
}

export interface ChartData {
  labels: string[];
  datasets: {
    label: string;
    data: number[];
    backgroundColor?: string | string[];
    borderColor?: string;
    fill?: boolean;
  }[];
}

export interface DashboardConfig {
  autoRefresh: boolean;
  refreshInterval: number;
  timeRange: number;
  severityFilter: string[];
  showSections: {
    overview: boolean;
    timeline: boolean;
    network: boolean;
    mitre: boolean;
    geo: boolean;
    analytics: boolean;
    events: boolean;
  };
}
