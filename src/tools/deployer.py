import json
import uuid
import base64
from typing import Dict, Any
from datetime import datetime

class AgentDeployer:
    def __init__(self):
        self.deployments = {}
        
    async def generate_chat_interface(self, agent_id: str, theme: str = "modern") -> Dict[str, Any]:
        """Generuje interfejs chatu HTML z zaawansowanymi funkcjami specjalnymi dla różnych typów agentów"""
        
        # Try to get agent details to customize interface
        agent_name = f"Agent {agent_id[:8]}"
        agent_type = "general"
        agent_description = "Inteligentny asystent AI"
        
        try:
            # Access the enhanced agent manager through the class variable if available
            from .enhanced_agent_manager import EnhancedAgentManager
            temp_manager = EnhancedAgentManager()
            if agent_id in temp_manager.agents:
                agent = temp_manager.agents[agent_id]
                agent_name = agent.get("name", agent_name)
                agent_type = agent.get("domain", "general")
                agent_description = agent.get("description", agent_description)
        except Exception as e:
            print(f"⚠️ Could not access agent details: {e}")
            pass
        
        # Customize interface based on agent type
        specialized_features = self._get_specialized_features(agent_type)
        custom_responses = self._get_custom_responses(agent_type)
        
        html_content = f"""<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat Interface - {agent_name}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .chat-container {{ 
            width: 90%;
            max-width: 800px;
            height: 90vh;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }}
        .chat-header {{
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 20px 20px 0 0;
        }}
        .chat-header h1 {{ font-size: 1.5em; margin-bottom: 5px; }}
        .chat-header p {{ opacity: 0.9; font-size: 0.9em; }}
        .specialized-info {{
            background: rgba(255,255,255,0.1);
            padding: 10px;
            margin-top: 10px;
            border-radius: 10px;
            font-size: 0.8em;
        }}
        .messages {{ 
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            background: #f8f9fa;
        }}
        .message {{ 
            margin: 15px 0;
            animation: fadeIn 0.3s ease-in;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .user-message {{ 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 20px;
            border-radius: 20px 20px 5px 20px;
            margin-left: 20%;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        }}
        .bot-message {{ 
            background: white;
            color: #333;
            padding: 15px 20px;
            border-radius: 20px 20px 20px 5px;
            margin-right: 20%;
            border-left: 4px solid #4facfe;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        .input-area {{
            padding: 20px;
            background: white;
            border-top: 1px solid #eee;
            display: flex;
            gap: 10px;
        }}
        .message-input {{ 
            flex: 1;
            padding: 15px 20px;
            border: 2px solid #e9ecef;
            border-radius: 25px;
            font-size: 16px;
            outline: none;
            transition: all 0.3s ease;
        }}
        .message-input:focus {{
            border-color: #4facfe;
            box-shadow: 0 0 0 3px rgba(79, 172, 254, 0.1);
        }}
        .send-button {{ 
            padding: 15px 25px;
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(79, 172, 254, 0.3);
        }}
        .send-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(79, 172, 254, 0.4);
        }}
        .send-button:active {{
            transform: translateY(0);
        }}
        .typing-indicator {{
            display: none;
            padding: 10px 20px;
            color: #666;
            font-style: italic;
        }}
        .quick-actions {{
            display: flex;
            gap: 10px;
            padding: 10px 20px;
            flex-wrap: wrap;
        }}
        .quick-action {{
            background: #e9ecef;
            border: none;
            padding: 8px 15px;
            border-radius: 15px;
            cursor: pointer;
            font-size: 0.9em;
            transition: all 0.3s ease;
        }}
        .quick-action:hover {{
            background: #4facfe;
            color: white;
        }}
        .status-indicator {{
            width: 10px;
            height: 10px;
            background: #28a745;
            border-radius: 50%;
            display: inline-block;
            margin-right: 8px;
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{
            0% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
            100% {{ opacity: 1; }}
        }}
        
        /* Mobile responsiveness */
        @media (max-width: 768px) {{
            .chat-container {{ width: 95%; height: 95vh; }}
            .user-message {{ margin-left: 10%; }}
            .bot-message {{ margin-right: 10%; }}
            .input-area {{ padding: 15px; }}
        }}
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h1><span class="status-indicator"></span>{agent_name}</h1>
            <p>{agent_description}</p>
            <div class="specialized-info">
                {specialized_features}
            </div>
        </div>
        
        <div class="messages" id="messages">
            <div class="message bot-message">
                <strong>🤖 {agent_name}:</strong> {custom_responses['welcome']}
            </div>
        </div>
        
        <div class="quick-actions">
            {self._generate_quick_actions_html(agent_type)}
        </div>
        
        <div class="typing-indicator" id="typingIndicator">
            🤖 Agent pisze odpowiedź...
        </div>
        
        <div class="input-area">
            <input type="text" id="messageInput" class="message-input" placeholder="Wpisz swoją wiadomość...">
            <button id="sendButton" class="send-button">Wyślij</button>
        </div>
    </div>
    
    <script>
        const responses = {custom_responses['responses_js']};
        const agentType = '{agent_type}';
        
        function sendMessage() {{
            const input = document.getElementById('messageInput');
            const messages = document.getElementById('messages');
            const typingIndicator = document.getElementById('typingIndicator');
            const message = input.value.trim();
            
            if (message) {{
                // User message
                messages.innerHTML += `<div class="message user-message"><strong>Ty:</strong> ${{message}}</div>`;
                input.value = '';
                
                // Show typing indicator
                typingIndicator.style.display = 'block';
                messages.scrollTop = messages.scrollHeight;
                
                // Bot response (simulated with agent-specific responses)
                setTimeout(() => {{
                    typingIndicator.style.display = 'none';
                    const response = getAgentResponse(message, agentType);
                    messages.innerHTML += `<div class="message bot-message"><strong>🤖 {agent_name}:</strong> ${{response}}</div>`;
                    messages.scrollTop = messages.scrollHeight;
                }}, 1000 + Math.random() * 1000);
            }}
        }}
        
        function getAgentResponse(message, type) {{
            const messageLower = message.toLowerCase();
            
            // Agent-specific responses
            if (type === 'communication' || type === 'email') {{
                if (messageLower.includes('email') || messageLower.includes('mail')) {{
                    return responses.email[Math.floor(Math.random() * responses.email.length)];
                }}
                if (messageLower.includes('wysłać') || messageLower.includes('send')) {{
                    return responses.send[Math.floor(Math.random() * responses.send.length)];
                }}
                if (messageLower.includes('śledzenie') || messageLower.includes('track')) {{
                    return responses.track[Math.floor(Math.random() * responses.track.length)];
                }}
            }}
            
            // General responses
            return responses.general[Math.floor(Math.random() * responses.general.length)];
        }}
        
        function sendQuickAction(action) {{
            document.getElementById('messageInput').value = action;
            sendMessage();
        }}
        
        document.getElementById('messageInput').addEventListener('keypress', function(e) {{
            if (e.key === 'Enter') sendMessage();
        }});
        
        document.getElementById('sendButton').addEventListener('click', sendMessage);
        
        // Auto-focus input
        document.getElementById('messageInput').focus();
    </script>
</body>
</html>"""
        
        html_base64 = base64.b64encode(html_content.encode('utf-8')).decode()
        
        return {
            "success": True,
            "html_content": html_content,
            "download_base64": html_base64,
            "filename": f"agent_chat_{agent_name.replace(' ', '_').lower()}_{agent_id[:8]}.html",
            "theme": theme,
            "agent_type": agent_type,
            "features": [
                "Responsive design", 
                "Auto-scroll", 
                "Enter support", 
                "Typing indicator",
                "Quick actions",
                "Agent-specific responses",
                "Modern animations",
                "Mobile-friendly"
            ]
        }
        
    async def deploy_agent(self, agent_id: str, environment: str = "local") -> Dict[str, Any]:
        """Wdraża agenta"""
        deployment_id = str(uuid.uuid4())
        
        self.deployments[deployment_id] = {
            "id": deployment_id,
            "agent_id": agent_id,
            "environment": environment,
            "status": "running",
            "deployed_at": datetime.now().isoformat()
        }
        
        return {
            "success": True,
            "deployment_id": deployment_id,
            "environment": environment,
            "status": "deployed",
            "endpoint": f"http://localhost:8000/agent/{agent_id}" if environment == "local" else f"https://api.example.com/{deployment_id}"
        }
        
    def _get_specialized_features(self, agent_type: str) -> str:
        """Zwraca specjalne funkcje dla typu agenta"""
        features = {
            'communication': '📧 Specjalizacja: Email Management & Communication • SMTP/IMAP Integration • Tracking & Analytics',
            'email': '📧 Specjalizacja: Email Management & Communication • SMTP/IMAP Integration • Tracking & Analytics',
            'ecommerce': '🛒 Specjalizacja: E-commerce & Sales • Product Management • Order Processing',
            'customer_service': '🎧 Specjalizacja: Customer Support • Ticket Management • Knowledge Base',
            'sales': '💼 Specjalizacja: Sales & CRM • Lead Management • Pipeline Tracking',
            'marketing': '📊 Specjalizacja: Marketing Automation • Campaign Management • Analytics',
            'finance': '💰 Specjalizacja: Financial Services • Invoice Management • Payment Processing',
            'general': '🤖 Uniwersalny Agent AI • Multi-domain Support • Intelligent Processing'
        }
        return features.get(agent_type, features['general'])
    
    def _get_custom_responses(self, agent_type: str) -> Dict[str, Any]:
        """Zwraca niestandardowe odpowiedzi dla typu agenta"""
        if agent_type in ['communication', 'email']:
            return {
                'welcome': 'Witaj! Jestem Twoim specjalistą od zarządzania pocztą elektroniczną. Mogę pomóc Ci z wysyłaniem, śledzeniem i analizą emaili. Co chcesz dzisiaj zrobić?',
                'responses_js': '''{{
                    email: [
                        "📧 Analizuję Twoje wymagania dotyczące emaili. Mogę zintegrować Gmail, Outlook lub SendGrid dla optymalnej obsługi poczty.",
                        "📨 Świetnie! Dla lepszego zarządzania emailami sugeruję konfigurację automatycznego trackingu dostaw i odpowiedzi.",
                        "✉️ Email marketing wymaga strategicznego podejścia. Czy chcesz skonfigurować szablon oraz personalizację wiadomości?"
                    ],
                    send: [
                        "📤 Przygotowuję wysyłkę emaili. Czy mam użyć domyślnego szablonu czy chcesz utworzyć niestandardową wiadomość?",
                        "🚀 Rozpoczynam proces wysyłania. Monitoring dostaw będzie dostępny w czasie rzeczywistym.",
                        "📨 Email zostanie wysłany z pełnym trackingiem. Otrzymasz powiadomienie o statusie dostarczenia."
                    ],
                    track: [
                        "📊 Sprawdzam status śledzenia emaili. Widzę szczegółowe statystyki otwarć, kliknięć i dostaw.",
                        "📈 Analiza trackingu pokazuje wysokie zaangażowanie odbiorców. Oto szczegółowy raport...",
                        "🎯 Śledzenie aktywne! Mogę pokazać Ci mapy cieplne kliknięć oraz czasy otwarcia wiadomości."
                    ],
                    general: [
                        "📧 Jako specjalista emaili, mogę pomóc z integracją SMTP/IMAP, automatyzacją wysyłek oraz analizą rezultatów.",
                        "💡 Mam dostęp do zaawansowanych narzędzi email marketingu. Chcesz skonfigurować automatyczne kampanie?",
                        "🔧 Mogę zintegrować Twój system z Gmail, Outlook, SendGrid lub innym dostawcą email services."
                    ]
                }}'''
            }
        
        elif agent_type == 'ecommerce':
            return {
                'welcome': 'Cześć! Jestem Twoim asystentem e-commerce. Pomagam z zarządzaniem produktami, zamówieniami i obsługą klientów. W czym mogę pomóc?',
                'responses_js': '''{{
                    general: [
                        "🛒 Jako specjalista e-commerce mogę pomóc z optymalizacją sklepu, zarządzaniem inwentarzem i analizą sprzedaży.",
                        "📊 Analizuję Twoje potrzeby biznesowe. Mogę zintegrować systemy płatności, shipping i customer support.",
                        "💼 Przygotowuję rozwiązania dla Twojego e-commerce. Chcesz rozpocząć od analizy konkurencji czy optymalizacji konwersji?"
                    ]
                }}'''
            }
        
        elif agent_type == 'customer_service':
            return {
                'welcome': 'Witaj! Jestem Twoim asystentem customer service. Specializuję się w obsłudze klienta, zarządzaniu ticketami i knowledge base. Jak mogę pomóc?',
                'responses_js': '''{{
                    general: [
                        "🎧 Jako specjalista customer service mogę pomóc z automatyzacją odpowiedzi, eskalacją problemów i analizą satysfakcji klientów.",
                        "📋 Analizuję Twoje procesy obsługi klienta. Mogę zoptymalizować czas odpowiedzi i jakość wsparcia.",
                        "💬 Przygotowuję inteligentne rozwiązania dla customer support. Rozpoczniemy od chatbota czy knowledge base?"
                    ]
                }}'''
            }
        
        else:
            return {
                'welcome': 'Cześć! Jestem Twoim inteligentnym asystentem AI. Jestem gotowy pomóc Ci z różnymi zadaniami i projektami. O czym chcesz porozmawiać?',
                'responses_js': '''{{
                    general: [
                        "🤖 Dzięki za pytanie! Na podstawie mojej analizy AI sugeruję optymalne rozwiązanie dla Twojej sytuacji.",
                        "💡 Przeanalizowałem Twoją sytuację. Oto co proponuję na podstawie najlepszych praktyk...",
                        "✨ Świetne pytanie! Moja inteligentna analiza wskazuje na kilka interesujących możliwości..."
                    ]
                }}'''
            }
    
    def _generate_quick_actions_html(self, agent_type: str) -> str:
        """Generuje przyciski szybkich akcji dla typu agenta"""
        if agent_type in ['communication', 'email']:
            return '''
                <button class="quick-action" onclick="sendQuickAction('Sprawdź status emaili')">📊 Status Emaili</button>
                <button class="quick-action" onclick="sendQuickAction('Wyślij newsletter')">📧 Wyślij Newsletter</button>
                <button class="quick-action" onclick="sendQuickAction('Konfiguruj SMTP')">⚙️ Konfiguruj SMTP</button>
                <button class="quick-action" onclick="sendQuickAction('Analizuj bounce rate')">📈 Analiza Bounce</button>
            '''
        elif agent_type == 'ecommerce':
            return '''
                <button class="quick-action" onclick="sendQuickAction('Sprawdź zamówienia')">📦 Zamówienia</button>
                <button class="quick-action" onclick="sendQuickAction('Analiza produktów')">🛍️ Produkty</button>
                <button class="quick-action" onclick="sendQuickAction('Raport sprzedaży')">📊 Sprzedaż</button>
            '''
        elif agent_type == 'customer_service':
            return '''
                <button class="quick-action" onclick="sendQuickAction('Sprawdź tickety')">🎫 Tickety</button>
                <button class="quick-action" onclick="sendQuickAction('FAQ update')">❓ FAQ</button>
                <button class="quick-action" onclick="sendQuickAction('Satysfakcja klientów')">😊 Satysfakcja</button>
            '''
        else:
            return '''
                <button class="quick-action" onclick="sendQuickAction('Pomoc')">❓ Pomoc</button>
                <button class="quick-action" onclick="sendQuickAction('Funkcje')">⚡ Funkcje</button>
                <button class="quick-action" onclick="sendQuickAction('Przykłady')">💡 Przykłady</button>
            '''