import { motion } from 'framer-motion';
import { BarChart3, TrendingUp, CheckCircle2 } from 'lucide-react';
import MetricCard from '../components/common/MetricCard';

export default function ExecutivePage() {
  return (
    <div className="space-y-8">
      <motion.h1
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-5xl font-extrabold gradient-text text-center"
      >
        🎯 Executive Dashboard
      </motion.h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <MetricCard
          label="Security Score"
          value="94/100"
          icon={CheckCircle2}
          color="green"
          badge="EXCELLENT"
          delta="+2.3% vs last month"
          deltaType="positive"
        />

        <MetricCard
          label="Total Incidents"
          value="127"
          icon={BarChart3}
          color="cyan"
          badge="30 DAYS"
          delta="-12% vs prev period"
          deltaType="positive"
        />

        <MetricCard
          label="MTTR"
          value="35m"
          icon={TrendingUp}
          color="purple"
          badge="IMPROVED"
          delta="-18% faster"
          deltaType="positive"
        />
      </div>

      <div className="glass-panel p-8 text-center">
        <h2 className="text-2xl font-bold mb-4">Executive Dashboard - Coming Soon</h2>
        <p className="text-gray-400 mb-6">
          Full executive metrics, compliance scorecards, and trend analysis will be available here.
        </p>
        <div className="inline-flex items-center space-x-2 px-4 py-2 bg-primary-blue rounded-lg">
          <span>Implementation in progress...</span>
        </div>
      </div>
    </div>
  );
}
