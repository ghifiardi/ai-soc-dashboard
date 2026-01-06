import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Shield, AlertTriangle, CheckCircle, Clock, RefreshCw } from 'lucide-react';
import MetricCard from '../components/common/MetricCard';
import {
  generateSecurityEvents,
  generateThreatHunts,
  formatTimestamp,
  formatNumber,
} from '../utils/mockData';
import { SecurityEvent } from '../types/dashboard';

export default function EnhancedSOCPage() {
  const [events, setEvents] = useState<SecurityEvent[]>([]);
  const [loading, setLoading] = useState(true);
  const [lastRefresh, setLastRefresh] = useState(new Date());
  const [autoRefresh, setAutoRefresh] = useState(false);

  // Load initial data
  useEffect(() => {
    loadData();
  }, []);

  // Auto-refresh logic
  useEffect(() => {
    if (!autoRefresh) return;

    const interval = setInterval(() => {
      loadData();
    }, 30000); // Refresh every 30 seconds

    return () => clearInterval(interval);
  }, [autoRefresh]);

  const loadData = () => {
    setLoading(true);
    // Simulate API call with timeout
    setTimeout(() => {
      setEvents(generateSecurityEvents(100));
      setLastRefresh(new Date());
      setLoading(false);
    }, 500);
  };

  const handleRefresh = () => {
    loadData();
  };

  // Calculate metrics
  const totalEvents = events.length;
  const criticalCount = events.filter((e) => e.severity === 'Critical').length;
  const activeThreats = events.filter((e) => e.status === 'Active').length;
  const resolvedCount = events.filter((e) => e.status === 'Resolved').length;

  const severityCounts = {
    Critical: events.filter((e) => e.severity === 'Critical').length,
    High: events.filter((e) => e.severity === 'High').length,
    Medium: events.filter((e) => e.severity === 'Medium').length,
    Low: events.filter((e) => e.severity === 'Low').length,
  };

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="text-center space-y-4">
        <motion.h1
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-5xl md:text-6xl font-extrabold gradient-text text-shadow-glow"
        >
          🛡️ AI-SOC COMMAND CENTER
        </motion.h1>
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.2 }}
          className="text-xl text-gray-400"
        >
          Enterprise Security Operations | Real-time Threat Intelligence & Advanced Analytics
        </motion.p>

        {/* Current Time */}
        <div className="flex items-center justify-center space-x-2 text-accent-green font-mono">
          <Clock className="h-5 w-5" />
          <span className="text-lg font-semibold">
            Current Time: {new Date().toLocaleString()}
          </span>
        </div>
      </div>

      {/* Controls */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4 glass-panel p-4">
        <div className="flex items-center space-x-4">
          <button
            onClick={handleRefresh}
            disabled={loading}
            className="flex items-center space-x-2 px-4 py-2 bg-primary-blue hover:bg-primary-blue/80 rounded-lg transition-colors disabled:opacity-50"
          >
            <RefreshCw className={`h-4 w-4 ${loading ? 'animate-spin' : ''}`} />
            <span>Refresh</span>
          </button>

          <label className="flex items-center space-x-2 cursor-pointer">
            <input
              type="checkbox"
              checked={autoRefresh}
              onChange={(e) => setAutoRefresh(e.target.checked)}
              className="w-4 h-4 rounded"
            />
            <span className="text-sm text-gray-300">Auto-refresh (30s)</span>
          </label>
        </div>

        <div className="text-sm text-gray-400">
          Last updated: {lastRefresh.toLocaleTimeString()}
        </div>
      </div>

      {/* Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <MetricCard
          label="Total Events"
          value={formatNumber(totalEvents)}
          icon={Shield}
          color="cyan"
          badge="LIVE"
          delta="+12% vs last hour"
          deltaType="positive"
        />

        <MetricCard
          label="Critical Alerts"
          value={criticalCount}
          icon={AlertTriangle}
          color="red"
          badge="HIGH PRIORITY"
          delta="-5% vs last hour"
          deltaType="positive"
        />

        <MetricCard
          label="Active Threats"
          value={activeThreats}
          icon={AlertTriangle}
          color="amber"
          badge="MONITORING"
          delta="+3 new"
          deltaType="negative"
        />

        <MetricCard
          label="Resolved"
          value={resolvedCount}
          icon={CheckCircle}
          color="green"
          badge="SUCCESS"
          delta="+8% vs last hour"
          deltaType="positive"
        />
      </div>

      {/* Severity Distribution */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
        className="glass-panel p-6"
      >
        <h2 className="text-2xl font-bold mb-6 flex items-center space-x-2">
          <span className="text-accent-cyan">📊</span>
          <span>Threat Severity Distribution</span>
        </h2>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {Object.entries(severityCounts).map(([severity, count]) => {
            const colors = {
              Critical: 'bg-accent-red',
              High: 'bg-accent-amber',
              Medium: 'bg-primary-blue',
              Low: 'bg-accent-green',
            };

            const percentage = ((count / totalEvents) * 100).toFixed(1);

            return (
              <div
                key={severity}
                className="glass-panel p-4 border-l-4"
                style={{
                  borderLeftColor:
                    severity === 'Critical'
                      ? '#FF3B30'
                      : severity === 'High'
                      ? '#FFB800'
                      : severity === 'Medium'
                      ? '#0066FF'
                      : '#00C896',
                }}
              >
                <div className="text-sm text-gray-400 mb-2">{severity}</div>
                <div className="text-3xl font-bold mb-2">{count}</div>
                <div className="flex items-center space-x-2">
                  <div className="flex-1 h-2 bg-gray-700 rounded-full overflow-hidden">
                    <motion.div
                      initial={{ width: 0 }}
                      animate={{ width: `${percentage}%` }}
                      transition={{ duration: 1, ease: 'easeOut' }}
                      className={`h-full ${colors[severity as keyof typeof colors]}`}
                    />
                  </div>
                  <span className="text-xs text-gray-400">{percentage}%</span>
                </div>
              </div>
            );
          })}
        </div>
      </motion.div>

      {/* Recent Events Table */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
        className="glass-panel p-6"
      >
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-2xl font-bold flex items-center space-x-2">
            <span className="text-accent-cyan">🚨</span>
            <span>Recent Security Events</span>
          </h2>
          <span className="text-sm text-gray-400">
            Showing {Math.min(20, events.length)} of {formatNumber(totalEvents)} events
          </span>
        </div>

        {loading ? (
          <div className="flex items-center justify-center py-12">
            <div className="loading-spinner" />
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead className="text-left text-sm text-gray-400 border-b border-glass-border">
                <tr>
                  <th className="pb-3 px-4">Timestamp</th>
                  <th className="pb-3 px-4">Event ID</th>
                  <th className="pb-3 px-4">Severity</th>
                  <th className="pb-3 px-4">Type</th>
                  <th className="pb-3 px-4">Source IP</th>
                  <th className="pb-3 px-4">Status</th>
                  <th className="pb-3 px-4">Confidence</th>
                </tr>
              </thead>
              <tbody className="text-sm">
                {events.slice(0, 20).map((event, index) => (
                  <motion.tr
                    key={event.id}
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: index * 0.02 }}
                    className="border-b border-glass-border/50 hover:bg-glass-bg transition-colors"
                  >
                    <td className="py-3 px-4 font-mono text-xs text-gray-400">
                      {formatTimestamp(event.timestamp)}
                    </td>
                    <td className="py-3 px-4 font-mono text-accent-cyan">
                      {event.eventId}
                    </td>
                    <td className="py-3 px-4">
                      <span
                        className={`px-2 py-1 rounded text-xs font-bold ${
                          event.severity === 'Critical'
                            ? 'bg-accent-red/20 text-accent-red'
                            : event.severity === 'High'
                            ? 'bg-accent-amber/20 text-accent-amber'
                            : event.severity === 'Medium'
                            ? 'bg-primary-blue/20 text-primary-blue'
                            : 'bg-accent-green/20 text-accent-green'
                        }`}
                      >
                        {event.severity}
                      </span>
                    </td>
                    <td className="py-3 px-4">{event.eventType}</td>
                    <td className="py-3 px-4 font-mono text-xs">{event.sourceIp}</td>
                    <td className="py-3 px-4">
                      <span
                        className={`px-2 py-1 rounded text-xs ${
                          event.status === 'Active'
                            ? 'bg-accent-red/20 text-accent-red'
                            : event.status === 'Resolved'
                            ? 'bg-accent-green/20 text-accent-green'
                            : 'bg-primary-blue/20 text-primary-blue'
                        }`}
                      >
                        {event.status}
                      </span>
                    </td>
                    <td className="py-3 px-4">
                      <div className="flex items-center space-x-2">
                        <div className="flex-1 h-2 bg-gray-700 rounded-full overflow-hidden">
                          <div
                            className="h-full bg-accent-cyan"
                            style={{ width: `${event.confidence * 100}%` }}
                          />
                        </div>
                        <span className="text-xs text-gray-400">
                          {(event.confidence * 100).toFixed(0)}%
                        </span>
                      </div>
                    </td>
                  </motion.tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </motion.div>

      {/* Info Box */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
        className="glass-panel p-6 border-l-4 border-l-accent-cyan"
      >
        <div className="flex items-start space-x-4">
          <Shield className="h-6 w-6 text-accent-cyan flex-shrink-0 mt-1" />
          <div>
            <h3 className="text-lg font-bold mb-2">React + TypeScript Edition</h3>
            <p className="text-gray-400 text-sm leading-relaxed">
              This dashboard is built with React 18, TypeScript 5, and Tailwind CSS. It features
              instant client-side rendering, full type safety, smooth animations with Framer Motion,
              and can be deployed as static files to any CDN. All timestamps are dynamically
              generated relative to the current time, ensuring data is always fresh and relevant.
            </p>
            <div className="mt-4 flex flex-wrap gap-2">
              <span className="px-3 py-1 bg-primary-blue/20 text-primary-blue rounded text-xs font-semibold">
                React 18
              </span>
              <span className="px-3 py-1 bg-accent-cyan/20 text-accent-cyan rounded text-xs font-semibold">
                TypeScript 5
              </span>
              <span className="px-3 py-1 bg-accent-purple/20 text-accent-purple rounded text-xs font-semibold">
                Tailwind CSS
              </span>
              <span className="px-3 py-1 bg-accent-green/20 text-accent-green rounded text-xs font-semibold">
                Vite
              </span>
            </div>
          </div>
        </div>
      </motion.div>
    </div>
  );
}
