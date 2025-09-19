def get_data_components():
    """Zwraca wszystkie komponenty przetwarzania danych"""
    return [
        # === BAZY DANYCH ===
        {
            "component_id": "postgresql_connector",
            "name": "PostgreSQL",
            "type": "data_storage",
            "category": "database",
            "description": "Konektor do bazy PostgreSQL",
            "capabilities": ["sql_query", "data_insert", "transaction_management", "connection_pooling"]
        },
        {
            "component_id": "mysql_connector",
            "name": "MySQL",
            "type": "data_storage",
            "category": "database",
            "description": "Konektor do bazy MySQL/MariaDB",
            "capabilities": ["sql_query", "data_insert", "stored_procedures", "replication_support"]
        },
        {
            "component_id": "mongodb_connector",
            "name": "MongoDB",
            "type": "data_storage",
            "category": "nosql_database",
            "description": "Konektor do MongoDB",
            "capabilities": ["document_operations", "aggregation_pipeline", "indexing", "sharding_support"]
        },
        {
            "component_id": "redis_connector",
            "name": "Redis",
            "type": "data_storage",
            "category": "cache_database",
            "description": "Redis - cache i struktura danych",
            "capabilities": ["key_value_storage", "pub_sub", "lua_scripting", "clustering"]
        },
        {
            "component_id": "elasticsearch_connector",
            "name": "Elasticsearch",
            "type": "data_storage",
            "category": "search_engine",
            "description": "Elasticsearch - wyszukiwanie i analityka",
            "capabilities": ["full_text_search", "aggregations", "real_time_indexing", "clustering"]
        },
        {
            "component_id": "sqlite_connector",
            "name": "SQLite",
            "type": "data_storage",
            "category": "embedded_database",
            "description": "SQLite - lekka baza danych",
            "capabilities": ["embedded_sql", "file_based", "acid_compliance", "backup_restore"]
        },

        # === BAZY WEKTOROWE ===
        {
            "component_id": "pinecone_vector_db",
            "name": "Pinecone",
            "type": "data_storage",
            "category": "vector_database",
            "description": "Pinecone - managed vector database",
            "capabilities": ["vector_similarity_search", "metadata_filtering", "real_time_updates", "scaling"]
        },
        {
            "component_id": "weaviate_vector_db",
            "name": "Weaviate",
            "type": "data_storage",
            "category": "vector_database",
            "description": "Weaviate - open source vector database",
            "capabilities": ["semantic_search", "hybrid_search", "auto_vectorization", "graph_capabilities"]
        },
        {
            "component_id": "chroma_vector_db",
            "name": "Chroma",
            "type": "data_storage",
            "category": "vector_database",
            "description": "Chroma - embedding database",
            "capabilities": ["embedding_storage", "similarity_search", "metadata_queries", "persistence"]
        },
        {
            "component_id": "qdrant_vector_db",
            "name": "Qdrant",
            "type": "data_storage",
            "category": "vector_database",
            "description": "Qdrant - vector similarity engine",
            "capabilities": ["vector_search", "payload_filtering", "clustering", "quantization"]
        },

        # === PRZETWARZANIE PLIKÓW ===
        {
            "component_id": "pdf_processor",
            "name": "Procesor PDF",
            "type": "data_processing",
            "category": "document_processing",
            "description": "Przetwarzanie dokumentów PDF",
            "capabilities": ["text_extraction", "image_extraction", "metadata_parsing", "table_extraction"]
        },
        {
            "component_id": "excel_processor",
            "name": "Procesor Excel",
            "type": "data_processing",
            "category": "spreadsheet_processing",
            "description": "Przetwarzanie arkuszy Excel",
            "capabilities": ["sheet_reading", "data_validation", "formula_evaluation", "chart_extraction"]
        },
        {
            "component_id": "csv_processor",
            "name": "Procesor CSV",
            "type": "data_processing",
            "category": "data_format",
            "description": "Przetwarzanie plików CSV",
            "capabilities": ["delimiter_detection", "encoding_handling", "data_cleaning", "schema_inference"]
        },
        {
            "component_id": "json_processor",
            "name": "Procesor JSON",
            "type": "data_processing",
            "category": "data_format",
            "description": "Przetwarzanie danych JSON",
            "capabilities": ["json_parsing", "schema_validation", "path_querying", "transformation"]
        },
        {
            "component_id": "xml_processor",
            "name": "Procesor XML",
            "type": "data_processing",
            "category": "data_format",
            "description": "Przetwarzanie dokumentów XML",
            "capabilities": ["xml_parsing", "xpath_queries", "schema_validation", "xslt_transformation"]
        },
        {
            "component_id": "image_processor",
            "name": "Procesor Obrazów",
            "type": "data_processing",
            "category": "image_processing",
            "description": "Przetwarzanie plików graficznych",
            "capabilities": ["format_conversion", "resize_crop", "metadata_extraction", "compression"]
        },
        {
            "component_id": "audio_processor",
            "name": "Procesor Audio",
            "type": "data_processing",
            "category": "audio_processing",
            "description": "Przetwarzanie plików audio",
            "capabilities": ["format_conversion", "noise_reduction", "feature_extraction", "transcoding"]
        },
        {
            "component_id": "video_processor",
            "name": "Procesor Wideo",
            "type": "data_processing",
            "category": "video_processing",
            "description": "Przetwarzanie plików wideo",
            "capabilities": ["frame_extraction", "format_conversion", "compression", "thumbnail_generation"]
        },

        # === WEB SCRAPING ===
        {
            "component_id": "web_scraper",
            "name": "Web Scraper",
            "type": "data_extraction",
            "category": "web_scraping",
            "description": "Ekstraktuje dane ze stron internetowych",
            "capabilities": ["html_parsing", "javascript_rendering", "form_interaction", "proxy_support"]
        },
        {
            "component_id": "selenium_scraper",
            "name": "Selenium Scraper",
            "type": "data_extraction",
            "category": "browser_automation",
            "description": "Scraping z pełną automatyzacją przeglądarki",
            "capabilities": ["browser_automation", "javascript_execution", "screenshot_capture", "file_download"]
        },
        {
            "component_id": "api_scraper",
            "name": "API Scraper",
            "type": "data_extraction",
            "category": "api_integration",
            "description": "Pobiera dane z API zewnętrznych",
            "capabilities": ["rest_api_calls", "graphql_queries", "authentication_handling", "rate_limiting"]
        },
        {
            "component_id": "rss_scraper",
            "name": "RSS/Atom Scraper",
            "type": "data_extraction",
            "category": "feed_processing",
            "description": "Pobiera dane z feedów RSS/Atom",
            "capabilities": ["feed_parsing", "item_deduplication", "content_extraction", "change_detection"]
        },

        # === TRANSFORMACJA DANYCH ===
        {
            "component_id": "data_transformer",
            "name": "Transformator Danych",
            "type": "data_processing",
            "category": "etl",
            "description": "Przekształca i manipuluje strukturami danych",
            "capabilities": ["data_mapping", "field_transformation", "aggregation", "filtering"]
        },
        {
            "component_id": "data_validator",
            "name": "Walidator Danych",
            "type": "data_processing",
            "category": "data_quality",
            "description": "Sprawdza jakość i poprawność danych",
            "capabilities": ["schema_validation", "constraint_checking", "anomaly_detection", "data_profiling"]
        },
        {
            "component_id": "data_cleaner",
            "name": "Czyszczenie Danych",
            "type": "data_processing",
            "category": "data_preparation",
            "description": "Czyści i normalizuje dane",
            "capabilities": ["null_handling", "duplicate_removal", "outlier_detection", "standardization"]
        },
        {
            "component_id": "data_enricher",
            "name": "Wzbogacacz Danych",
            "type": "data_processing",
            "category": "data_enhancement",
            "description": "Wzbogaca dane o dodatkowe informacje",
            "capabilities": ["external_data_lookup", "geocoding", "entity_resolution", "classification"]
        },
        {
            "component_id": "data_aggregator",
            "name": "Agregator Danych",
            "type": "data_processing",
            "category": "analytics",
            "description": "Agreguje i podsumowuje dane",
            "capabilities": ["grouping", "statistical_functions", "time_series_aggregation", "window_functions"]
        },

        # === CHMURA I STORAGE ===
        {
            "component_id": "s3_storage",
            "name": "Amazon S3",
            "type": "data_storage",
            "category": "cloud_storage",
            "description": "Amazon S3 object storage",
            "capabilities": ["file_upload", "file_download", "bucket_management", "lifecycle_policies"]
        },
        {
            "component_id": "gcs_storage",
            "name": "Google Cloud Storage",
            "type": "data_storage",
            "category": "cloud_storage",
            "description": "Google Cloud Storage",
            "capabilities": ["object_operations", "bucket_management", "access_control", "versioning"]
        },
        {
            "component_id": "azure_blob_storage",
            "name": "Azure Blob Storage",
            "type": "data_storage",
            "category": "cloud_storage",
            "description": "Microsoft Azure Blob Storage",
            "capabilities": ["blob_operations", "container_management", "access_tiers", "encryption"]
        },
        {
            "component_id": "dropbox_storage",
            "name": "Dropbox",
            "type": "data_storage",
            "category": "file_storage",
            "description": "Dropbox file storage",
            "capabilities": ["file_sync", "sharing", "version_history", "collaboration"]
        },
        {
            "component_id": "google_drive_storage",
            "name": "Google Drive",
            "type": "data_storage",
            "category": "file_storage",
            "description": "Google Drive storage",
            "capabilities": ["file_management", "sharing", "collaboration", "real_time_editing"]
        },

        # === CACHE I MESSAGING ===
        {
            "component_id": "memcached_cache",
            "name": "Memcached",
            "type": "data_storage",
            "category": "cache",
            "description": "Memcached distributed caching",
            "capabilities": ["key_value_cache", "expiration_handling", "clustering", "statistics"]
        },
        {
            "component_id": "rabbitmq_queue",
            "name": "RabbitMQ",
            "type": "data_processing",
            "category": "message_queue",
            "description": "RabbitMQ message broker",
            "capabilities": ["message_queuing", "routing", "clustering", "management"]
        },
        {
            "component_id": "kafka_streaming",
            "name": "Apache Kafka",
            "type": "data_processing",
            "category": "streaming",
            "description": "Apache Kafka streaming platform",
            "capabilities": ["stream_processing", "partitioning", "replication", "connect_ecosystem"]
        },
        {
            "component_id": "sqs_queue",
            "name": "Amazon SQS",
            "type": "data_processing",
            "category": "message_queue",
            "description": "Amazon Simple Queue Service",
            "capabilities": ["message_queuing", "dead_letter_queues", "visibility_timeout", "batch_operations"]
        },

        # === ANALITYKA I BI ===
        {
            "component_id": "pandas_analyzer",
            "name": "Pandas Analyzer",
            "type": "data_processing",
            "category": "data_analysis",
            "description": "Analiza danych z Pandas",
            "capabilities": ["dataframe_operations", "statistical_analysis", "data_visualization", "time_series"]
        },
        {
            "component_id": "numpy_processor",
            "name": "NumPy Processor",
            "type": "data_processing",
            "category": "numerical_computing",
            "description": "Obliczenia numeryczne z NumPy",
            "capabilities": ["array_operations", "mathematical_functions", "linear_algebra", "fft"]
        },
        {
            "component_id": "spark_processor",
            "name": "Apache Spark",
            "type": "data_processing",
            "category": "big_data",
            "description": "Apache Spark big data processing",
            "capabilities": ["distributed_computing", "sql_queries", "streaming", "machine_learning"]
        },
        {
            "component_id": "tableau_connector",
            "name": "Tableau",
            "type": "data_processing",
            "category": "visualization",
            "description": "Tableau data visualization",
            "capabilities": ["dashboard_creation", "data_connection", "visualization", "publishing"]
        },
        {
            "component_id": "powerbi_connector",
            "name": "Power BI",
            "type": "data_processing",
            "category": "business_intelligence",
            "description": "Microsoft Power BI",
            "capabilities": ["report_creation", "data_modeling", "dashboard_sharing", "real_time_data"]
        },

        # === SECURITY I COMPLIANCE ===
        {
            "component_id": "data_encryptor",
            "name": "Szyfrowanie Danych",
            "type": "data_processing",
            "category": "security",
            "description": "Szyfrowanie i deszyfrowanie danych",
            "capabilities": ["aes_encryption", "key_management", "digital_signatures", "hashing"]
        },
        {
            "component_id": "data_anonymizer",
            "name": "Anonimizacja Danych",
            "type": "data_processing",
            "category": "privacy",
            "description": "Anonimizacja danych osobowych",
            "capabilities": ["pii_detection", "masking", "tokenization", "differential_privacy"]
        },
        {
            "component_id": "gdpr_compliance",
            "name": "GDPR Compliance",
            "type": "data_processing",
            "category": "compliance",
            "description": "Narzędzia zgodności z GDPR",
            "capabilities": ["consent_management", "data_mapping", "right_to_erasure", "audit_logging"]
        },

        # === BACKUP I RECOVERY ===
        {
            "component_id": "backup_manager",
            "name": "Menedżer Backupów",
            "type": "data_storage",
            "category": "backup",
            "description": "Zarządzanie kopiami zapasowymi",
            "capabilities": ["scheduled_backups", "incremental_backup", "compression", "encryption"]
        },
        {
            "component_id": "disaster_recovery",
            "name": "Disaster Recovery",
            "type": "data_storage",
            "category": "recovery",
            "description": "Odzyskiwanie po awarii",
            "capabilities": ["failover", "replication", "recovery_testing", "rto_rpo_monitoring"]
        },

        # === MONITORING I LOGGING ===
        {
            "component_id": "data_monitor",
            "name": "Monitor Danych",
            "type": "data_processing",
            "category": "monitoring",
            "description": "Monitorowanie jakości i przepływu danych",
            "capabilities": ["data_quality_metrics", "lineage_tracking", "alerting", "dashboard"]
        },
        {
            "component_id": "audit_logger",
            "name": "Logger Audytu",
            "type": "data_processing",
            "category": "logging",
            "description": "Logowanie dostępu do danych",
            "capabilities": ["access_logging", "change_tracking", "compliance_reporting", "retention_policies"]
        }
    ]