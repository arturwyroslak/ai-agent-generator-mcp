def get_workflow_templates():
    """Zwraca gotowe szablony workflow dla różnych typów agentów"""
    return [
        # === OBSŁUGA KLIENTA ===
        {
            "template_id": "customer_support_basic",
            "name": "Podstawowa Obsługa Klienta",
            "description": "Prosty agent do odpowiadania na pytania klientów",
            "domain": "customer_service",
            "complexity": "simple",
            "estimated_setup_time": "10 minut",
            "components": [
                {
                    "type": "pollinations_llm",
                    "name": "Główny LLM",
                    "config": {
                        "system_prompt": "Jesteś przyjaznym konsultantem obsługi klienta. Odpowiadaj pomocnie i profesjonalnie.",
                        "temperature": 0.7
                    }
                },
                {
                    "type": "intent_classifier",
                    "name": "Klasyfikator Intencji",
                    "config": {
                        "categories": ["question", "complaint", "compliment", "request"]
                    }
                },
                {
                    "type": "response_personalizer",
                    "name": "Personalizator",
                    "config": {
                        "style": "friendly_professional"
                    }
                }
            ],
            "workflow": {
                "steps": [
                    "input → intent_classifier",
                    "intent_classifier → llm", 
                    "llm → response_personalizer",
                    "response_personalizer → output"
                ],
                "conditions": [
                    {
                        "if": "intent == 'complaint'",
                        "then": "escalate_to_human",
                        "priority": "high"
                    }
                ]
            }
        },
        {
            "template_id": "customer_support_advanced",
            "name": "Zaawansowana Obsługa Klienta",
            "description": "Kompleksowy agent z bazą wiedzy i eskalacją",
            "domain": "customer_service",
            "complexity": "complex",
            "estimated_setup_time": "45 minut",
            "components": [
                {
                    "type": "intent_classifier",
                    "name": "Klasyfikator Intencji",
                    "config": {
                        "categories": ["question", "complaint", "technical_issue", "billing", "general"]
                    }
                },
                {
                    "type": "knowledge_base_search",
                    "name": "Wyszukiwarka FAQ",
                    "config": {
                        "knowledge_source": "company_faq",
                        "similarity_threshold": 0.8
                    }
                },
                {
                    "type": "pollinations_llm",
                    "name": "Generator Odpowiedzi",
                    "config": {
                        "system_prompt": "Jesteś ekspertem obsługi klienta. Wykorzystuj informacje z bazy wiedzy.",
                        "temperature": 0.6
                    }
                },
                {
                    "type": "sentiment_analyzer",
                    "name": "Analiza Emocji",
                    "config": {
                        "detect_frustration": true
                    }
                },
                {
                    "type": "conditional_router",
                    "name": "Router Eskalacji",
                    "config": {
                        "escalation_triggers": ["high_frustration", "complex_issue", "billing_dispute"]
                    }
                },
                {
                    "type": "slack_integration",
                    "name": "Powiadomienia Slack",
                    "config": {
                        "channel": "#customer-support",
                        "escalation_template": "Nowy ticket do obsłużenia: {ticket_id}"
                    }
                }
            ]
        },

        # === SPRZEDAŻ I MARKETING ===
        {
            "template_id": "sales_assistant",
            "name": "Asystent Sprzedaży",
            "description": "Agent wspierający proces sprzedaży",
            "domain": "sales",
            "complexity": "medium",
            "estimated_setup_time": "30 minut",
            "components": [
                {
                    "type": "lead_scorer",
                    "name": "Oceniacz Leadów",
                    "config": {
                        "scoring_criteria": ["budget", "authority", "need", "timeline"]
                    }
                },
                {
                    "type": "pollinations_llm",
                    "name": "Konsultant Sprzedaży",
                    "config": {
                        "system_prompt": "Jesteś doświadczonym konsultantem sprzedaży. Pomagasz klientom znaleźć najlepsze rozwiązania.",
                        "temperature": 0.8
                    }
                },
                {
                    "type": "hubspot_integration",
                    "name": "Integracja CRM",
                    "config": {
                        "auto_create_contacts": true,
                        "track_interactions": true
                    }
                },
                {
                    "type": "email_composer",
                    "name": "Generator Followup",
                    "config": {
                        "template_type": "sales_followup",
                        "personalization": true
                    }
                }
            ]
        },
        {
            "template_id": "lead_qualifier",
            "name": "Kwalifikator Leadów",
            "description": "Automatyczna kwalifikacja leadów sprzedażowych",
            "domain": "sales",
            "complexity": "medium",
            "estimated_setup_time": "25 minut",
            "components": [
                {
                    "type": "pollinations_llm",
                    "name": "Ankieter",
                    "config": {
                        "system_prompt": "Prowadzisz rozmowę kwalifikacyjną z potencjalnym klientem. Zadawaj inteligentne pytania.",
                        "temperature": 0.7
                    }
                },
                {
                    "type": "lead_scorer",
                    "name": "System Scoring",
                    "config": {
                        "bant_criteria": true,
                        "custom_scoring": {
                            "budget_weight": 0.3,
                            "timeline_weight": 0.25,
                            "authority_weight": 0.25,
                            "need_weight": 0.2
                        }
                    }
                },
                {
                    "type": "conditional_router",
                    "name": "Router Kwalifikacji",
                    "config": {
                        "hot_lead_threshold": 80,
                        "warm_lead_threshold": 60,
                        "cold_lead_threshold": 30
                    }
                }
            ]
        },
        {
            "template_id": "content_marketer",
            "name": "Marketer Treści",
            "description": "Tworzy i zarządza treściami marketingowymi",
            "domain": "marketing",
            "complexity": "medium",
            "estimated_setup_time": "35 minut",
            "components": [
                {
                    "type": "content_generator",
                    "name": "Generator Treści",
                    "config": {
                        "content_types": ["blog_post", "social_media", "email_campaign"],
                        "tone": "engaging"
                    }
                },
                {
                    "type": "seo_optimizer",
                    "name": "Optymalizator SEO",
                    "config": {
                        "target_keywords": true,
                        "readability_check": true
                    }
                },
                {
                    "type": "social_media_manager",
                    "name": "Manager Social Media",
                    "config": {
                        "platforms": ["facebook", "linkedin", "twitter"],
                        "optimal_timing": true
                    }
                }
            ]
        },

        # === ROZWÓJ I TECHNOLOGIA ===
        {
            "template_id": "code_reviewer",
            "name": "Recenzent Kodu",
            "description": "Automatyczna analiza i przegląd kodu",
            "domain": "development",
            "complexity": "complex",
            "estimated_setup_time": "40 minut",
            "components": [
                {
                    "type": "deepseek_coder",
                    "name": "Analizator Kodu",
                    "config": {
                        "review_focus": ["security", "performance", "style", "logic"],
                        "severity_levels": ["critical", "major", "minor", "info"]
                    }
                },
                {
                    "type": "security_scanner",
                    "name": "Skaner Bezpieczeństwa",
                    "config": {
                        "vulnerability_db": "latest",
                        "scan_dependencies": true
                    }
                },
                {
                    "type": "github_integration",
                    "name": "Integracja GitHub",
                    "config": {
                        "auto_comment": true,
                        "create_issues": true,
                        "pr_analysis": true
                    }
                },
                {
                    "type": "slack_integration",
                    "name": "Powiadomienia Dev",
                    "config": {
                        "channel": "#code-review",
                        "critical_alerts": true
                    }
                }
            ]
        },
        {
            "template_id": "documentation_bot",
            "name": "Bot Dokumentacji",
            "description": "Automatyczne generowanie i aktualizacja dokumentacji",
            "domain": "development",
            "complexity": "medium",
            "estimated_setup_time": "20 minut",
            "components": [
                {
                    "type": "code_explainer",
                    "name": "Eksplainer Kodu",
                    "config": {
                        "explanation_level": "intermediate",
                        "include_examples": true
                    }
                },
                {
                    "type": "pollinations_llm",
                    "name": "Writer Dokumentacji",
                    "config": {
                        "system_prompt": "Jesteś ekspertem w pisaniu dokumentacji technicznej. Twórz jasne i przydatne instrukcje.",
                        "temperature": 0.3
                    }
                },
                {
                    "type": "github_integration",
                    "name": "GitHub Docs",
                    "config": {
                        "auto_update_readme": true,
                        "generate_api_docs": true
                    }
                }
            ]
        },

        # === ANALITYKA I DANE ===
        {
            "template_id": "data_analyst",
            "name": "Analityk Danych",
            "description": "Automatyczna analiza i raportowanie danych",
            "domain": "analytics",
            "complexity": "complex",
            "estimated_setup_time": "50 minut",
            "components": [
                {
                    "type": "data_analyst",
                    "name": "Procesor Danych",
                    "config": {
                        "analysis_types": ["trend", "correlation", "anomaly"],
                        "statistical_tests": true
                    }
                },
                {
                    "type": "predictive_analyzer",
                    "name": "Predykcja",
                    "config": {
                        "forecasting_horizon": "30_days",
                        "confidence_intervals": true
                    }
                },
                {
                    "type": "report_generator",
                    "name": "Generator Raportów",
                    "config": {
                        "report_format": "executive",
                        "include_charts": true
                    }
                },
                {
                    "type": "google_analytics_integration",
                    "name": "Źródło Danych GA",
                    "config": {
                        "metrics": ["sessions", "pageviews", "conversions"],
                        "dimensions": ["source", "medium", "campaign"]
                    }
                }
            ]
        },
        {
            "template_id": "business_intelligence",
            "name": "Business Intelligence",
            "description": "Kompleksowe rozwiązanie BI z dashboardami",
            "domain": "analytics",
            "complexity": "complex",
            "estimated_setup_time": "60 minut",
            "components": [
                {
                    "type": "data_aggregator",
                    "name": "Agregator KPI",
                    "config": {
                        "kpis": ["revenue", "customer_acquisition", "churn_rate"],
                        "time_periods": ["daily", "weekly", "monthly"]
                    }
                },
                {
                    "type": "market_analyzer",
                    "name": "Analiza Rynku",
                    "config": {
                        "competitive_analysis": true,
                        "trend_detection": true
                    }
                },
                {
                    "type": "powerbi_connector",
                    "name": "Dashboard Power BI",
                    "config": {
                        "auto_refresh": "hourly",
                        "real_time_data": true
                    }
                }
            ]
        },

        # === HR I ZASOBY LUDZKIE ===
        {
            "template_id": "hr_assistant",
            "name": "Asystent HR",
            "description": "Wsparcie procesów HR i rekrutacji",
            "domain": "hr",
            "complexity": "medium",
            "estimated_setup_time": "35 minut",
            "components": [
                {
                    "type": "pollinations_llm",
                    "name": "Konsultant HR",
                    "config": {
                        "system_prompt": "Jesteś doświadczonym specjalistą HR. Pomagasz w procesach rekrutacji i zarządzania personelem.",
                        "temperature": 0.6
                    }
                },
                {
                    "type": "text_analyzer",
                    "name": "Analizator CV",
                    "config": {
                        "extract_skills": true,
                        "experience_analysis": true,
                        "education_parsing": true
                    }
                },
                {
                    "type": "linkedin_integration",
                    "name": "LinkedIn Recruiter",
                    "config": {
                        "candidate_search": true,
                        "profile_analysis": true
                    }
                },
                {
                    "type": "calendly_integration",
                    "name": "Planowanie Rozmów",
                    "config": {
                        "interview_types": ["phone_screen", "technical", "final"],
                        "auto_scheduling": true
                    }
                }
            ]
        },
        {
            "template_id": "employee_onboarding",
            "name": "Onboarding Pracowników",
            "description": "Automatyczny proces wdrażania nowych pracowników",
            "domain": "hr",
            "complexity": "medium",
            "estimated_setup_time": "30 minut",
            "components": [
                {
                    "type": "workflow_orchestrator",
                    "name": "Orkiestrator Onboardingu",
                    "config": {
                        "onboarding_steps": [
                            "welcome_email",
                            "document_collection",
                            "it_setup",
                            "training_schedule",
                            "mentor_assignment"
                        ]
                    }
                },
                {
                    "type": "email_composer",
                    "name": "Generator Emaili Powitalnych",
                    "config": {
                        "template_type": "welcome",
                        "personalization": true
                    }
                },
                {
                    "type": "slack_integration",
                    "name": "Integracja Slack",
                    "config": {
                        "auto_add_channels": true,
                        "welcome_message": true
                    }
                }
            ]
        },

        # === FINANSE I KSIĘGOWOŚĆ ===
        {
            "template_id": "financial_advisor",
            "name": "Doradca Finansowy",
            "description": "Automatyczna analiza finansowa i doradztwo",
            "domain": "finance",
            "complexity": "complex",
            "estimated_setup_time": "45 minut",
            "components": [
                {
                    "type": "data_analyst",
                    "name": "Analizator Finansowy",
                    "config": {
                        "financial_metrics": ["roi", "cash_flow", "profit_margin"],
                        "trend_analysis": true
                    }
                },
                {
                    "type": "pollinations_llm",
                    "name": "Konsultant Finansowy",
                    "config": {
                        "system_prompt": "Jesteś ekspertem finansowym. Analizujesz dane i udzielasz praktycznych rad.",
                        "temperature": 0.4
                    }
                },
                {
                    "type": "quickbooks_integration",
                    "name": "QuickBooks Data",
                    "config": {
                        "sync_transactions": true,
                        "generate_reports": true
                    }
                },
                {
                    "type": "report_generator",
                    "name": "Raporty Finansowe",
                    "config": {
                        "report_types": ["cash_flow", "profit_loss", "balance_sheet"]
                    }
                }
            ]
        },
        {
            "template_id": "expense_tracker",
            "name": "Tracker Wydatków",
            "description": "Automatyczne śledzenie i kategoryzacja wydatków",
            "domain": "finance",
            "complexity": "simple",
            "estimated_setup_time": "15 minut",
            "components": [
                {
                    "type": "text_classifier",
                    "name": "Klasyfikator Wydatków",
                    "config": {
                        "categories": ["travel", "office", "marketing", "software", "misc"],
                        "auto_learning": true
                    }
                },
                {
                    "type": "data_validator",
                    "name": "Walidator Danych",
                    "config": {
                        "required_fields": ["amount", "date", "vendor"],
                        "amount_limits": true
                    }
                },
                {
                    "type": "gmail_integration",
                    "name": "Email Receipts",
                    "config": {
                        "auto_extract_receipts": true,
                        "vendor_detection": true
                    }
                }
            ]
        },

        # === E-COMMERCE ===
        {
            "template_id": "ecommerce_assistant",
            "name": "Asystent E-commerce",
            "description": "Kompleksowe wsparcie sklepu internetowego",
            "domain": "ecommerce",
            "complexity": "complex",
            "estimated_setup_time": "55 minut",
            "components": [
                {
                    "type": "pollinations_llm",
                    "name": "Doradca Produktowy",
                    "config": {
                        "system_prompt": "Jesteś ekspertem e-commerce. Pomagasz klientom znaleźć idealne produkty.",
                        "temperature": 0.7
                    }
                },
                {
                    "type": "shopify_integration",
                    "name": "Integracja Shopify",
                    "config": {
                        "inventory_sync": true,
                        "order_processing": true
                    }
                },
                {
                    "type": "stripe_integration",
                    "name": "Płatności Stripe",
                    "config": {
                        "payment_processing": true,
                        "fraud_detection": true
                    }
                },
                {
                    "type": "email_composer",
                    "name": "Email Marketing",
                    "config": {
                        "template_types": ["abandoned_cart", "order_confirmation", "shipping_update"]
                    }
                }
            ]
        },
        {
            "template_id": "inventory_manager",
            "name": "Manager Magazynu",
            "description": "Automatyczne zarządzanie zapasami",
            "domain": "ecommerce",
            "complexity": "medium",
            "estimated_setup_time": "25 minut",
            "components": [
                {
                    "type": "predictive_analyzer",
                    "name": "Prognoza Popytu",
                    "config": {
                        "forecast_horizon": "90_days",
                        "seasonal_adjustment": true
                    }
                },
                {
                    "type": "conditional_router",
                    "name": "Alerts Manager",
                    "config": {
                        "low_stock_threshold": 10,
                        "reorder_point_calculation": true
                    }
                },
                {
                    "type": "shopify_integration",
                    "name": "Inventory Sync",
                    "config": {
                        "real_time_updates": true,
                        "variant_tracking": true
                    }
                }
            ]
        },

        # === AUTOMATYZACJA OGÓLNA ===
        {
            "template_id": "task_automator",
            "name": "Automatyzator Zadań",
            "description": "Uniwersalny agent do automatyzacji zadań",
            "domain": "general",
            "complexity": "medium",
            "estimated_setup_time": "20 minut",
            "components": [
                {
                    "type": "workflow_orchestrator",
                    "name": "Orkiestrator Główny",
                    "config": {
                        "task_scheduling": true,
                        "retry_logic": true
                    }
                },
                {
                    "type": "conditional_router",
                    "name": "Router Zadań",
                    "config": {
                        "task_prioritization": true,
                        "resource_allocation": true
                    }
                },
                {
                    "type": "zapier_integration",
                    "name": "Zapier Connector",
                    "config": {
                        "webhook_handling": true,
                        "multi_app_workflows": true
                    }
                }
            ]
        },
        {
            "template_id": "notification_center",
            "name": "Centrum Powiadomień",
            "description": "Inteligentne zarządzanie powiadomieniami",
            "domain": "general",
            "complexity": "simple",
            "estimated_setup_time": "15 minut",
            "components": [
                {
                    "type": "notification_sender",
                    "name": "Multi-Channel Sender",
                    "config": {
                        "channels": ["email", "sms", "slack", "teams"],
                        "smart_routing": true
                    }
                },
                {
                    "type": "scheduler",
                    "name": "Scheduler",
                    "config": {
                        "timezone_handling": true,
                        "delivery_optimization": true
                    }
                },
                {
                    "type": "rate_limiter",
                    "name": "Rate Controller",
                    "config": {
                        "prevent_spam": true,
                        "user_preferences": true
                    }
                }
            ]
        },

        # === SPECJALISTYCZNE ===
        {
            "template_id": "social_media_monitor",
            "name": "Monitor Social Media",
            "description": "Monitorowanie i zarządzanie mediami społecznościowymi",
            "domain": "marketing",
            "complexity": "complex",
            "estimated_setup_time": "40 minut",
            "components": [
                {
                    "type": "sentiment_analyzer",
                    "name": "Analiza Sentymentu",
                    "config": {
                        "platforms": ["twitter", "facebook", "instagram"],
                        "brand_mentions": true
                    }
                },
                {
                    "type": "facebook_integration",
                    "name": "Facebook Manager",
                    "config": {
                        "post_scheduling": true,
                        "engagement_tracking": true
                    }
                },
                {
                    "type": "twitter_integration",
                    "name": "Twitter Manager",
                    "config": {
                        "trend_monitoring": true,
                        "hashtag_research": true
                    }
                },
                {
                    "type": "content_generator",
                    "name": "Content Creator",
                    "config": {
                        "platform_optimization": true,
                        "viral_potential_scoring": true
                    }
                }
            ]
        },
        {
            "template_id": "security_monitor",
            "name": "Monitor Bezpieczeństwa",
            "description": "Monitoring bezpieczeństwa i wykrywanie zagrożeń",
            "domain": "security",
            "complexity": "complex",
            "estimated_setup_time": "60 minut",
            "components": [
                {
                    "type": "security_scanner",
                    "name": "Skaner Zagrożeń",
                    "config": {
                        "scan_frequency": "continuous",
                        "threat_intelligence": true
                    }
                },
                {
                    "type": "fraud_detector",
                    "name": "Detektor Anomalii",
                    "config": {
                        "ml_models": true,
                        "behavioral_analysis": true
                    }
                },
                {
                    "type": "conditional_router",
                    "name": "Incident Response",
                    "config": {
                        "severity_escalation": true,
                        "auto_mitigation": true
                    }
                },
                {
                    "type": "slack_integration",
                    "name": "Security Alerts",
                    "config": {
                        "channel": "#security-incidents",
                        "escalation_matrix": true
                    }
                }
            ]
        }
    ]