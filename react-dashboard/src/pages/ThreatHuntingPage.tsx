import { motion } from 'framer-motion';
import { Target, Zap, Search } from 'lucide-react';
import MetricCard from '../components/common/MetricCard';

export default function ThreatHuntingPage() {
  return (
    <div className="space-y-8">
      <motion.h1
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-5xl font-extrabold gradient-text text-center"
      >
        🔍 Threat Hunting Dashboard
      </motion.h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <MetricCard
          label="Active Hunts"
          value="8"
          icon={Target}
          color="amber"
          badge="HUNTING"
          delta="3 new missions"
          deltaType="neutral"
        />

        <MetricCard
          label="IOCs Found"
          value="47"
          icon={Zap}
          color="red"
          badge="TRACKED"
          delta="+12 today"
          deltaType="positive"
        />

        <MetricCard
          label="ML Models"
          value="7"
          icon={Search}
          color="purple"
          badge="AI-POWERED"
        />
      </div>

      <div className="glass-panel p-8 text-center">
        <h2 className="text-2xl font-bold mb-4">Threat Hunting Dashboard - Coming Soon</h2>
        <p className="text-gray-400 mb-6">
          AI-powered threat hunting with hunt missions, IOC tracking, and social media monitoring will be available here.
        </p>
        <div className="inline-flex items-center space-x-2 px-4 py-2 bg-primary-blue rounded-lg">
          <span>Implementation in progress...</span>
        </div>
      </div>
    </div>
  );
}
