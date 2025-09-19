def get_usage_examples():
    """Zwraca przykłady użycia komponentów"""
    return {
        "pollinations_llm": {
            "basic_chat": {
                "description": "Podstawowa rozmowa z AI",
                "input": {
                    "prompt": "Jak mogę poprawić produktywność w pracy?",
                    "system_prompt": "Jesteś ekspertem produktywności.",
                    "temperature": 0.7
                },
                "expected_output": {
                    "generated_text": "Oto kilka sprawdzonych sposobów na zwiększenie produktywności...",
                    "model_used": "openai"
                }
            },
            "code_generation": {
                "description": "Generowanie kodu Python",
                "input": {
                    "prompt": "Napisz funkcję Python do sortowania listy",
                    "system_prompt": "Jesteś ekspertem programowania Python.",
                    "temperature": 0.3
                },
                "expected_output": {
                    "generated_text": "def sort_list(lst):\n    return sorted(lst)"
                }
            }
        },
        "sentiment_analyzer": {
            "product_review": {
                "description": "Analiza opinii o produkcie",
                "input": {
                    "text": "Ten produkt jest niesamowity! Bardzo polecam każdemu.",
                    "language": "pl"
                },
                "expected_output": {
                    "sentiment": "positive",
                    "confidence": 0.95,
                    "emotions": ["joy", "satisfaction"]
                }
            },
            "customer_feedback": {
                "description": "Analiza feedbacku klienta",
                "input": {
                    "text": "Obsługa była okropna, nikt mi nie pomógł",
                    "context": "customer_service"
                },
                "expected_output": {
                    "sentiment": "negative",
                    "confidence": 0.89,
                    "priority": "high",
                    "requires_escalation": true
                }
            }
        },
        "slack_integration": {
            "team_notification": {
                "description": "Powiadomienie zespołu o nowym zadaniu",
                "input": {
                    "channel": "#development",
                    "message": "Nowy bug zgłoszony: Problem z logowaniem użytkowników",
                    "priority": "high",
                    "attachments": ["error_log.txt"]
                },
                "expected_output": {
                    "message_sent": true,
                    "message_id": "ts_1634567890",
                    "mentions": ["@channel"]
                }
            },
            "status_update": {
                "description": "Aktualizacja statusu projektu",
                "input": {
                    "channel": "#project-alpha",
                    "message": "Milestone 2 ukończony! ✅",
                    "thread_ts": "1634567800"
                },
                "expected_output": {
                    "message_sent": true,
                    "in_thread": true
                }
            }
        },
        "conditional_router": {
            "customer_triage": {
                "description": "Routing zapytań klientów",
                "input": {
                    "customer_tier": "premium",
                    "issue_type": "billing",
                    "urgency": "high"
                },
                "expected_output": {
                    "route_to": "premium_support_team",
                    "priority": "high",
                    "sla": "2_hours"
                }
            },
            "lead_qualification": {
                "description": "Routing leadów sprzedażowych",
                "input": {
                    "budget": 50000,
                    "company_size": "enterprise",
                    "timeline": "immediate"
                },
                "expected_output": {
                    "route_to": "enterprise_sales",
                    "score": 95,
                    "follow_up": "immediate"
                }
            }
        },
        "email_composer": {
            "follow_up_email": {
                "description": "Email follow-up po spotkaniu",
                "input": {
                    "email_type": "follow_up",
                    "recipient_info": {
                        "name": "Jan Kowalski",
                        "company": "TechCorp",
                        "position": "CTO"
                    },
                    "context": "Spotkanie w sprawie implementacji systemu CRM",
                    "tone": "professional"
                },
                "expected_output": {
                    "subject": "Dziękuję za spotkanie - następne kroki",
                    "body": "Szanowny Panie Kowalski,\n\nDziękuję za czas poświęcony na dzisiejsze spotkanie...",
                    "call_to_action": "Proszę o potwierdzenie terminu kolejnego spotkania"
                }
            }
        },
        "web_scraper": {
            "competitor_pricing": {
                "description": "Scraping cen konkurencji",
                "input": {
                    "url": "https://competitor.com/pricing",
                    "selectors": {
                        "price": ".price-value",
                        "plan_name": ".plan-title"
                    },
                    "rate_limit": 1000
                },
                "expected_output": {
                    "products": [
                        {"plan": "Basic", "price": "$29/mo"},
                        {"plan": "Pro", "price": "$99/mo"}
                    ],
                    "scraped_at": "2024-01-15T10:30:00Z"
                }
            }
        },
        "data_validator": {
            "customer_data_validation": {
                "description": "Walidacja danych klienta",
                "input": {
                    "data": {
                        "email": "jan.kowalski@email.com",
                        "phone": "+48123456789",
                        "age": 25,
                        "country": "Poland"
                    },
                    "schema": {
                        "email": "email_format",
                        "phone": "phone_format",
                        "age": "min:18,max:120",
                        "country": "required"
                    }
                },
                "expected_output": {
                    "valid": true,
                    "errors": [],
                    "warnings": [],
                    "normalized_data": {
                        "email": "jan.kowalski@email.com",
                        "phone": "+48123456789",
                        "age": 25,
                        "country": "Poland"
                    }
                }
            }
        }
    }

def get_integration_guides():
    """Zwraca przewodniki integracji dla komponentów"""
    return {
        "slack_integration": {
            "setup_steps": [
                "1. Utwórz Slack App w https://api.slack.com/apps",
                "2. Dodaj OAuth Scopes: channels:read, channels:write, chat:write",
                "3. Zainstaluj aplikację w workspace",
                "4. Skopiuj Bot User OAuth Token",
                "5. Skonfiguruj token w komponencie"
            ],
            "required_permissions": [
                "channels:read",
                "channels:write", 
                "chat:write",
                "files:write"
            ],
            "testing_checklist": [
                "✓ Sprawdź połączenie z API",
                "✓ Wyślij testową wiadomość",
                "✓ Sprawdź uprawnienia do kanałów",
                "✓ Przetestuj załączniki"
            ]
        },
        "openai_api_integration": {
            "setup_steps": [
                "1. Zarejestruj się na https://platform.openai.com",
                "2. Wygeneruj API key w sekcji API Keys",
                "3. Skonfiguruj klucz w komponencie",
                "4. Wybierz odpowiedni model",
                "5. Ustaw limity usage"
            ],
            "cost_optimization": [
                "Używaj niższej temperature dla precyzyjnych odpowiedzi",
                "Ogranicz max_tokens do minimum",
                "Cachuj częste zapytania",
                "Monitoruj zużycie tokenów"
            ],
            "best_practices": [
                "Zawsze ustawiaj system prompt",
                "Waliduj wejście przed wysłaniem",
                "Obsługuj rate limiting",
                "Loguj wszystkie zapytania"
            ]
        },
        "shopify_integration": {
            "setup_steps": [
                "1. Utwórz Private App w Shopify Admin",
                "2. Wygeneruj Admin API access token", 
                "3. Skonfiguruj webhooks dla zdarzeń",
                "4. Ustaw odpowiednie uprawnienia",
                "5. Przetestuj połączenie"
            ],
            "required_permissions": [
                "read_products",
                "write_products",
                "read_orders",
                "write_orders",
                "read_customers",
                "write_customers"
            ],
            "webhook_events": [
                "orders/create",
                "orders/updated",
                "products/create",
                "products/update",
                "customers/create"
            ]
        }
    }

def get_troubleshooting_guide():
    """Zwraca przewodnik rozwiązywania problemów"""
    return {
        "common_issues": {
            "authentication_failed": {
                "description": "Błąd autoryzacji z zewnętrznym API",
                "causes": [
                    "Nieprawidłowy API key",
                    "Wygasły token",
                    "Brak uprawnień",
                    "Rate limiting"
                ],
                "solutions": [
                    "Sprawdź poprawność klucza API",
                    "Odnów token autoryzacji",
                    "Zweryfikuj uprawnienia",
                    "Zaimplementuj retry z backoff"
                ]
            },
            "slow_response_times": {
                "description": "Wolne odpowiedzi z komponentów",
                "causes": [
                    "Brak cache'owania",
                    "Nieoptymalne zapytania",
                    "Przeciążone API",
                    "Sieciowe opóźnienia"
                ],
                "solutions": [
                    "Włącz cache dla częstych zapytań",
                    "Optymalizuj zapytania",
                    "Dodaj load balancing",
                    "Zaimplementuj timeout handling"
                ]
            },
            "data_validation_errors": {
                "description": "Błędy walidacji danych",
                "causes": [
                    "Nieprawidłowy format danych",
                    "Brakujące wymagane pola",
                    "Niezgodność typów",
                    "Za duże dane"
                ],
                "solutions": [
                    "Zwaliduj dane przed przetworzeniem",
                    "Dodaj domyślne wartości",
                    "Konwertuj typy automatycznie",
                    "Zaimplementuj chunking"
                ]
            }
        },
        "debugging_steps": [
            "1. Sprawdź logi komponentów",
            "2. Zweryfikuj konfigurację",
            "3. Przetestuj połączenia", 
            "4. Sprawdź uprawnienia",
            "5. Monitoruj metryki performance",
            "6. Analizuj przepływ danych"
        ],
        "performance_optimization": {
            "caching_strategies": [
                "Cache wyniki LLM dla identycznych zapytań",
                "Używaj Redis dla szybkiego cache",
                "Implementuj TTL dla danych",
                "Cache metadata z integracji"
            ],
            "resource_management": [
                "Monitoruj zużycie CPU i RAM",
                "Optymalizuj rozmiar batchów",
                "Używaj connection pooling",
                "Implementuj graceful shutdown"
            ]
        }
    }