"""Description Analyzer for intelligent requirement detection"""

import re
from typing import Dict, Any, List
from datetime import datetime

class DescriptionAnalyzer:
    """Analizator opisów do wykrywania ukrytych wymagań i wzorców"""
    
    def __init__(self):
        self.patterns = {
            'data_processing': [
                r'\b(proces|przetwarzanie|analiza|dane|database|baza|csv|excel|json)\b',
                r'\b(import|export|konwersja|transformacja|parsing)\b'
            ],
            'user_interaction': [
                r'\b(chat|rozmowa|conversation|interface|ui|użytkownik|user)\b',
                r'\b(input|wejście|pytanie|question|odpowiedź|response)\b'
            ],
            'automation': [
                r'\b(automatyz|automation|trigger|scheduled|cron|workflow)\b',
                r'\b(task|zadanie|proces|process|wykonanie|execution)\b'
            ],
            'integration': [
                r'\b(api|integration|connect|połączenie|webhook|sync)\b',
                r'\b(slack|discord|gmail|google|facebook|twitter|salesforce)\b'
            ],
            'file_handling': [
                r'\b(file|plik|document|dokument|upload|download|storage)\b',
                r'\b(pdf|doc|txt|image|photo|zdjęcie|obrazek)\b'
            ],
            'communication': [
                r'\b(email|mail|wiadomość|message|notification|powiadomienie)\b',
                r'\b(send|wyślij|receive|odbierz|sms|newsletter)\b'
            ],
            'security': [
                r'\b(security|bezpieczeństwo|auth|login|password|hasło)\b',
                r'\b(permission|uprawnienie|role|rola|access|dostęp)\b'
            ],
            'analytics': [
                r'\b(analityka|analytics|report|raport|statystyki|metrics)\b',
                r'\b(dashboard|wykres|chart|visualization|monitoring)\b'
            ]
        }
        
        self.complexity_indicators = [
            r'\b(complex|złożony|advanced|zaawansowany|sophisticated)\b',
            r'\b(multiple|wiele|different|różne|various|różnorodne)\b',
            r'\b(custom|niestandardowy|specific|specyficzny|unique)\b'
        ]
        
        self.urgency_indicators = [
            r'\b(urgent|pilne|asap|natychmiast|quickly|szybko)\b',
            r'\b(deadline|termin|time|czas|today|dzisiaj|immediately)\b'
        ]
    
    async def analyze_description(self, description: str, domain: str) -> Dict[str, Any]:
        """Analizuje opis i zwraca szczegółową analizę"""
        
        analysis = {
            'detected_patterns': [],
            'implicit_requirements': [],
            'complexity_score': 0,
            'urgency_score': 0,
            'suggested_components': [],
            'workflow_patterns': [],
            'domain_specific_insights': {},
            'technical_keywords': [],
            'business_keywords': []
        }
        
        text = description.lower()
        
        # Wykrywanie wzorców
        for pattern_name, pattern_regexes in self.patterns.items():
            for regex in pattern_regexes:
                if re.search(regex, text, re.IGNORECASE):
                    if pattern_name not in analysis['detected_patterns']:
                        analysis['detected_patterns'].append(pattern_name)
                    break
        
        # Analiza złożoności
        complexity_count = sum(1 for regex in self.complexity_indicators 
                             if re.search(regex, text, re.IGNORECASE))
        analysis['complexity_score'] = min(10, complexity_count * 2 + len(analysis['detected_patterns']))
        
        # Analiza pilności
        urgency_count = sum(1 for regex in self.urgency_indicators 
                          if re.search(regex, text, re.IGNORECASE))
        analysis['urgency_score'] = min(10, urgency_count * 3)
        
        # Ukryte wymagania na podstawie wzorców
        analysis['implicit_requirements'] = self._extract_implicit_requirements(
            analysis['detected_patterns'], text
        )
        
        # Wzorce workflow
        analysis['workflow_patterns'] = self._detect_workflow_patterns(text)
        
        # Słowa kluczowe techniczne i biznesowe
        analysis['technical_keywords'] = self._extract_technical_keywords(text)
        analysis['business_keywords'] = self._extract_business_keywords(text)
        
        # Insights specyficzne dla domeny
        analysis['domain_specific_insights'] = self._get_domain_insights(domain, text)
        
        return analysis
    
    def _extract_implicit_requirements(self, patterns: List[str], text: str) -> List[str]:
        """Wykrywa ukryte wymagania na podstawie wzorców"""
        requirements = []
        
        if 'user_interaction' in patterns:
            requirements.append("System powinien być intuicyjny i user-friendly")
            if 'chat' in text or 'rozmowa' in text:
                requirements.append("Implementacja natural language processing")
        
        if 'data_processing' in patterns:
            requirements.append("Zabezpieczenie i walidacja danych wejściowych")
            requirements.append("System backup i recovery danych")
            
        if 'integration' in patterns:
            requirements.append("Obsługa rate limiting i error handling")
            requirements.append("Monitoring i logging integracji")
            
        if 'file_handling' in patterns:
            requirements.append("Kontrola rozmiaru i typu plików")
            requirements.append("Skanowanie antywirusowe przesyłanych plików")
            
        if 'communication' in patterns:
            requirements.append("System templates i personalizacji")
            requirements.append("Tracking delivery i engagement")
            
        if 'automation' in patterns:
            requirements.append("Graceful failure handling")
            requirements.append("Manual override capabilities")
            
        return requirements
    
    def _detect_workflow_patterns(self, text: str) -> List[str]:
        """Wykrywa wzorce workflow"""
        patterns = []
        
        # Sequential patterns
        if any(word in text for word in ['step', 'krok', 'kolejno', 'następnie', 'then', 'after']):
            patterns.append('sequential')
            
        # Conditional patterns  
        if any(word in text for word in ['if', 'jeśli', 'when', 'kiedy', 'condition', 'warunek']):
            patterns.append('conditional')
            
        # Parallel patterns
        if any(word in text for word in ['parallel', 'równolegle', 'simultaneously', 'jednocześnie']):
            patterns.append('parallel')
            
        # Loop patterns
        if any(word in text for word in ['repeat', 'powtarzaj', 'loop', 'cycle', 'cykl']):
            patterns.append('iterative')
            
        return patterns
    
    def _extract_technical_keywords(self, text: str) -> List[str]:
        """Wyciąga słowa kluczowe techniczne"""
        technical_terms = [
            'api', 'rest', 'graphql', 'webhook', 'json', 'xml', 'csv',
            'database', 'sql', 'nosql', 'redis', 'mongodb', 'postgresql',
            'authentication', 'oauth', 'jwt', 'ssl', 'https',
            'cloud', 'aws', 'azure', 'gcp', 'docker', 'kubernetes',
            'microservices', 'serverless', 'lambda', 'function'
        ]
        
        found_terms = []
        for term in technical_terms:
            if term in text.lower():
                found_terms.append(term)
                
        return found_terms
    
    def _extract_business_keywords(self, text: str) -> List[str]:
        """Wyciąga słowa kluczowe biznesowe"""
        business_terms = [
            'customer', 'klient', 'user', 'użytkownik',
            'sale', 'sprzedaż', 'revenue', 'przychód',
            'marketing', 'campaign', 'kampania',
            'support', 'wsparcie', 'help', 'pomoc',
            'analytics', 'analityka', 'report', 'raport',
            'efficiency', 'efektywność', 'productivity', 'produktywność',
            'cost', 'koszt', 'budget', 'budżet',
            'roi', 'return', 'zwrot', 'profit', 'zysk'
        ]
        
        found_terms = []
        for term in business_terms:
            if term in text.lower():
                found_terms.append(term)
                
        return found_terms
    
    def _get_domain_insights(self, domain: str, text: str) -> Dict[str, Any]:
        """Zwraca insights specyficzne dla domeny"""
        insights = {
            'domain_priorities': [],
            'common_patterns': [],
            'recommended_features': []
        }
        
        domain_knowledge = {
            'e-commerce': {
                'priorities': ['security', 'performance', 'user_experience'],
                'patterns': ['product_catalog', 'shopping_cart', 'payment_processing'],
                'features': ['inventory_management', 'order_tracking', 'customer_reviews']
            },
            'customer_service': {
                'priorities': ['response_time', 'knowledge_base', 'escalation'],
                'patterns': ['ticket_system', 'chat_support', 'knowledge_search'],
                'features': ['automated_responses', 'sentiment_analysis', 'performance_metrics']
            },
            'marketing': {
                'priorities': ['targeting', 'personalization', 'analytics'],
                'patterns': ['campaign_management', 'lead_generation', 'conversion_tracking'],
                'features': ['a_b_testing', 'social_media_integration', 'email_automation']
            },
            'finance': {
                'priorities': ['compliance', 'accuracy', 'audit_trail'],
                'patterns': ['transaction_processing', 'reporting', 'reconciliation'],
                'features': ['fraud_detection', 'automated_invoicing', 'tax_calculation']
            }
        }
        
        if domain in domain_knowledge:
            domain_info = domain_knowledge[domain]
            insights['domain_priorities'] = domain_info['priorities']
            insights['common_patterns'] = domain_info['patterns']
            insights['recommended_features'] = domain_info['features']
        
        return insights

# Singleton instance
_description_analyzer_instance = None

def get_description_analyzer() -> DescriptionAnalyzer:
    """Zwraca singleton instance DescriptionAnalyzer"""
    global _description_analyzer_instance
    if _description_analyzer_instance is None:
        _description_analyzer_instance = DescriptionAnalyzer()
    return _description_analyzer_instance