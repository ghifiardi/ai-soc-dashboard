import { motion } from 'framer-motion';
import { FileCheck, Shield, Award } from 'lucide-react';
import MetricCard from '../components/common/MetricCard';

export default function CompliancePage() {
  return (
    <div className="space-y-8">
      <motion.h1
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-5xl font-extrabold gradient-text text-center"
      >
        📜 Compliance & Audit Dashboard
      </motion.h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <MetricCard
          label="Overall Compliance"
          value="92%"
          icon={Award}
          color="green"
          badge="COMPLIANT"
          delta="+1.5% improvement"
          deltaType="positive"
        />

        <MetricCard
          label="Frameworks"
          value="7"
          icon={Shield}
          color="cyan"
          badge="TRACKED"
        />

        <MetricCard
          label="Controls Passed"
          value="389/421"
          icon={FileCheck}
          color="purple"
          badge="92.4%"
        />
      </div>

      <div className="glass-panel p-8 text-center">
        <h2 className="text-2xl font-bold mb-4">Compliance Dashboard - Coming Soon</h2>
        <p className="text-gray-400 mb-6">
          Multi-framework compliance tracking (NIST, ISO, SOC 2, GDPR, HIPAA) and audit trails will be available here.
        </p>
        <div className="inline-flex items-center space-x-2 px-4 py-2 bg-primary-blue rounded-lg">
          <span>Implementation in progress...</span>
        </div>
      </div>
    </div>
  );
}
