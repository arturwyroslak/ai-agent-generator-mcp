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
        
        # Auto-detect domain and complexity
        detected_domain = self._detect_domain_from_description(text)
        detected_complexity = self._calculate_complexity_level(analysis['complexity_score'])
        
        # Generate suggested components based on patterns
        suggested_components = self._suggest_components_for_patterns(analysis['detected_patterns'], text)
        analysis['suggested_components'] = suggested_components
        
        # Create enhanced analysis structure expected by create_agent
        return {
            'detected_patterns': analysis['detected_patterns'],
            'implicit_requirements': self._format_implicit_requirements(analysis['implicit_requirements'], analysis['detected_patterns'], text),
            'complexity_score': analysis['complexity_score'],
            'urgency_score': analysis['urgency_score'],
            'suggested_components': suggested_components,
            'workflow_patterns': analysis['workflow_patterns'],
            'domain_specific_insights': analysis['domain_specific_insights'],
            'technical_keywords': analysis['technical_keywords'],
            'business_keywords': analysis['business_keywords'],
            'enhanced_analysis': {
                'detected_domain': detected_domain,
                'complexity_level': detected_complexity,
                'confidence_score': self._calculate_confidence_score(analysis['detected_patterns'], text)
            },
            'smart_suggestions': suggested_components,
            'io_requirements': self._detect_io_requirements(text, analysis['detected_patterns'])
        }
    
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
    
    def _detect_domain_from_description(self, text: str) -> str:
        """Wykrywa domenę na podstawie treści opisu"""
        
        # Email/Communication domain
        if any(word in text for word in ['email', 'mail', 'poczta', 'wiadomość', 'newsletter', 'smtp', 'imap']):
            return 'communication'
        
        # E-commerce domain  
        if any(word in text for word in ['shop', 'sklep', 'product', 'produkt', 'order', 'zamówienie', 'payment', 'płatność']):
            return 'ecommerce'
            
        # Customer service domain
        if any(word in text for word in ['support', 'wsparcie', 'help', 'pomoc', 'ticket', 'chat', 'customer', 'klient']):
            return 'customer_service'
            
        # Sales domain
        if any(word in text for word in ['sales', 'sprzedaż', 'lead', 'crm', 'deal', 'kontrakt', 'offer', 'oferta']):
            return 'sales'
            
        # Marketing domain
        if any(word in text for word in ['marketing', 'campaign', 'kampania', 'social', 'analytics', 'tracking']):
            return 'marketing'
            
        # Finance domain
        if any(word in text for word in ['finance', 'finanse', 'invoice', 'faktura', 'payment', 'accounting', 'księgowość']):
            return 'finance'
            
        return 'general'
    
    def _calculate_complexity_level(self, complexity_score: int) -> str:
        """Oblicza poziom złożoności na podstawie wyniku"""
        if complexity_score >= 7:
            return 'complex'
        elif complexity_score >= 4:
            return 'medium'
        else:
            return 'simple'
    
    def _calculate_confidence_score(self, detected_patterns: List[str], text: str) -> int:
        """Oblicza poziom pewności analizy"""
        base_score = 50
        
        # Add points for each detected pattern
        pattern_score = len(detected_patterns) * 10
        
        # Add points for specific keywords
        keyword_matches = 0
        all_keywords = ['email', 'mail', 'automation', 'integration', 'api', 'workflow', 'process']
        for keyword in all_keywords:
            if keyword in text:
                keyword_matches += 1
        
        keyword_score = keyword_matches * 5
        
        total_score = min(95, base_score + pattern_score + keyword_score)
        return max(60, total_score)  # Minimum 60% confidence
    
    def _suggest_components_for_patterns(self, patterns: List[str], text: str) -> List[Dict[str, Any]]:
        """Sugeruje komponenty na podstawie wykrytych wzorców"""
        suggestions = []
        
        # Email/Communication components
        if 'communication' in patterns or any(word in text for word in ['email', 'mail', 'poczta', 'śledzenie', 'tracking']):
            suggestions.extend([
                {
                    'component_id': 'gmail_integration',
                    'reason': 'Wykryto potrzebę obsługi poczty Gmail',
                    'confidence': 90
                },
                {
                    'component_id': 'outlook_integration', 
                    'reason': 'Wykryto potrzebę obsługi poczty Outlook',
                    'confidence': 85
                },
                {
                    'component_id': 'sendgrid_integration',
                    'reason': 'Wykryto potrzebę masowego wysyłania emaili',
                    'confidence': 80
                },
                {
                    'component_id': 'email_template_manager',
                    'reason': 'Wykryto potrzebę zarządzania szablonami emaili',
                    'confidence': 85
                }
            ])
        
        # User interaction components
        if 'user_interaction' in patterns:
            suggestions.extend([
                {
                    'component_id': 'llm_text_generator',
                    'reason': 'Wykryto potrzebę generowania odpowiedzi',
                    'confidence': 95
                },
                {
                    'component_id': 'intent_classifier',
                    'reason': 'Wykryto potrzebę klasyfikacji intencji użytkownika',
                    'confidence': 85
                }
            ])
        
        # Automation components
        if 'automation' in patterns:
            suggestions.extend([
                {
                    'component_id': 'scheduler',
                    'reason': 'Wykryto potrzebę automatyzacji procesów',
                    'confidence': 90
                },
                {
                    'component_id': 'workflow_engine',
                    'reason': 'Wykryto potrzebę zarządzania przepływem pracy',
                    'confidence': 85
                }
            ])
        
        # Data processing components
        if 'data_processing' in patterns:
            suggestions.extend([
                {
                    'component_id': 'data_validator',
                    'reason': 'Wykryto potrzebę walidacji danych',
                    'confidence': 80
                },
                {
                    'component_id': 'data_transformer',
                    'reason': 'Wykryto potrzebę przetwarzania danych',
                    'confidence': 75
                }
            ])
        
        return suggestions
    
    def _format_implicit_requirements(self, requirements: List[str], patterns: List[str], text: str) -> List[Dict[str, Any]]:
        """Formatuje ukryte wymagania do odpowiedniej struktury"""
        formatted_requirements = []
        
        for req in requirements:
            formatted_requirements.append({
                'reasoning': req,
                'confidence': 75,
                'suggested_components': self._get_components_for_requirement(req)
            })
        
        # Add email-specific requirements if email patterns detected
        if 'communication' in patterns or any(word in text for word in ['email', 'mail', 'poczta']):
            formatted_requirements.extend([
                {
                    'reasoning': 'Agent do obsługi poczty wymaga integracji SMTP/IMAP',
                    'confidence': 95,
                    'suggested_components': ['gmail_integration', 'outlook_integration', 'sendgrid_integration']
                },
                {
                    'reasoning': 'Konieczne jest śledzenie statusu dostarczenia emaili',
                    'confidence': 85,
                    'suggested_components': ['email_tracker', 'delivery_monitor']
                },
                {
                    'reasoning': 'Potrzeba automatycznego przetwarzania przychodzących wiadomości',
                    'confidence': 90,
                    'suggested_components': ['email_parser', 'auto_responder', 'priority_classifier']
                }
            ])
        
        return formatted_requirements
    
    def _get_components_for_requirement(self, requirement: str) -> List[str]:
        """Zwraca komponenty dla danego wymagania"""
        requirement_lower = requirement.lower()
        
        if 'template' in requirement_lower or 'personaliz' in requirement_lower:
            return ['email_template_manager', 'personalization_engine']
        elif 'tracking' in requirement_lower or 'delivery' in requirement_lower:
            return ['email_tracker', 'delivery_monitor']
        elif 'backup' in requirement_lower or 'recovery' in requirement_lower:
            return ['data_backup', 'recovery_manager']
        elif 'validation' in requirement_lower or 'security' in requirement_lower:
            return ['data_validator', 'security_scanner']
        elif 'monitor' in requirement_lower or 'logging' in requirement_lower:
            return ['monitoring_agent', 'log_analyzer']
        
        return ['utility_helper']
    
    def _detect_io_requirements(self, text: str, patterns: List[str]) -> Dict[str, List[str]]:
        """Wykrywa wymagania wejścia i wyjścia"""
        inputs = ['user_message']
        outputs = ['response']
        
        if 'communication' in patterns or 'email' in text:
            inputs.extend(['email_content', 'recipient_list', 'subject'])
            outputs.extend(['sent_confirmation', 'delivery_status', 'email_response'])
        
        if 'data_processing' in patterns:
            inputs.extend(['data_file', 'parameters'])
            outputs.extend(['processed_data', 'report'])
        
        if 'automation' in patterns:
            inputs.extend(['trigger_event', 'schedule'])
            outputs.extend(['execution_log', 'status_update'])
        
        return {
            'inputs': list(set(inputs)),
            'outputs': list(set(outputs))
        }

# Singleton instance
_description_analyzer_instance = None

def get_description_analyzer() -> DescriptionAnalyzer:
    """Zwraca singleton instance DescriptionAnalyzer"""
    global _description_analyzer_instance
    if _description_analyzer_instance is None:
        _description_analyzer_instance = DescriptionAnalyzer()
    return _description_analyzer_instance