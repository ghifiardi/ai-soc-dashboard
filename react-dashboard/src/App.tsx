import { Routes, Route, Link, useLocation } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Shield, BarChart3, FileCheck, Target, Menu, X } from 'lucide-react';
import { useState } from 'react';

// Pages (we'll create these)
import EnhancedSOCPage from './pages/EnhancedSOCPage';
import ExecutivePage from './pages/ExecutivePage';
import CompliancePage from './pages/CompliancePage';
import ThreatHuntingPage from './pages/ThreatHuntingPage';

function App() {
  const location = useLocation();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const navItems = [
    { path: '/', label: 'Enhanced SOC', icon: Shield },
    { path: '/executive', label: 'Executive', icon: BarChart3 },
    { path: '/compliance', label: 'Compliance', icon: FileCheck },
    { path: '/threat-hunting', label: 'Threat Hunting', icon: Target },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#0A0E27] to-[#1a1f3a]">
      {/* Navigation */}
      <nav className="glass-panel border-b border-glass-border sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            {/* Logo */}
            <Link to="/" className="flex items-center space-x-3">
              <Shield className="h-8 w-8 text-accent-cyan" />
              <span className="text-xl font-bold gradient-text">
                AI-SOC Command Center
              </span>
            </Link>

            {/* Desktop Navigation */}
            <div className="hidden md:flex space-x-1">
              {navItems.map((item) => {
                const Icon = item.icon;
                const isActive = location.pathname === item.path;

                return (
                  <Link
                    key={item.path}
                    to={item.path}
                    className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-all ${
                      isActive
                        ? 'bg-primary-blue text-white'
                        : 'text-gray-300 hover:bg-glass-bg hover:text-white'
                    }`}
                  >
                    <Icon className="h-4 w-4" />
                    <span>{item.label}</span>
                  </Link>
                );
              })}
            </div>

            {/* Mobile menu button */}
            <button
              className="md:hidden p-2 rounded-lg hover:bg-glass-bg"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            >
              {mobileMenuOpen ? (
                <X className="h-6 w-6" />
              ) : (
                <Menu className="h-6 w-6" />
              )}
            </button>
          </div>

          {/* Mobile Navigation */}
          {mobileMenuOpen && (
            <motion.div
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              className="md:hidden py-4 space-y-2"
            >
              {navItems.map((item) => {
                const Icon = item.icon;
                const isActive = location.pathname === item.path;

                return (
                  <Link
                    key={item.path}
                    to={item.path}
                    onClick={() => setMobileMenuOpen(false)}
                    className={`flex items-center space-x-3 px-4 py-3 rounded-lg transition-all ${
                      isActive
                        ? 'bg-primary-blue text-white'
                        : 'text-gray-300 hover:bg-glass-bg hover:text-white'
                    }`}
                  >
                    <Icon className="h-5 w-5" />
                    <span>{item.label}</span>
                  </Link>
                );
              })}
            </motion.div>
          )}
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <motion.div
          key={location.pathname}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -20 }}
          transition={{ duration: 0.3 }}
        >
          <Routes>
            <Route path="/" element={<EnhancedSOCPage />} />
            <Route path="/executive" element={<ExecutivePage />} />
            <Route path="/compliance" element={<CompliancePage />} />
            <Route path="/threat-hunting" element={<ThreatHuntingPage />} />
          </Routes>
        </motion.div>
      </main>

      {/* Footer */}
      <footer className="border-t border-glass-border mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex flex-col md:flex-row items-center justify-between text-sm text-gray-400">
            <div className="flex items-center space-x-2 mb-4 md:mb-0">
              <Shield className="h-4 w-4 text-accent-cyan" />
              <span>AI-SOC Dashboard v2.0 - React Edition</span>
            </div>
            <div className="flex space-x-6">
              <span>Last Updated: {new Date().toLocaleString()}</span>
              <span className="text-accent-green">● Live Data</span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
