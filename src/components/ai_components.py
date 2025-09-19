def get_ai_components():
    """Zwraca wszystkie komponenty AI i LLM dostępne dla agentów"""
    return [
        # === MODELE JĘZYKOWE (LLM) ===
        {
            "component_id": "pollinations_llm",
            "name": "Pollinations AI (Bezpłatny)",
            "type": "ai_processing",
            "category": "text_generation",
            "description": "Bezpłatny model AI kompatybilny z OpenAI - idealny do testowania",
            "capabilities": ["text_generation", "conversation", "analysis", "reasoning"],
            "input_schema": {
                "type": "object",
                "properties": {
                    "prompt": {"type": "string", "description": "Prompt dla modelu"},
                    "system_prompt": {"type": "string", "description": "Systemowy prompt"},
                    "temperature": {"type": "number", "minimum": 0, "maximum": 2, "default": 0.7},
                    "max_tokens": {"type": "integer", "minimum": 1, "maximum": 4096, "default": 1000}
                },
                "required": ["prompt"]
            },
            "output_schema": {
                "type": "object",
                "properties": {
                    "generated_text": {"type": "string"},
                    "model_used": {"type": "string"},
                    "response_time": {"type": "number"}
                }
            },
            "default_config": {
                "api_endpoint": "https://text.pollinations.ai/openai",
                "model": "openai",
                "temperature": 0.7,
                "max_tokens": 1000,
                "system_prompt": "Jesteś pomocnym asystentem AI."
            }
        },
        {
            "component_id": "openai_gpt4",
            "name": "OpenAI GPT-4", 
            "type": "ai_processing",
            "category": "text_generation",
            "description": "Najnowszy model GPT-4 OpenAI",
            "capabilities": ["text_generation", "conversation", "code_generation", "analysis"]
        },
        {
            "component_id": "anthropic_claude",
            "name": "Anthropic Claude",
            "type": "ai_processing",
            "category": "text_generation", 
            "description": "Model Claude - doskonały w analizie i reasoning",
            "capabilities": ["analysis", "reasoning", "safety", "long_context"]
        },
        {
            "component_id": "google_gemini",
            "name": "Google Gemini",
            "type": "ai_processing",
            "category": "multimodal_ai",
            "description": "Model multimodalny Google",
            "capabilities": ["text_generation", "image_analysis", "multimodal_processing"]
        },
        {
            "component_id": "mistral_ai",
            "name": "Mistral AI",
            "type": "ai_processing",
            "category": "text_generation",
            "description": "Europejski model Mistral",
            "capabilities": ["text_generation", "multilingual", "code_generation"]
        },

        # === PRZETWARZANIE OBRAZÓW ===
        {
            "component_id": "vision_analyzer",
            "name": "Analizator Obrazów",
            "type": "ai_processing",
            "category": "vision_analysis",
            "description": "Kompleksowa analiza obrazów",
            "capabilities": ["image_description", "ocr", "object_detection", "face_recognition"]
        },
        {
            "component_id": "image_generator",
            "name": "Generator Obrazów",
            "type": "ai_processing", 
            "category": "image_generation",
            "description": "Generuje obrazy z opisów tekstowych",
            "capabilities": ["text_to_image", "image_editing", "style_transfer"]
        },

        # === AUDIO I MOWA ===
        {
            "component_id": "speech_to_text",
            "name": "Mowa na Tekst",
            "type": "ai_processing",
            "category": "audio_processing", 
            "description": "Transkrypcja audio na tekst",
            "capabilities": ["transcription", "language_detection", "speaker_identification"]
        },
        {
            "component_id": "text_to_speech",
            "name": "Tekst na Mowę",
            "type": "ai_processing",
            "category": "audio_generation",
            "description": "Synteza naturalnej mowy",
            "capabilities": ["speech_synthesis", "voice_cloning", "emotion_control"]
        },

        # === ANALIZA TEKSTU ===
        {
            "component_id": "sentiment_analyzer",
            "name": "Analizator Sentymentu",
            "type": "ai_processing",
            "category": "text_analysis",
            "description": "Wykrywa emocje i sentiment w tekście",
            "capabilities": ["sentiment_analysis", "emotion_detection", "polarity_scoring"]
        },
        {
            "component_id": "entity_extractor",
            "name": "Ekstraktor Encji",
            "type": "ai_processing",
            "category": "text_analysis",
            "description": "Wyodrębnia osoby, miejsca, organizacje z tekstu",
            "capabilities": ["named_entity_recognition", "entity_linking", "relationship_extraction"]
        },
        {
            "component_id": "keyword_extractor",
            "name": "Ekstraktor Słów Kluczowych",
            "type": "ai_processing", 
            "category": "text_analysis",
            "description": "Identyfikuje najważniejsze słowa kluczowe i frazy",
            "capabilities": ["keyword_extraction", "phrase_detection", "importance_scoring"]
        },
        {
            "component_id": "text_classifier",
            "name": "Klasyfikator Tekstu",
            "type": "ai_processing",
            "category": "classification",
            "description": "Klasyfikuje teksty do predefiniowanych kategorii",
            "capabilities": ["text_classification", "topic_modeling", "spam_detection"]
        },

        # === KONWERSACJA I DIALOG ===
        {
            "component_id": "intent_classifier",
            "name": "Klasyfikator Intencji",
            "type": "ai_processing",
            "category": "conversation",
            "description": "Rozpoznaje intencje użytkownika",
            "capabilities": ["intent_recognition", "confidence_scoring", "multi_intent_detection"]
        },
        {
            "component_id": "conversation_manager",
            "name": "Menedżer Konwersacji",
            "type": "ai_processing",
            "category": "conversation",
            "description": "Zarządza kontekstem i przepływem rozmowy",
            "capabilities": ["context_management", "turn_taking", "conversation_flow"]
        },
        {
            "component_id": "response_personalizer",
            "name": "Personalizator Odpowiedzi",
            "type": "ai_processing",
            "category": "personalization",
            "description": "Dostosowuje odpowiedzi do preferencji użytkownika",
            "capabilities": ["user_profiling", "response_adaptation", "style_matching"]
        },

        # === CONTENT I KREATYWNOŚĆ ===
        {
            "component_id": "content_generator",
            "name": "Generator Treści",
            "type": "ai_processing",
            "category": "content_creation",
            "description": "Tworzy różne rodzaje treści marketingowych",
            "capabilities": ["blog_writing", "social_media", "product_descriptions", "copywriting"]
        },
        {
            "component_id": "seo_optimizer",
            "name": "Optymalizator SEO",
            "type": "ai_processing",
            "category": "seo",
            "description": "Optymalizuje treści pod kątem SEO",
            "capabilities": ["keyword_optimization", "meta_tags", "readability_improvement"]
        },
        {
            "component_id": "social_media_manager",
            "name": "Menedżer Social Media",
            "type": "ai_processing",
            "category": "social_media",
            "description": "Zarządza treściami w social mediach",
            "capabilities": ["post_scheduling", "hashtag_optimization", "engagement_analysis"]
        },

        # === ANALIZA DANYCH ===
        {
            "component_id": "data_analyst",
            "name": "Analityk Danych",
            "type": "ai_processing",
            "category": "data_analysis", 
            "description": "Analizuje dane i wykrywa wzorce",
            "capabilities": ["statistical_analysis", "trend_detection", "anomaly_detection"]
        },
        {
            "component_id": "predictive_analyzer",
            "name": "Analizator Predykcyjny",
            "type": "ai_processing",
            "category": "prediction",
            "description": "Przewiduje trendy i przyszłe wartości",
            "capabilities": ["forecasting", "trend_prediction", "risk_modeling"]
        },

        # === BEZPIECZEŃSTWO ===
        {
            "component_id": "security_scanner",
            "name": "Skaner Bezpieczeństwa",
            "type": "ai_processing",
            "category": "security",
            "description": "Skanuje pod kątem zagrożeń bezpieczeństwa",
            "capabilities": ["vulnerability_detection", "threat_analysis", "compliance_checking"]
        },
        {
            "component_id": "fraud_detector",
            "name": "Detektor Oszustw",
            "type": "ai_processing",
            "category": "fraud_detection",
            "description": "Wykrywa podejrzane aktywności i oszustwa",
            "capabilities": ["anomaly_detection", "pattern_recognition", "risk_scoring"]
        }
    ]