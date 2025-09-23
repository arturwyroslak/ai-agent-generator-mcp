"""Smart Context module for AI-enhanced decision making"""

import json
from typing import Dict, Any, List
from datetime import datetime

class SmartContext:
    """Inteligentny kontekst do uczenia się wzorców i podpowiadania"""
    
    def __init__(self):
        self.learned_patterns = {}
        self.component_performance = {}
        self.domain_insights = {}
        
    async def get_smart_component_suggestions(self, description: str, domain: str, 
                                            existing_component_ids: List[str] = None) -> List[Dict[str, Any]]:
        """Inteligentne sugestie komponentów na podstawie opisu i domeny"""
        if existing_component_ids is None:
            existing_component_ids = []
            
        suggestions = []
        
        # Podstawowe sugestie na podstawie słów kluczowych
        keywords = description.lower().split()
        
        if any(word in keywords for word in ['chat', 'conversation', 'talk', 'rozmowa', 'czat']):
            suggestions.extend([
                {'component_id': 'llm_text_generator', 'reason': 'Conversation needs LLM', 'confidence': 90},
                {'component_id': 'chat_interface', 'reason': 'Chat functionality', 'confidence': 85},
                {'component_id': 'conversation_memory', 'reason': 'Context retention', 'confidence': 80}
            ])
            
        if any(word in keywords for word in ['email', 'mail', 'wiadomość', 'newsletter', 'poczta']):
            suggestions.extend([
                {'component_id': 'gmail_integration', 'reason': 'Gmail email handling', 'confidence': 90},
                {'component_id': 'sendgrid_integration', 'reason': 'Bulk email sending', 'confidence': 85},
                {'component_id': 'email_template_manager', 'reason': 'Template management', 'confidence': 80}
            ])
            
        if any(word in keywords for word in ['calendar', 'schedule', 'kalendarz', 'terminarz']):
            suggestions.extend([
                {'component_id': 'google_calendar_integration', 'reason': 'Calendar access', 'confidence': 90},
                {'component_id': 'scheduling_system', 'reason': 'Appointment scheduling', 'confidence': 85}
            ])
        
        # Filter out existing components
        filtered_suggestions = [s for s in suggestions if s['component_id'] not in existing_component_ids]
        
        # Return max 10 suggestions
        return filtered_suggestions[:10]
    
    async def get_intelligence_insights(self) -> Dict[str, Any]:
        """Zwraca aktualne insights AI"""
        return {
            "learned_patterns": list(self.learned_patterns.keys()),
            "success_metrics": {
                "total_patterns": len(self.learned_patterns),
                "component_performance_count": len(self.component_performance)
            },
            "optimization_suggestions": [
                "Use components with high success rates",
                "Learn from successful agent patterns",
                "Optimize based on domain-specific insights"
            ],
            "background_intelligence": "Active",
            "status": "full"
        }
    
    async def learn_from_successful_agent(self, agent: Dict[str, Any]):
        """Uczenie się z udanych agentów"""
        domain = agent.get('domain', 'general')
        components = agent.get('components', [])
        
        # Zapisz wzorzec sukcesu
        pattern_key = f"{domain}_{len(components)}_components"
        if pattern_key not in self.learned_patterns:
            self.learned_patterns[pattern_key] = {
                'count': 0,
                'components': {},
                'descriptions': []
            }
            
        pattern = self.learned_patterns[pattern_key]
        pattern['count'] += 1
        pattern['descriptions'].append(agent.get('description', ''))
        
        # Zlicz komponenty
        for comp in components:
            comp_id = comp.get('component_id', 'unknown')
            if comp_id not in pattern['components']:
                pattern['components'][comp_id] = 0
            pattern['components'][comp_id] += 1
            
        # Aktualizuj performance komponentów
        for comp in components:
            comp_id = comp.get('component_id', 'unknown')
            if comp_id not in self.component_performance:
                self.component_performance[comp_id] = {
                    'usage_count': 0,
                    'success_rate': 0.0,
                    'domains': []
                }
            
            perf = self.component_performance[comp_id]
            perf['usage_count'] += 1
            perf['success_rate'] = min(1.0, perf['success_rate'] + 0.1)
            if domain not in perf['domains']:
                perf['domains'].append(domain)
    
    async def get_domain_insights(self, domain: str) -> Dict[str, Any]:
        """Zwraca insights dla konkretnej domeny"""
        insights = {
            'popular_components': [],
            'success_patterns': [],
            'recommendations': []
        }
        
        # Znajdź popularne komponenty w tej domenie
        domain_components = {}
        for comp_id, perf in self.component_performance.items():
            if domain in perf['domains']:
                domain_components[comp_id] = perf['usage_count']
                
        # Sortuj po popularności
        popular = sorted(domain_components.items(), key=lambda x: x[1], reverse=True)
        insights['popular_components'] = [comp[0] for comp in popular[:5]]
        
        # Wzorce sukcesu
        for pattern_key, pattern in self.learned_patterns.items():
            if domain in pattern_key:
                insights['success_patterns'].append({
                    'pattern': pattern_key,
                    'count': pattern['count'],
                    'top_components': sorted(pattern['components'].items(), 
                                           key=lambda x: x[1], reverse=True)[:3]
                })
        
        # Rekomendacje
        insights['recommendations'] = [
            "Używaj sprawdzonych komponentów z wysokim success_rate",
            "Rozważ komponenty popularne w tej domenie",
            "Testuj nowe kombinacje na podstawie udanych wzorców"
        ]
        
        return insights

# Singleton instance
_smart_context_instance = None

def get_smart_context() -> SmartContext:
    """Zwraca singleton instance SmartContext"""
    global _smart_context_instance
    if _smart_context_instance is None:
        _smart_context_instance = SmartContext()
    return _smart_context_instance