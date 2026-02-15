import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ArrowRight, Shield, Zap, Activity, Users, Lock, Play, Layers, Code, Cpu, ChevronRight, Terminal, BarChart3, Fingerprint } from 'lucide-react';
import { Link } from 'react-router-dom';
import HowItWorksModal from '../components/HowItWorksModal';

// --- Hero Section ---
const HeroSection = ({ onOpenModal }) => (
    <div className="relative min-h-screen flex items-center justify-center overflow-hidden pt-20 pb-32">
        {/* Background Effects */}
        <div className="absolute inset-0 z-0 bg-background">
             <div className="absolute inset-0 bg-grid-white/[0.02] bg-[length:50px_50px]" />
             <div className="absolute top-0 right-0 -mr-20 -mt-20 w-[600px] h-[600px] bg-blue-500/10 rounded-full blur-[120px] animate-pulse" />
             <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-[500px] h-[500px] bg-accent-cyan/5 rounded-full blur-[100px]" />
            <div className="absolute inset-0 bg-noise opacity-20 pointer-events-none mix-blend-overlay" />
        </div>

        <div className="relative z-10 container mx-auto px-6 grid lg:grid-cols-2 gap-12 items-center">
            
            {/* Text Content */}
            <motion.div 
                initial={{ opacity: 0, x: -30 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.8, ease: "easeOut" }}
                className="space-y-8 text-center lg:text-left"
            >
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-mono tracking-wider uppercase backdrop-blur-md">
                    <span className="relative flex h-2 w-2">
                      <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
                      <span className="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
                    </span>
                    TrustLens Intelligence v2.0
                </div>

                <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-white leading-[1.1]">
                    Logic Over <br />
                    <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-accent-cyan">Hallucination.</span>
                </h1>

                <p className="text-xl text-text-secondary leading-relaxed max-w-2xl mx-auto lg:mx-0 font-light">
                    The specialized multi-agent system that <span className="text-white font-medium">reasons</span> about your code's security, logic, and quality. No guessing allowed.
                </p>

                <div className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start pt-4">
                    <Link to="/analyze" className="group relative px-8 py-4 bg-white text-background rounded-xl font-bold transition-all hover:bg-blue-50 hover:scale-[1.02] shadow-[0_0_20px_rgba(255,255,255,0.3)] hover:shadow-[0_0_30px_rgba(255,255,255,0.4)] flex items-center justify-center gap-2">
                        Start Analysis
                        <ArrowRight className="w-5 h-5 transition-transform group-hover:translate-x-1" />
                    </Link>
                    
                    <button 
                        onClick={onOpenModal}
                        className="group px-8 py-4 rounded-xl border border-white/10 hover:bg-white/5 text-white transition-all hover:border-white/20 flex items-center justify-center gap-3 backdrop-blur-sm"
                    >
                        <Play className="w-4 h-4 fill-current opacity-70" />
                        <span>Visual Walkthrough</span>
                    </button>
                </div>
                
                <div className="pt-8 flex items-center justify-center lg:justify-start gap-8 text-sm text-muted font-medium">
                     <div className="flex items-center gap-2"> <Shield className="w-4 h-4 text-emerald-500" /> Enterprise Grade </div>
                     <div className="flex items-center gap-2"> <Cpu className="w-4 h-4 text-accent-cyan" /> Multi-Agent Core </div>
                </div>
            </motion.div>

            {/* Visual Element */}
            <motion.div
                 initial={{ opacity: 0, scale: 0.9 }}
                 animate={{ opacity: 1, scale: 1 }}
                 transition={{ duration: 1, delay: 0.2 }}
                 className="relative hidden lg:block"
            >
                {/* Abstract Code/Analysis Interface Mockup */}
                <div className="relative z-10 bg-surface/80 border border-white/10 rounded-2xl p-6 backdrop-blur-xl shadow-2xl skew-y-[-2deg] hover:skew-y-0 transition-transform duration-700 ease-out">
                    <div className="flex items-center gap-4 mb-6 border-b border-white/5 pb-4">
                        <div className="flex gap-2">
                            <div className="w-3 h-3 rounded-full bg-red-500/20 border border-red-500/50" />
                            <div className="w-3 h-3 rounded-full bg-yellow-500/20 border border-yellow-500/50" />
                            <div className="w-3 h-3 rounded-full bg-emerald-500/20 border border-emerald-500/50" />
                        </div>
                        <div className="text-xs font-mono text-muted flex-1 text-center">analysis_core_v2.tsx</div>
                    </div>
                    
                    <div className="space-y-4 font-mono text-sm">
                        <div className="flex gap-4">
                             <span className="text-muted w-6 text-right">01</span>
                             <span className="text-purple-400">const</span> <span className="text-blue-400">analyzeCode</span> = <span className="text-purple-400">async</span> (<span className="text-orange-400">snippet</span>) ={'>'} {'{'}
                        </div>
                         <div className="flex gap-4">
                             <span className="text-muted w-6 text-right">02</span>
                             <span className="pl-4 text-muted">// Dispatching agents...</span>
                        </div>
                        <div className="flex gap-4 bg-blue-500/10 -mx-6 px-6 py-1 border-l-2 border-blue-500">
                             <span className="text-muted w-6 text-right">03</span>
                             <span className="pl-4 text-blue-300">await securityAgent.scan(snippet);</span>
                             <Shield className="w-4 h-4 text-blue-400 animate-pulse ml-auto" />
                        </div>
                        <div className="flex gap-4 bg-emerald-500/10 -mx-6 px-6 py-1 border-l-2 border-emerald-500">
                             <span className="text-muted w-6 text-right">04</span>
                             <span className="pl-4 text-emerald-300">await logicAgent.verify(snippet);</span>
                             <Zap className="w-4 h-4 text-emerald-400 animate-pulse ml-auto" />
                        </div>
                         <div className="flex gap-4">
                             <span className="text-muted w-6 text-right">05</span>
                             <span className="pl-4 text-text-secondary">return calculateConfidence();</span>
                        </div>
                        <div className="flex gap-4">
                             <span className="text-muted w-6 text-right">06</span>
                             <span>{'}'}</span>
                        </div>
                    </div>

                    <div className="absolute -bottom-6 -right-6 bg-surface border border-white/10 p-4 rounded-xl shadow-xl flex items-center gap-4">
                         <div className="w-10 h-10 rounded-full bg-emerald-500/20 flex items-center justify-center">
                             <Activity className="w-5 h-5 text-emerald-500" />
                         </div>
                         <div>
                             <div className="text-xs text-muted uppercase tracking-wider font-bold">Confidence Score</div>
                             <div className="text-xl font-bold text-white">98.4%</div>
                         </div>
                    </div>
                </div>

                {/* Decorative Glows */}
                <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full bg-blue-500/20 blur-[80px] -z-10 rounded-full" />
            </motion.div>
        </div>
    </div>
);

// --- Features Grid (The "Brain") ---
const FeaturesSection = () => {
    const features = [
        { 
            title: "Security Specialist", 
            desc: "Identifies vulnerabilities, injection risks, and auth flaws.",
            icon: Lock,
            color: "from-red-500/20 to-red-600/5",
            border: "group-hover:border-red-500/30",
            iconColor: "text-red-400"
        },
        { 
            title: "Logic Architect", 
            desc: "Traces execution paths to find deadlocks and race conditions.",
            icon: Zap,
            color: "from-emerald-500/20 to-emerald-600/5",
            border: "group-hover:border-emerald-500/30",
            iconColor: "text-emerald-400"

        },
        { 
            title: "Quality Controller", 
            desc: "Enforces readability, complexity limits, and best practices.",
            icon: Layers,
            color: "from-amber-500/20 to-amber-600/5",
            border: "group-hover:border-amber-500/30",
            iconColor: "text-amber-400"
        }
    ];

    return (
        <section className="py-24 relative">
             <div className="max-w-7xl mx-auto px-6">
                <div className="text-center mb-16">
                    <h2 className="text-3xl md:text-5xl font-bold text-white mb-6">The Multi-Agent Advantage</h2>
                    <p className="text-text-secondary max-w-2xl mx-auto text-lg font-light">
                        Single models hallucinate. TrustLens uses a council of specialized agents to cross-verify every line of code.
                    </p>
                </div>

                <div className="grid md:grid-cols-3 gap-8">
                    {features.map((f, i) => (
                        <motion.div 
                            key={i}
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                            transition={{ delay: i * 0.1 }}
                            className={`group relative p-8 rounded-2xl bg-surface border border-white/5 ${f.border} transition-all duration-300 hover:-translate-y-1 overflow-hidden`}
                        >
                             <div className={`absolute inset-0 bg-gradient-to-br ${f.color} opacity-0 group-hover:opacity-100 transition-opacity duration-500`} />
                             
                             <div className="relative z-10">
                                 <div className={`w-12 h-12 rounded-lg bg-background/50 border border-white/10 flex items-center justify-center mb-6`}>
                                     <f.icon className={`w-6 h-6 ${f.iconColor}`} />
                                 </div>
                                 <h3 className="text-xl font-bold text-white mb-3">{f.title}</h3>
                                 <p className="text-text-secondary leading-relaxed">{f.desc}</p>
                             </div>
                        </motion.div>
                    ))}
                </div>
             </div>
        </section>
    );
};

// --- Interactive Data / Confidence Concept ---
const DataSection = () => (
    <section className="py-24 bg-secondary/30 border-y border-white/5">
        <div className="max-w-7xl mx-auto px-6 grid lg:grid-cols-2 gap-16 items-center">
             <div>
                 <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 text-xs font-bold uppercase tracking-wider mb-6">
                    <Activity className="w-3 h-3" />
                    Transparency Core
                 </div>
                 <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">Confidence, Quantified.</h2>
                 <p className="text-text-secondary text-lg mb-8 leading-relaxed">
                     Every analysis comes with a confidence score derived from agent consensus. If the Logic Agent and Security Agent disagree, the score drops. You get the raw reasoning, not a black box answer.
                 </p>
                 
                 <div className="space-y-4">
                     {[
                         { label: "Consensus Check", val: "Pass", color: "text-emerald-400" },
                         { label: "Conflict Detection", val: "0 Found", color: "text-emerald-400" },
                         { label: "Reasoning Depth", val: "Level 4", color: "text-blue-400" },
                     ].map((item, i) => (
                         <div key={i} className="flex items-center justify-between p-4 rounded-lg bg-background border border-white/5">
                             <span className="text-muted font-medium">{item.label}</span>
                             <span className={`font-mono font-bold ${item.color}`}>{item.val}</span>
                         </div>
                     ))}
                 </div>
             </div>
             
             <div className="relative">
                 {/* Decorative Grid */}
                 <div className="absolute inset-0 bg-gradient-to-tr from-blue-500/10 to-purple-500/10 rounded-2xl blur-2xl" />
                 <div className="relative bg-background border border-white/10 rounded-2xl p-8 overflow-hidden">
                     <div className="flex justify-between items-end mb-8">
                         <div>
                             <div className="text-sm text-muted mb-1">Total System Confidence</div>
                             <div className="text-5xl font-bold text-white tracking-tight">94.2%</div>
                         </div>
                         <div className="h-10 w-32 bg-emerald-500/10 rounded overflow-hidden flex items-end gap-1 pb-1 px-1">
                             {[40, 70, 50, 90, 60, 80, 75, 95].map((h, i) => (
                                 <div key={i} style={{ height: `${h}%` }} className="flex-1 bg-emerald-500/50 rounded-sm" />
                             ))}
                         </div>
                     </div>
                     
                     <div className="space-y-3">
                         <div className="h-2 w-full bg-surface rounded-full overflow-hidden">
                             <div className="h-full bg-emerald-500 w-[94%]" />
                         </div>
                         <div className="flex justify-between text-xs font-mono text-muted">
                             <span>SECURITY: 98%</span>
                             <span>LOGIC: 92%</span>
                             <span>QUALITY: 95%</span>
                         </div>
                     </div>
                 </div>
             </div>
        </div>
    </section>
);

// --- CTA Section ---
const CTASection = () => (
    <section className="py-32 relative overflow-hidden text-center">
        <div className="absolute inset-0 bg-blue-600/5" />
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[400px] bg-accent-cyan/10 blur-[100px] rounded-full" />
        
        <div className="relative z-10 max-w-4xl mx-auto px-6">
            <h2 className="text-4xl md:text-5xl font-bold text-white mb-8 tracking-tight">
                Ready to stop guessing?
            </h2>
            <p className="text-xl text-text-secondary mb-10 max-w-2xl mx-auto">
                Deploy the swarm on your codebase today. Get actionable insights in seconds.
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
                 <Link to="/analyze" className="px-10 py-4 bg-white text-background rounded-full font-bold hover:bg-gray-100 transition-colors shadow-lg shadow-white/10 flex items-center justify-center gap-2">
                    <Terminal className="w-5 h-5 text-blue-600" />
                    Initialize Analysis
                </Link>
            </div>
        </div>
    </section>
);

const LandingPage = () => {
    const [isModalOpen, setIsModalOpen] = useState(false);

    return (
        <div className="min-h-screen bg-background text-primary selection:bg-accent-cyan/30 selection:text-white font-sans">
            <HeroSection onOpenModal={() => setIsModalOpen(true)} />
            <FeaturesSection />
            <DataSection />
            <CTASection />
            <HowItWorksModal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} />
        </div>
    );
};

export default LandingPage;
