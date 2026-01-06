import { motion } from 'framer-motion';
import { LucideIcon } from 'lucide-react';

interface MetricCardProps {
  label: string;
  value: string | number;
  delta?: string;
  deltaType?: 'positive' | 'negative' | 'neutral';
  icon?: LucideIcon;
  color?: 'cyan' | 'green' | 'amber' | 'red' | 'purple';
  badge?: string;
}

const colorClasses = {
  cyan: 'border-l-accent-cyan text-accent-cyan',
  green: 'border-l-accent-green text-accent-green',
  amber: 'border-l-accent-amber text-accent-amber',
  red: 'border-l-accent-red text-accent-red',
  purple: 'border-l-accent-purple text-accent-purple',
};

export default function MetricCard({
  label,
  value,
  delta,
  deltaType = 'neutral',
  icon: Icon,
  color = 'cyan',
  badge,
}: MetricCardProps) {
  const deltaColorClass =
    deltaType === 'positive'
      ? 'text-accent-green'
      : deltaType === 'negative'
      ? 'text-accent-red'
      : 'text-gray-400';

  return (
    <motion.div
      whileHover={{ scale: 1.02, y: -4 }}
      transition={{ duration: 0.2 }}
      className={`glass-panel p-6 border-l-4 ${colorClasses[color]} relative overflow-hidden group`}
    >
      {/* Shimmer effect on hover */}
      <div className="shimmer" />

      {/* Content */}
      <div className="relative z-10">
        {/* Header */}
        <div className="flex items-center justify-between mb-3">
          <span className="text-sm font-semibold text-gray-300 uppercase tracking-wide">
            {label}
          </span>
          {Icon && (
            <Icon className={`h-5 w-5 ${colorClasses[color].split(' ')[1]} opacity-70`} />
          )}
        </div>

        {/* Value */}
        <div className="text-3xl md:text-4xl font-bold text-white mb-2 font-mono">
          {value}
        </div>

        {/* Delta and Badge */}
        <div className="flex items-center justify-between">
          {delta && (
            <span className={`text-sm font-semibold ${deltaColorClass}`}>
              {delta}
            </span>
          )}

          {badge && (
            <span className="px-3 py-1 text-xs font-bold rounded-full bg-gradient-to-r from-accent-green to-accent-cyan text-white pulse-glow">
              {badge}
            </span>
          )}
        </div>
      </div>

      {/* Animated background gradient on hover */}
      <div className="absolute inset-0 bg-gradient-to-br from-transparent via-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
    </motion.div>
  );
}
