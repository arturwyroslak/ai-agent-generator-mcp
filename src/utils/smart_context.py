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
        
    async def get_smart_component_suggestions(self, description: str, domain: str) -> List[str]:
        """Inteligentne sugestie komponentów na podstawie opisu i domeny"""
        suggestions = []
        
        # Podstawowe sugestie na podstawie słów kluczowych
        keywords = description.lower().split()
        
        if any(word in keywords for word in ['chat', 'conversation', 'talk', 'rozmowa', 'czat']):
            suggestions.extend(['openai_api_integration', 'chat_interface', 'conversation_memory'])
            
        if any(word in keywords for word in ['email', 'mail', 'wiadomość', 'newsletter']):
            suggestions.extend(['gmail_integration', 'sendgrid_integration', 'email_template'])
            
        if any(word in keywords for word in ['calendar', 'schedule', 'kalendarz', 'terminarz']):
            suggestions.extend(['google_calendar_integration', 'scheduling_system'])
            
        if any(word in keywords for word in ['file', 'document', 'plik', 'dokument']):
            suggestions.extend(['file_manager', 'google_drive_integration', 'pdf_processor'])
            
        if any(word in keywords for word in ['database', 'data', 'baza', 'dane']):
            suggestions.extend(['database_connector', 'data_processor', 'csv_handler'])
            
        if any(word in keywords for word in ['web', 'website', 'scraping', 'internet']):
            suggestions.extend(['web_scraper', 'url_processor', 'selenium_automation'])
            
        # Sugestie specyficzne dla domeny
        domain_specific = {
            'customer_service': ['ticket_system', 'knowledge_base', 'chat_support'],
            'e-commerce': ['payment_processor', 'inventory_manager', 'order_tracker'],
            'marketing': ['social_media_integration', 'analytics_tracker', 'campaign_manager'],
            'finance': ['expense_tracker', 'invoice_generator', 'accounting_integration'],
            'education': ['learning_manager', 'quiz_system', 'progress_tracker'],
            'healthcare': ['appointment_scheduler', 'patient_manager', 'health_tracker']
        }
        
        if domain in domain_specific:
            suggestions.extend(domain_specific[domain])
            
        # Usuń duplikaty i ogranicz liczbę
        return list(set(suggestions))[:10]
    
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