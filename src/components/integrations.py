def get_integration_components():
    """Zwraca wszystkie komponenty integracji dostępne dla agentów"""
    return [
        # === KOMUNIKACJA I WIADOMOŚCI ===
        {
            "component_id": "slack_integration",
            "name": "Slack",
            "type": "integration",
            "category": "communication",
            "description": "Integracja z Slack - wiadomości, kanały, powiadomienia",
            "capabilities": ["send_message", "create_channel", "get_messages", "upload_file", "manage_users"],
            "auth_config": {"type": "oauth2", "scopes": ["channels:read", "channels:write", "chat:write"]},
            "platforms": ["Slack"]
        },
        {
            "component_id": "discord_integration",
            "name": "Discord", 
            "type": "integration",
            "category": "communication",
            "description": "Integracja z Discord - boty, serwery, głos",
            "capabilities": ["send_message", "create_channel", "manage_roles", "voice_actions"],
            "platforms": ["Discord"]
        },
        {
            "component_id": "telegram_integration",
            "name": "Telegram",
            "type": "integration",
            "category": "communication",
            "description": "Telegram Bot API - wiadomości, grupy, pliki",
            "capabilities": ["send_message", "handle_commands", "file_upload", "inline_keyboards"],
            "platforms": ["Telegram"]
        },
        {
            "component_id": "whatsapp_integration",
            "name": "WhatsApp Business",
            "type": "integration",
            "category": "communication",
            "description": "WhatsApp Business API",
            "capabilities": ["send_message", "send_media", "handle_webhooks", "message_templates"],
            "platforms": ["WhatsApp"]
        },
        {
            "component_id": "teams_integration",
            "name": "Microsoft Teams",
            "type": "integration",
            "category": "communication",
            "description": "Microsoft Teams - czat, spotkania, aplikacje",
            "capabilities": ["send_message", "create_meeting", "manage_channels", "adaptive_cards"],
            "platforms": ["Microsoft Teams"]
        },

        # === EMAIL I NEWSLETTER ===
        {
            "component_id": "gmail_integration",
            "name": "Gmail",
            "type": "integration",
            "category": "email",
            "description": "Integracja z Gmail - wysyłanie, odbieranie, filtrowanie",
            "capabilities": ["send_email", "read_email", "search_email", "manage_labels"],
            "platforms": ["Gmail"]
        },
        {
            "component_id": "outlook_integration",
            "name": "Outlook",
            "type": "integration",
            "category": "email",
            "description": "Microsoft Outlook i Exchange",
            "capabilities": ["send_email", "calendar_management", "contact_sync", "task_management"],
            "platforms": ["Outlook"]
        },
        {
            "component_id": "sendgrid_integration",
            "name": "SendGrid",
            "type": "integration",
            "category": "email",
            "description": "SendGrid - masowe wysyłanie emaili",
            "capabilities": ["bulk_email", "template_management", "analytics", "bounce_handling"],
            "platforms": ["SendGrid"]
        },
        {
            "component_id": "mailchimp_integration",
            "name": "Mailchimp",
            "type": "integration",
            "category": "email_marketing",
            "description": "Mailchimp - email marketing i automatyzacja",
            "capabilities": ["campaign_management", "audience_segmentation", "automation", "analytics"],
            "platforms": ["Mailchimp"]
        },

        # === CRM I SPRZEDAŻ ===
        {
            "component_id": "salesforce_integration",
            "name": "Salesforce",
            "type": "integration", 
            "category": "crm",
            "description": "Salesforce CRM - leady, kontakty, możliwości",
            "capabilities": ["lead_management", "opportunity_management", "account_management", "custom_objects"],
            "platforms": ["Salesforce"]
        },
        {
            "component_id": "hubspot_integration",
            "name": "HubSpot",
            "type": "integration",
            "category": "crm",
            "description": "HubSpot CRM i Marketing Hub",
            "capabilities": ["contact_management", "deal_pipeline", "marketing_automation", "analytics"],
            "platforms": ["HubSpot"]
        },
        {
            "component_id": "pipedrive_integration",
            "name": "Pipedrive",
            "type": "integration",
            "category": "crm",
            "description": "Pipedrive CRM - pipeline sprzedaży",
            "capabilities": ["deal_management", "pipeline_tracking", "activity_logging", "reporting"],
            "platforms": ["Pipedrive"]
        },
        {
            "component_id": "freshsales_integration",
            "name": "Freshsales",
            "type": "integration",
            "category": "crm",
            "description": "Freshworks CRM",
            "capabilities": ["lead_scoring", "contact_management", "email_tracking", "workflow_automation"],
            "platforms": ["Freshsales"]
        },

        # === ZARZĄDZANIE PROJEKTAMI ===
        {
            "component_id": "jira_integration",
            "name": "Jira",
            "type": "integration",
            "category": "project_management",
            "description": "Atlassian Jira - zarządzanie projektami i zagadnieniami",
            "capabilities": ["issue_management", "project_tracking", "workflow_automation", "reporting"],
            "platforms": ["Jira"]
        },
        {
            "component_id": "asana_integration",
            "name": "Asana",
            "type": "integration",
            "category": "project_management", 
            "description": "Asana - zadania, projekty, zespoły",
            "capabilities": ["task_management", "project_organization", "team_collaboration", "progress_tracking"],
            "platforms": ["Asana"]
        },
        {
            "component_id": "trello_integration",
            "name": "Trello",
            "type": "integration",
            "category": "project_management",
            "description": "Trello - tablice Kanban",
            "capabilities": ["board_management", "card_automation", "checklist_management", "team_collaboration"],
            "platforms": ["Trello"]
        },
        {
            "component_id": "notion_integration",
            "name": "Notion",
            "type": "integration",
            "category": "productivity",
            "description": "Notion - dokumenty, bazy danych, wiki",
            "capabilities": ["page_management", "database_operations", "block_manipulation", "collaboration"],
            "platforms": ["Notion"]
        },
        {
            "component_id": "monday_integration",
            "name": "Monday.com",
            "type": "integration",
            "category": "project_management",
            "description": "Monday.com - platforma pracy zespołowej",
            "capabilities": ["board_management", "item_tracking", "automation", "reporting"],
            "platforms": ["Monday.com"]
        },

        # === ROZWÓJ I KOD ===
        {
            "component_id": "github_integration",
            "name": "GitHub",
            "type": "integration",
            "category": "development",
            "description": "GitHub - repozytoria, pull requesty, issues",
            "capabilities": ["repository_management", "pull_request_automation", "issue_tracking", "ci_cd_integration"],
            "platforms": ["GitHub"]
        },
        {
            "component_id": "gitlab_integration",
            "name": "GitLab",
            "type": "integration",
            "category": "development",
            "description": "GitLab - DevOps platform",
            "capabilities": ["repository_management", "ci_cd_pipelines", "issue_management", "deployment_tracking"],
            "platforms": ["GitLab"]
        },
        {
            "component_id": "bitbucket_integration",
            "name": "Bitbucket",
            "type": "integration",
            "category": "development",
            "description": "Atlassian Bitbucket",
            "capabilities": ["repository_management", "pipeline_automation", "code_review", "deployment_management"],
            "platforms": ["Bitbucket"]
        },
        {
            "component_id": "jenkins_integration",
            "name": "Jenkins",
            "type": "integration",
            "category": "ci_cd",
            "description": "Jenkins CI/CD",
            "capabilities": ["build_automation", "pipeline_management", "deployment_automation", "test_execution"],
            "platforms": ["Jenkins"]
        },

        # === PŁATNOŚCI I FINANSE ===
        {
            "component_id": "stripe_integration",
            "name": "Stripe",
            "type": "integration",
            "category": "payment",
            "description": "Stripe - płatności online",
            "capabilities": ["payment_processing", "subscription_management", "invoice_management", "fraud_detection"],
            "platforms": ["Stripe"]
        },
        {
            "component_id": "paypal_integration",
            "name": "PayPal",
            "type": "integration",
            "category": "payment",
            "description": "PayPal - płatności globalne",
            "capabilities": ["payment_processing", "money_transfer", "invoice_creation", "dispute_management"],
            "platforms": ["PayPal"]
        },
        {
            "component_id": "square_integration",
            "name": "Square",
            "type": "integration",
            "category": "payment",
            "description": "Square - płatności i sprzedaż",
            "capabilities": ["payment_processing", "inventory_management", "customer_management", "analytics"],
            "platforms": ["Square"]
        },
        {
            "component_id": "quickbooks_integration",
            "name": "QuickBooks",
            "type": "integration",
            "category": "accounting",
            "description": "QuickBooks - księgowość i finanse",
            "capabilities": ["invoice_management", "expense_tracking", "financial_reporting", "tax_preparation"],
            "platforms": ["QuickBooks"]
        },

        # === E-COMMERCE ===
        {
            "component_id": "shopify_integration",
            "name": "Shopify",
            "type": "integration",
            "category": "ecommerce",
            "description": "Shopify - sklep internetowy",
            "capabilities": ["product_management", "order_processing", "inventory_sync", "customer_management"],
            "platforms": ["Shopify"]
        },
        {
            "component_id": "woocommerce_integration",
            "name": "WooCommerce",
            "type": "integration",
            "category": "ecommerce",
            "description": "WooCommerce - WordPress e-commerce",
            "capabilities": ["product_sync", "order_management", "customer_data", "reporting"],
            "platforms": ["WooCommerce"]
        },
        {
            "component_id": "magento_integration",
            "name": "Magento",
            "type": "integration",
            "category": "ecommerce",
            "description": "Adobe Magento Commerce",
            "capabilities": ["catalog_management", "order_processing", "customer_segmentation", "marketing_automation"],
            "platforms": ["Magento"]
        },
        {
            "component_id": "amazon_integration",
            "name": "Amazon",
            "type": "integration",
            "category": "marketplace",
            "description": "Amazon Marketplace i AWS",
            "capabilities": ["product_listing", "order_fulfillment", "inventory_management", "advertising"],
            "platforms": ["Amazon"]
        },

        # === SOCIAL MEDIA ===
        {
            "component_id": "facebook_integration",
            "name": "Facebook",
            "type": "integration",
            "category": "social_media",
            "description": "Facebook - strony, posty, reklamy",
            "capabilities": ["page_management", "post_publishing", "ad_management", "insights_analytics"],
            "platforms": ["Facebook"]
        },
        {
            "component_id": "instagram_integration",
            "name": "Instagram",
            "type": "integration",
            "category": "social_media",
            "description": "Instagram Business - posty, stories, reklamy",
            "capabilities": ["media_publishing", "story_management", "hashtag_research", "analytics"],
            "platforms": ["Instagram"]
        },
        {
            "component_id": "twitter_integration",
            "name": "Twitter/X",
            "type": "integration",
            "category": "social_media",
            "description": "Twitter/X - tweety, engagement, analityka",
            "capabilities": ["tweet_publishing", "engagement_tracking", "trend_monitoring", "dm_management"],
            "platforms": ["Twitter"]
        },
        {
            "component_id": "linkedin_integration",
            "name": "LinkedIn",
            "type": "integration",
            "category": "social_media",
            "description": "LinkedIn - networking biznesowy",
            "capabilities": ["content_publishing", "lead_generation", "company_page_management", "recruitment"],
            "platforms": ["LinkedIn"]
        },
        {
            "component_id": "youtube_integration",
            "name": "YouTube",
            "type": "integration",
            "category": "video_platform",
            "description": "YouTube - wideo, kanały, analityka",
            "capabilities": ["video_upload", "channel_management", "comment_moderation", "analytics"],
            "platforms": ["YouTube"]
        },
        {
            "component_id": "tiktok_integration",
            "name": "TikTok",
            "type": "integration",
            "category": "social_media",
            "description": "TikTok Business - krótkie wideo",
            "capabilities": ["video_publishing", "trend_analysis", "hashtag_research", "performance_tracking"],
            "platforms": ["TikTok"]
        },

        # === ANALITYKA I MONITOROWANIE ===
        {
            "component_id": "google_analytics_integration",
            "name": "Google Analytics",
            "type": "integration",
            "category": "analytics",
            "description": "Google Analytics - analityka stron",
            "capabilities": ["traffic_analysis", "conversion_tracking", "audience_insights", "custom_reporting"],
            "platforms": ["Google Analytics"]
        },
        {
            "component_id": "google_ads_integration",
            "name": "Google Ads",
            "type": "integration",
            "category": "advertising",
            "description": "Google Ads - reklamy wyszukiwania",
            "capabilities": ["campaign_management", "keyword_bidding", "performance_tracking", "audience_targeting"],
            "platforms": ["Google Ads"]
        },
        {
            "component_id": "mixpanel_integration",
            "name": "Mixpanel",
            "type": "integration",
            "category": "analytics",
            "description": "Mixpanel - product analytics",
            "capabilities": ["event_tracking", "user_behavior", "funnel_analysis", "cohort_analysis"],
            "platforms": ["Mixpanel"]
        },
        {
            "component_id": "amplitude_integration",
            "name": "Amplitude",
            "type": "integration",
            "category": "analytics",
            "description": "Amplitude - digital analytics",
            "capabilities": ["behavioral_analysis", "user_journey", "retention_analysis", "experimentation"],
            "platforms": ["Amplitude"]
        },

        # === CHMURA I HOSTING ===
        {
            "component_id": "aws_integration",
            "name": "Amazon Web Services",
            "type": "integration",
            "category": "cloud_platform",
            "description": "AWS - usługi chmurowe",
            "capabilities": ["ec2_management", "s3_storage", "lambda_functions", "rds_databases"],
            "platforms": ["AWS"]
        },
        {
            "component_id": "azure_integration",
            "name": "Microsoft Azure",
            "type": "integration",
            "category": "cloud_platform",
            "description": "Azure - platforma chmurowa Microsoft",
            "capabilities": ["vm_management", "storage_accounts", "azure_functions", "cognitive_services"],
            "platforms": ["Azure"]
        },
        {
            "component_id": "gcp_integration",
            "name": "Google Cloud Platform",
            "type": "integration",
            "category": "cloud_platform",
            "description": "GCP - usługi chmurowe Google",
            "capabilities": ["compute_engine", "cloud_storage", "cloud_functions", "ai_ml_services"],
            "platforms": ["Google Cloud"]
        },
        {
            "component_id": "vercel_integration",
            "name": "Vercel",
            "type": "integration",
            "category": "hosting",
            "description": "Vercel - hosting dla aplikacji frontend",
            "capabilities": ["deployment_automation", "domain_management", "analytics", "edge_functions"],
            "platforms": ["Vercel"]
        },
        {
            "component_id": "netlify_integration",
            "name": "Netlify",
            "type": "integration",
            "category": "hosting",
            "description": "Netlify - hosting i CI/CD",
            "capabilities": ["site_deployment", "form_handling", "function_hosting", "a_b_testing"],
            "platforms": ["Netlify"]
        },

        # === BAZY DANYCH ===
        {
            "component_id": "airtable_integration",
            "name": "Airtable",
            "type": "integration",
            "category": "database",
            "description": "Airtable - baza danych w chmurze",
            "capabilities": ["record_management", "table_operations", "view_filtering", "automation"],
            "platforms": ["Airtable"]
        },
        {
            "component_id": "supabase_integration",
            "name": "Supabase",
            "type": "integration",
            "category": "database",
            "description": "Supabase - PostgreSQL w chmurze",
            "capabilities": ["database_operations", "realtime_subscriptions", "authentication", "storage"],
            "platforms": ["Supabase"]
        },
        {
            "component_id": "firebase_integration",
            "name": "Firebase",
            "type": "integration",
            "category": "database",
            "description": "Google Firebase - backend w chmurze",
            "capabilities": ["firestore_database", "realtime_database", "authentication", "cloud_messaging"],
            "platforms": ["Firebase"]
        },

        # === AUTOMATYZACJA ===
        {
            "component_id": "zapier_integration",
            "name": "Zapier",
            "type": "integration",
            "category": "automation",
            "description": "Zapier - automatyzacja między aplikacjami",
            "capabilities": ["workflow_automation", "trigger_management", "multi_step_zaps", "webhook_handling"],
            "platforms": ["Zapier"]
        },
        {
            "component_id": "make_integration",
            "name": "Make (Integromat)",
            "type": "integration",
            "category": "automation",
            "description": "Make - zaawansowana automatyzacja",
            "capabilities": ["visual_automation", "conditional_logic", "data_transformation", "error_handling"],
            "platforms": ["Make"]
        },
        {
            "component_id": "ifttt_integration",
            "name": "IFTTT",
            "type": "integration",
            "category": "automation",
            "description": "IFTTT - If This Then That",
            "capabilities": ["simple_automation", "trigger_action", "service_connection", "location_based"],
            "platforms": ["IFTTT"]
        },

        # === NARZĘDZIA BIZNESOWE ===
        {
            "component_id": "typeform_integration",
            "name": "Typeform",
            "type": "integration",
            "category": "forms",
            "description": "Typeform - interaktywne formularze",
            "capabilities": ["form_creation", "response_collection", "conditional_logic", "webhook_integration"],
            "platforms": ["Typeform"]
        },
        {
            "component_id": "calendly_integration",
            "name": "Calendly",
            "type": "integration",
            "category": "scheduling",
            "description": "Calendly - planowanie spotkań",
            "capabilities": ["meeting_scheduling", "availability_management", "calendar_sync", "reminder_automation"],
            "platforms": ["Calendly"]
        },
        {
            "component_id": "zoom_integration",
            "name": "Zoom",
            "type": "integration",
            "category": "video_conferencing",
            "description": "Zoom - wideokonferencje",
            "capabilities": ["meeting_creation", "participant_management", "recording_access", "webinar_hosting"],
            "platforms": ["Zoom"]
        },
        {
            "component_id": "intercom_integration",
            "name": "Intercom",
            "type": "integration",
            "category": "customer_support",
            "description": "Intercom - obsługa klienta",
            "capabilities": ["live_chat", "ticket_management", "user_messaging", "automation_bots"],
            "platforms": ["Intercom"]
        },
        {
            "component_id": "zendesk_integration",
            "name": "Zendesk",
            "type": "integration",
            "category": "customer_support",
            "description": "Zendesk - help desk",
            "capabilities": ["ticket_management", "knowledge_base", "customer_communication", "reporting"],
            "platforms": ["Zendesk"]
        },

        # === SPECJALISTYCZNE ===
        {
            "component_id": "openai_api_integration",
            "name": "OpenAI API",
            "type": "integration",
            "category": "ai_services",
            "description": "OpenAI API - modele językowe i AI",
            "capabilities": ["text_generation", "image_generation", "embeddings", "fine_tuning"],
            "platforms": ["OpenAI"]
        },
        {
            "component_id": "huggingface_integration",
            "name": "Hugging Face",
            "type": "integration",
            "category": "ai_services",
            "description": "Hugging Face - modele ML i NLP",
            "capabilities": ["model_inference", "dataset_access", "model_hosting", "transformers"],
            "platforms": ["Hugging Face"]
        },
        {
            "component_id": "twilio_integration",
            "name": "Twilio",
            "type": "integration",
            "category": "communication",
            "description": "Twilio - SMS, głos, wideo",
            "capabilities": ["sms_messaging", "voice_calls", "video_calls", "phone_verification"],
            "platforms": ["Twilio"]
        }
    ]