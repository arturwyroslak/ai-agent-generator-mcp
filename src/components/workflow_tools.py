def get_workflow_components():
    """Zwraca komponenty logiki workflow"""
    return [
        # === KONTROLA PRZEPŁYWU ===
        {
            "component_id": "conditional_router",
            "name": "Router Warunkowy",
            "type": "workflow_control",
            "category": "control_flow",
            "description": "Kieruje przepływ na podstawie warunków",
            "capabilities": ["condition_evaluation", "branching", "multiple_paths", "default_routing"]
        },
        {
            "component_id": "loop_controller",
            "name": "Kontroler Pętli",
            "type": "workflow_control",
            "category": "iteration",
            "description": "Wykonuje pętle for, while, foreach",
            "capabilities": ["for_loops", "while_loops", "foreach_iteration", "break_continue"]
        },
        {
            "component_id": "parallel_executor",
            "name": "Wykonawca Równoległy",
            "type": "workflow_control",
            "category": "parallelization",
            "description": "Wykonuje zadania równolegle",
            "capabilities": ["parallel_processing", "thread_management", "result_aggregation", "load_balancing"]
        },
        {
            "component_id": "sequence_controller",
            "name": "Kontroler Sekwencji",
            "type": "workflow_control",
            "category": "sequencing",
            "description": "Kontroluje kolejność wykonania",
            "capabilities": ["step_ordering", "dependency_resolution", "checkpoint_recovery", "rollback"]
        },
        {
            "component_id": "decision_tree",
            "name": "Drzewo Decyzyjne",
            "type": "workflow_control",
            "category": "decision_making",
            "description": "Złożone drzewo decyzji",
            "capabilities": ["multi_level_decisions", "weighted_conditions", "probability_based", "learning"]
        },

        # === ZARZĄDZANIE STANEM ===
        {
            "component_id": "state_manager",
            "name": "Menedżer Stanu",
            "type": "workflow_control",
            "category": "state_management",
            "description": "Zarządza stanem workflow",
            "capabilities": ["state_persistence", "state_transitions", "rollback", "state_validation"]
        },
        {
            "component_id": "variable_store",
            "name": "Magazyn Zmiennych",
            "type": "workflow_control",
            "category": "data_management",
            "description": "Przechowuje zmienne workflow",
            "capabilities": ["variable_storage", "scope_management", "type_safety", "serialization"]
        },
        {
            "component_id": "context_manager",
            "name": "Menedżer Kontekstu",
            "type": "workflow_control",
            "category": "context_management",
            "description": "Zarządza kontekstem wykonania",
            "capabilities": ["context_switching", "isolation", "inheritance", "cleanup"]
        },

        # === OBSŁUGA BŁĘDÓW ===
        {
            "component_id": "error_handler",
            "name": "Obsługa Błędów",
            "type": "workflow_control",
            "category": "error_handling",
            "description": "Obsługuje błędy i wyjątki",
            "capabilities": ["exception_catching", "retry_logic", "fallback_actions", "error_reporting"]
        },
        {
            "component_id": "retry_mechanism",
            "name": "Mechanizm Powtórzeń",
            "type": "workflow_control",
            "category": "resilience",
            "description": "Automatyczne powtórzenia przy błędach",
            "capabilities": ["exponential_backoff", "retry_policies", "circuit_breaker", "jitter"]
        },
        {
            "component_id": "fallback_handler",
            "name": "Obsługa Fallback",
            "type": "workflow_control",
            "category": "resilience",
            "description": "Alternatywne ścieżki przy błędach",
            "capabilities": ["graceful_degradation", "alternative_paths", "service_fallback", "default_responses"]
        },
        {
            "component_id": "timeout_controller",
            "name": "Kontroler Timeoutów",
            "type": "workflow_control",
            "category": "timing",
            "description": "Kontroluje czasy wykonania",
            "capabilities": ["execution_timeout", "step_timeout", "timeout_actions", "time_monitoring"]
        },

        # === HARMONOGRAMOWANIE ===
        {
            "component_id": "scheduler",
            "name": "Harmonogramowiec",
            "type": "workflow_control",
            "category": "scheduling",
            "description": "Planuje wykonanie zadań",
            "capabilities": ["cron_scheduling", "interval_scheduling", "event_scheduling", "priority_queues"]
        },
        {
            "component_id": "delay_controller",
            "name": "Kontroler Opóźnień",
            "type": "workflow_control",
            "category": "timing",
            "description": "Wprowadza opóźnienia",
            "capabilities": ["fixed_delay", "variable_delay", "conditional_delay", "delay_patterns"]
        },
        {
            "component_id": "rate_limiter",
            "name": "Ogranicznik Szybkości",
            "type": "workflow_control",
            "category": "rate_limiting",
            "description": "Kontroluje szybkość wykonania",
            "capabilities": ["request_limiting", "token_bucket", "sliding_window", "adaptive_limiting"]
        },
        {
            "component_id": "batch_processor",
            "name": "Procesor Batch",
            "type": "workflow_control",
            "category": "batching",
            "description": "Grupuje zadania w batche",
            "capabilities": ["batch_collection", "size_based_batching", "time_based_batching", "batch_processing"]
        },

        # === SYNCHRONIZACJA ===
        {
            "component_id": "synchronizer",
            "name": "Synchronizator",
            "type": "workflow_control",
            "category": "synchronization",
            "description": "Synchronizuje równoległe procesy",
            "capabilities": ["barrier_synchronization", "mutex_locks", "semaphores", "condition_variables"]
        },
        {
            "component_id": "wait_condition",
            "name": "Warunek Oczekiwania",
            "type": "workflow_control",
            "category": "waiting",
            "description": "Czeka na spełnienie warunków",
            "capabilities": ["condition_waiting", "event_waiting", "polling", "notification"]
        },
        {
            "component_id": "join_controller",
            "name": "Kontroler Łączenia",
            "type": "workflow_control",
            "category": "synchronization",
            "description": "Łączy wyniki z wielu ścieżek",
            "capabilities": ["result_merging", "partial_results", "completion_detection", "aggregation"]
        },

        # === MONITOROWANIE I METRYKI ===
        {
            "component_id": "workflow_monitor",
            "name": "Monitor Workflow",
            "type": "workflow_control",
            "category": "monitoring",
            "description": "Monitoruje przebieg workflow",
            "capabilities": ["execution_tracking", "performance_metrics", "bottleneck_detection", "alerting"]
        },
        {
            "component_id": "metrics_collector",
            "name": "Kolektor Metryk",
            "type": "workflow_control",
            "category": "metrics",
            "description": "Zbiera metryki wykonania",
            "capabilities": ["timing_metrics", "throughput_metrics", "error_metrics", "custom_metrics"]
        },
        {
            "component_id": "logger",
            "name": "Logger",
            "type": "workflow_control",
            "category": "logging",
            "description": "Loguje przebieg workflow",
            "capabilities": ["structured_logging", "log_levels", "log_filtering", "log_aggregation"]
        },
        {
            "component_id": "debugger",
            "name": "Debugger",
            "type": "workflow_control",
            "category": "debugging",
            "description": "Debuguje workflow",
            "capabilities": ["breakpoints", "step_execution", "variable_inspection", "stack_trace"]
        },

        # === WALIDACJA I TESTOWANIE ===
        {
            "component_id": "validator",
            "name": "Walidator",
            "type": "workflow_control",
            "category": "validation",
            "description": "Waliduje dane i stan workflow",
            "capabilities": ["data_validation", "schema_validation", "business_rules", "constraint_checking"]
        },
        {
            "component_id": "test_runner",
            "name": "Runner Testów",
            "type": "workflow_control",
            "category": "testing",
            "description": "Uruchamia testy workflow",
            "capabilities": ["unit_testing", "integration_testing", "mock_services", "test_reporting"]
        },
        {
            "component_id": "assertion_checker",
            "name": "Sprawdzacz Asercji",
            "type": "workflow_control",
            "category": "validation",
            "description": "Sprawdza asercje w workflow",
            "capabilities": ["condition_assertions", "data_assertions", "state_assertions", "performance_assertions"]
        },

        # === TRANSFORMACJA I MAPPING ===
        {
            "component_id": "data_mapper",
            "name": "Mapper Danych",
            "type": "workflow_control",
            "category": "data_transformation",
            "description": "Mapuje dane między krokami",
            "capabilities": ["field_mapping", "type_conversion", "transformation_rules", "expression_evaluation"]
        },
        {
            "component_id": "format_converter",
            "name": "Konwerter Formatów",
            "type": "workflow_control",
            "category": "format_conversion",
            "description": "Konwertuje formaty danych",
            "capabilities": ["json_xml_conversion", "csv_json_conversion", "binary_text_conversion", "encoding_conversion"]
        },
        {
            "component_id": "aggregator",
            "name": "Agregator",
            "type": "workflow_control",
            "category": "aggregation",
            "description": "Agreguje dane z wielu źródeł",
            "capabilities": ["sum_aggregation", "count_aggregation", "average_aggregation", "custom_aggregation"]
        },
        {
            "component_id": "filter",
            "name": "Filtr",
            "type": "workflow_control",
            "category": "filtering",
            "description": "Filtruje dane przepływające przez workflow",
            "capabilities": ["condition_filtering", "pattern_filtering", "whitelist_blacklist", "dynamic_filtering"]
        },

        # === CACHE I OPTYMALIZACJA ===
        {
            "component_id": "cache_manager",
            "name": "Menedżer Cache",
            "type": "workflow_control",
            "category": "caching",
            "description": "Cachuje wyniki między krokami",
            "capabilities": ["result_caching", "ttl_management", "cache_invalidation", "cache_strategies"]
        },
        {
            "component_id": "optimizer",
            "name": "Optymalizator",
            "type": "workflow_control",
            "category": "optimization",
            "description": "Optymalizuje wykonanie workflow",
            "capabilities": ["execution_optimization", "resource_optimization", "path_optimization", "performance_tuning"]
        },
        {
            "component_id": "compressor",
            "name": "Kompresor",
            "type": "workflow_control",
            "category": "compression",
            "description": "Kompresuje dane w workflow",
            "capabilities": ["data_compression", "stream_compression", "compression_algorithms", "decompression"]
        },

        # === BEZPIECZEŃSTWO ===
        {
            "component_id": "access_controller",
            "name": "Kontroler Dostępu",
            "type": "workflow_control",
            "category": "security",
            "description": "Kontroluje dostęp do workflow",
            "capabilities": ["authentication", "authorization", "role_based_access", "permission_checking"]
        },
        {
            "component_id": "encryptor",
            "name": "Szyfrowanie",
            "type": "workflow_control",
            "category": "security",
            "description": "Szyfruje dane w workflow",
            "capabilities": ["data_encryption", "key_management", "encryption_algorithms", "decryption"]
        },
        {
            "component_id": "audit_trail",
            "name": "Ścieżka Audytu",
            "type": "workflow_control",
            "category": "auditing",
            "description": "Prowadzi ścieżkę audytu",
            "capabilities": ["action_logging", "change_tracking", "compliance_reporting", "audit_analysis"]
        },

        # === INTEGRACJA I KOMUNIKACJA ===
        {
            "component_id": "webhook_handler",
            "name": "Obsługa Webhooków",
            "type": "workflow_control",
            "category": "integration",
            "description": "Obsługuje webhook i na zewnątrz",
            "capabilities": ["webhook_receiving", "webhook_sending", "signature_verification", "retry_handling"]
        },
        {
            "component_id": "event_emitter",
            "name": "Emiter Zdarzeń",
            "type": "workflow_control",
            "category": "events",
            "description": "Emituje zdarzenia z workflow",
            "capabilities": ["event_publishing", "event_routing", "event_filtering", "event_transformation"]
        },
        {
            "component_id": "notification_sender",
            "name": "Wysyłacz Powiadomień",
            "type": "workflow_control",
            "category": "notifications",
            "description": "Wysyła powiadomienia o statusie",
            "capabilities": ["email_notifications", "sms_notifications", "push_notifications", "webhook_notifications"]
        },
        {
            "component_id": "api_gateway",
            "name": "API Gateway",
            "type": "workflow_control",
            "category": "api_management",
            "description": "Zarządza dostępem do workflow przez API",
            "capabilities": ["request_routing", "rate_limiting", "authentication", "response_transformation"]
        }
    ]