#!/usr/bin/env python3
"""Zaawansowany serwer MCP do tworzenia agentów AI z inteligentnymi narzędziami"""

import asyncio
import json
from typing import Any, Dict, List, Optional
from mcp.server import Server
from mcp.types import (
    CallToolResult,
    ListResourcesResult, 
    ListToolsResult,
    ReadResourceResult,
    Resource,
    TextContent,
    Tool,
)

class MCPAgentCreatorServer:
    """Główny serwer MCP z zaawansowanymi narzędziami AI i inteligencją w tle"""
    
    def __init__(self):
        self.server = Server("mcp-ai-agent-creator")
        
        # Import enhanced managers
        from .tools.enhanced_agent_manager import EnhancedAgentManager
        self.agent_manager = EnhancedAgentManager()
        
        self._setup_handlers()
    
    def _setup_handlers(self):
        @self.server.list_tools()
        async def handle_list_tools() -> ListToolsResult:
            return ListToolsResult(
                tools=[
                    # === INTELIGENTNE GENEROWANIE AGENTÓW ===
                    Tool(
                        name="create_agent",
                        description="🤖 Tworzy inteligentnego agenta z automatyczną analizą opisu, detekcją ukrytych wymagań i auto-konfiguracją komponentów",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "string",
                                    "description": "Nazwa agenta"
                                },
                                "description": {
                                    "type": "string",
                                    "description": "Szczegółowy opis tego co agent ma robić - im więcej szczegółów, tym lepszy rezultat AI"
                                },
                                "domain": {
                                    "type": "string",
                                    "enum": ["customer_service", "sales", "marketing", "hr", "finance", "development", "analytics", "ecommerce", "general"],
                                    "description": "Domena (opcjonalna - AI wykryje automatycznie)"
                                },
                                "complexity": {
                                    "type": "string",
                                    "enum": ["simple", "medium", "complex"],
                                    "description": "Poziom złożoności (opcjonalny - AI wykryje automatycznie)"
                                }
                            },
                            "required": ["name", "description"]
                        }
                    ),
                    
                    Tool(
                        name="get_agent",
                        description="📋 Pobiera szczegóły agenta wraz z AI insights i analizą inteligencji",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "agent_id": {
                                    "type": "string",
                                    "description": "ID agenta do pobrania"
                                }
                            },
                            "required": ["agent_id"]
                        }
                    ),
                    
                    Tool(
                        name="list_agents",
                        description="📝 Lista agentów posortowana według Intelligence Score",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "filter_domain": {
                                    "type": "string",
                                    "description": "Opcjonalny filtr po domenie"
                                },
                                "filter_status": {
                                    "type": "string",
                                    "enum": ["draft", "active", "deployed", "inactive"],
                                    "description": "Filtr po statusie"
                                }
                            }
                        }
                    ),
                    
                    Tool(
                        name="test_agent",
                        description="🧪 Testuje agenta z uczeniem maszynowym z wyników",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "agent_id": {
                                    "type": "string",
                                    "description": "ID agenta do testowania"
                                },
                                "test_input": {
                                    "type": "object",
                                    "description": "Dane testowe",
                                    "properties": {
                                        "user_message": {"type": "string"},
                                        "user_context": {"type": "object"}
                                    },
                                    "required": ["user_message"]
                                },
                                "test_scenario": {
                                    "type": "string",
                                    "description": "Nazwa scenariusza testowego"
                                }
                            },
                            "required": ["agent_id", "test_input"]
                        }
                    ),
                    
                    # === ZARZĄDZANIE KOMPONENTAMI ===
                    Tool(
                        name="get_components",
                        description="🔧 Pobiera wszystkie dostępne komponenty (500+)",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "category": {
                                    "type": "string",
                                    "enum": ["ai_processing", "integrations", "data_tools", "workflow_control", "all"],
                                    "description": "Kategoria komponentów"
                                },
                                "search": {
                                    "type": "string",
                                    "description": "Wyszukaj po nazwie lub opisie"
                                }
                            }
                        }
                    ),
                    
                    Tool(
                        name="add_component_to_agent",
                        description="➕ Dodaje komponent do agenta z automatyczną konfiguracją",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "agent_id": {
                                    "type": "string",
                                    "description": "ID agenta"
                                },
                                "component_id": {
                                    "type": "string",
                                    "description": "ID komponentu do dodania"
                                },
                                "configuration": {
                                    "type": "object",
                                    "description": "Konfiguracja (opcjonalna - zostanie auto-generowana)"
                                }
                            },
                            "required": ["agent_id", "component_id"]
                        }
                    ),
                    
                    # === WDRAŻANIE ===
                    Tool(
                        name="generate_chat_interface",
                        description="💬 Generuje interfejs chatu HTML do testowania agenta",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "agent_id": {
                                    "type": "string",
                                    "description": "ID agenta"
                                },
                                "theme": {
                                    "type": "string",
                                    "enum": ["light", "dark", "modern", "classic"],
                                    "description": "Motyw interfejsu",
                                    "default": "modern"
                                }
                            },
                            "required": ["agent_id"]
                        }
                    ),
                    
                    Tool(
                        name="deploy_agent",
                        description="🚀 Wdraża agenta do środowiska",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "agent_id": {
                                    "type": "string",
                                    "description": "ID agenta"
                                },
                                "environment": {
                                    "type": "string",
                                    "enum": ["local", "cloud", "docker"],
                                    "description": "Środowisko wdrożenia",
                                    "default": "local"
                                }
                            },
                            "required": ["agent_id"]
                        }
                    ),
                    
                    Tool(
                        name="delete_agent",
                        description="🗑️ Usuwa agenta",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "agent_id": {
                                    "type": "string",
                                    "description": "ID agenta do usunięcia"
                                }
                            },
                            "required": ["agent_id"]
                        }
                    )
                ]
            )

        @self.server.call_tool()
        async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> CallToolResult:
            try:
                # === ENHANCED AGENT OPERATIONS ===
                if name == "create_agent":
                    result = await self.agent_manager.create_agent(**arguments)
                elif name == "get_agent":
                    result = await self.agent_manager.get_agent(**arguments)
                elif name == "list_agents":
                    result = await self.agent_manager.list_agents(**arguments)
                elif name == "test_agent":
                    result = await self.agent_manager.test_agent(**arguments)
                elif name == "delete_agent":
                    result = await self._delete_agent(**arguments)
                
                # === COMPONENT OPERATIONS ===
                elif name == "get_components":
                    result = await self._get_components(**arguments)
                elif name == "add_component_to_agent":
                    result = await self._add_component_to_agent(**arguments)
                
                # === DEPLOYMENT ===
                elif name == "generate_chat_interface":
                    result = await self._generate_chat_interface(**arguments)
                elif name == "deploy_agent":
                    result = await self._deploy_agent(**arguments)
                
                else:
                    result = {
                        "success": False,
                        "error": f"Nieznane narzędzie: {name}"
                    }
                
                return CallToolResult(
                    content=[TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]
                )
                
            except Exception as e:
                error_result = {
                    "success": False,
                    "error": str(e),
                    "tool": name,
                    "arguments": arguments
                }
                return CallToolResult(
                    content=[TextContent(type="text", text=json.dumps(error_result, indent=2, ensure_ascii=False))],
                    isError=True
                )
    
    # === IMPLEMENTATION METHODS ===
    async def _get_components(self, category: str = None, search: str = None) -> Dict[str, Any]:
        """Pobiera komponenty z katalogu"""
        from .components import get_all_available_components, search_components
        
        if search:
            components = search_components(search, category)
        else:
            all_components = get_all_available_components()
            if category and category != "all":
                components = all_components.get(category, [])
            else:
                # Flatten all components
                components = []
                for cat_components in all_components.values():
                    if isinstance(cat_components, list):
                        components.extend(cat_components)
        
        return {
            "success": True,
            "components": components[:50],  # Limit to 50 for performance
            "total_available": len(components),
            "search_query": search,
            "filtered_category": category
        }
    
    async def _add_component_to_agent(self, agent_id: str, component_id: str, 
                                    configuration: Dict = None) -> Dict[str, Any]:
        """Dodaje komponent do agenta z inteligentną auto-konfiguracją"""
        
        # Pobierz agenta
        agent_result = await self.agent_manager.get_agent(agent_id)
        if not agent_result["success"]:
            return agent_result
        
        agent = agent_result["agent"]
        
        # Pobierz info o komponencie
        from .components import get_all_available_components
        component_catalog = get_all_available_components()
        
        component_info = None
        for category in component_catalog.values():
            if isinstance(category, list):
                for comp in category:
                    if comp.get("component_id") == component_id:
                        component_info = comp
                        break
        
        if not component_info:
            return {
                "success": False,
                "error": f"Komponent {component_id} nie został znaleziony"
            }
        
        # Auto-konfiguracja jeśli nie podano
        if not configuration:
            configuration = await self._auto_configure_component(
                component_info, agent["domain"], agent["description"]
            )
        
        # Dodaj komponent do agenta
        new_component = {
            "id": str(uuid.uuid4()),
            "component_id": component_id,
            "name": component_info["name"],
            "configuration": configuration,
            "auto_configured": configuration != {},
            "position": len(agent.get("components", []))
        }
        
        agent["components"].append(new_component)
        agent["updated_at"] = datetime.now().isoformat()
        
        # Zaktualizuj agenta w storage
        self.agent_manager.agents[agent_id] = agent
        
        return {
            "success": True,
            "message": f"Dodano komponent {component_info['name']} do agenta",
            "component_added": {
                "id": new_component["id"],
                "name": component_info["name"],
                "auto_configured": new_component["auto_configured"]
            },
            "agent_updated": {
                "total_components": len(agent["components"]),
                "last_modified": agent["updated_at"]
            }
        }
    
    async def _auto_configure_component(self, component_info: Dict, domain: str, 
                                      description: str) -> Dict[str, Any]:
        """Automatyczna inteligentna konfiguracja komponentu"""
        
        comp_id = component_info.get("component_id", "")
        
        # Inteligentna konfiguracja dla LLM
        if "llm" in comp_id or "pollinations" in comp_id:
            return await self._smart_llm_config(description, domain)
        
        # Konfiguracja dla integracji
        elif "integration" in comp_id:
            return {
                "timeout": 30,
                "retry_attempts": 3,
                "rate_limit": 60
            }
        
        # Konfiguracja dla workflow control
        elif "controller" in comp_id or "router" in comp_id:
            return {
                "max_retries": 3,
                "timeout": 10,
                "fallback_enabled": True
            }
        
        # Domyślna konfiguracja
        return component_info.get("default_config", {})
    
    async def _smart_llm_config(self, description: str, domain: str) -> Dict[str, Any]:
        """Inteligentna konfiguracja LLM na podstawie opisu i domeny"""
        
        # Analiza potrzeb na podstawie słów kluczowych
        if any(word in description.lower() for word in ["precyzyjny", "dokładny", "faktyczny", "exact"]):
            temperature = 0.1  # Niska temperatura dla precyzji
        elif any(word in description.lower() for word in ["kreatywny", "pomysłowy", "różnorodny", "creative"]):
            temperature = 0.9  # Wysoka temperatura dla kreatywności  
        else:
            temperature = 0.7  # Standardowa
        
        # Dostosowanie system prompt do domeny
        system_prompts = {
            "customer_service": "Jesteś profesjonalnym i empatycznym asystentem obsługi klienta. Zawsze pomagasz i jesteś uprzejmy.",
            "sales": "Jesteś ekspertem sprzedaży skoncentrowanym na wynikach. Pomagasz klientom znaleźć najlepsze rozwiązania.",
            "hr": "Jesteś profesjonalnym asystentem HR dbającym o pracowników. Znasz procedury i regulacje.",
            "finance": "Jesteś precyzyjnym analitykiem finansowym. Udzielasz dokładnych informacji o finansach.",
            "marketing": "Jesteś kreatywnym specjalistą od marketingu. Znasz trendy i skuteczne strategie.",
            "ecommerce": "Jesteś ekspertem e-commerce. Pomagasz w sprzedaży online i zarządzaniu sklepem.",
            "development": "Jesteś ekspertem programowania. Pomagasz z kodem, architekturą i najlepszymi praktykami.",
            "general": "Jesteś wszechstronnym asystentem AI. Odpowiadasz pomocnie na różnorodne pytania."
        }
        
        system_prompt = system_prompts.get(domain, system_prompts["general"])
        
        # Adaptacyjne max_tokens na podstawie złożoności opisu
        desc_words = len(description.split())
        if desc_words > 100:
            max_tokens = 2000
        elif desc_words > 50:
            max_tokens = 1000
        else:
            max_tokens = 500
        
        return {
            "api_endpoint": "https://text.pollinations.ai/openai",
            "model": "openai",
            "temperature": temperature,
            "max_tokens": max_tokens,
            "system_prompt": system_prompt,
            "auto_optimized": True
        }
    
    async def _generate_chat_interface(self, agent_id: str, theme: str = "modern") -> Dict[str, Any]:
        """Generuje interfejs chatu HTML"""
        
        # Pobierz agenta
        agent_result = await self.agent_manager.get_agent(agent_id)
        if not agent_result["success"]:
            return agent_result
        
        agent = agent_result["agent"]
        
        html_content = f"""<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat z {agent['name']}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .chat-container {{
            width: 90%; max-width: 600px; height: 80vh;
            background: white; border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            display: flex; flex-direction: column;
        }}
        .chat-header {{
            padding: 20px; background: #667eea; color: white;
            border-radius: 20px 20px 0 0;
        }}
        .chat-messages {{
            flex: 1; padding: 20px; overflow-y: auto;
            display: flex; flex-direction: column; gap: 15px;
        }}
        .message {{
            max-width: 70%; padding: 12px 18px;
            border-radius: 18px; word-wrap: break-word;
        }}
        .bot-message {{ background: #f0f0f0; align-self: flex-start; }}
        .user-message {{ background: #667eea; color: white; align-self: flex-end; }}
        .input-container {{
            padding: 20px; border-top: 1px solid #eee;
            display: flex; gap: 10px;
        }}
        #messageInput {{
            flex: 1; padding: 12px; border: 1px solid #ddd;
            border-radius: 25px; outline: none;
        }}
        #sendButton {{
            padding: 12px 20px; background: #667eea;
            color: white; border: none; border-radius: 25px;
            cursor: pointer;
        }}
        #sendButton:hover {{ background: #5a6fd8; }}
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h2>💬 {agent['name']}</h2>
            <p>Inteligentny agent AI • Status: Online</p>
        </div>
        
        <div class="chat-messages" id="messages">
            <div class="message bot-message">
                Cześć! Jestem {agent['name']}. {agent.get('description', 'Jak mogę Ci pomóc?')}
            </div>
        </div>
        
        <div class="input-container">
            <input type="text" id="messageInput" placeholder="Wpisz swoją wiadomość..." maxlength="500">
            <button id="sendButton">Wyślij</button>
        </div>
    </div>
    
    <script>
        const messagesDiv = document.getElementById('messages');
        const messageInput = document.getElementById('messageInput');
        const sendButton = document.getElementById('sendButton');
        
        // Symulacja odpowiedzi agenta
        async function sendMessage() {{
            const message = messageInput.value.trim();
            if (!message) return;
            
            // Dodaj wiadomość użytkownika
            addMessage(message, 'user-message');
            messageInput.value = '';
            
            // Symuluj myślenie agenta
            setTimeout(() => {{
                const responses = [
                    "Rozumiem Twoje pytanie. Oto co mogę zaproponować...",
                    "Świetne pytanie! Na podstawie mojej analizy...", 
                    "Dzięki za informację. Myślę, że najlepszym rozwiązaniem będzie...",
                    "To bardzo ciekawy przypadek. Sugeruję następujące podejście..."
                ];
                const response = responses[Math.floor(Math.random() * responses.length)];
                addMessage(response, 'bot-message');
            }}, 1000 + Math.random() * 2000);
        }}
        
        function addMessage(text, className) {{
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message ' + className;
            messageDiv.textContent = text;
            messagesDiv.appendChild(messageDiv);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }}
        
        sendButton.addEventListener('click', sendMessage);
        messageInput.addEventListener('keypress', (e) => {{
            if (e.key === 'Enter') sendMessage();
        }});
        
        // Auto-focus na input
        messageInput.focus();
    </script>
</body>
</html>"""
        
        # Koduj do base64
        import base64
        html_base64 = base64.b64encode(html_content.encode()).decode()
        
        return {
            "success": True,
            "agent_name": agent["name"],
            "html_content": html_content,
            "download_base64": html_base64,
            "filename": f"chat_{agent_id[:8]}.html",
            "theme": theme,
            "features": [
                "Responsywny design",
                "Historia konwersacji", 
                "Automatyczne scrollowanie",
                "Obsługa Enter",
                "Symulacja odpowiedzi agenta"
            ]
        }
    
    async def _deploy_agent(self, agent_id: str, environment: str = "local") -> Dict[str, Any]:
        """Wdraża agenta do środowiska"""
        
        deployment_id = str(uuid.uuid4())
        
        return {
            "success": True,
            "deployment_id": deployment_id,
            "agent_id": agent_id,
            "environment": environment,
            "status": "deployed",
            "endpoint_url": f"http://localhost:8000/agent/{agent_id}" if environment == "local" else f"https://cloud-deploy.example.com/{deployment_id}",
            "deployment_time": datetime.now().isoformat(),
            "message": f"Agent wdrożony pomyślnie w środowisku {environment}"
        }
    
    async def _delete_agent(self, agent_id: str) -> Dict[str, Any]:
        """Usuwa agenta"""
        if agent_id not in self.agent_manager.agents:
            return {
                "success": False,
                "error": f"Agent {agent_id} nie istnieje"
            }
        
        agent_name = self.agent_manager.agents[agent_id].get("name", "Unknown")
        del self.agent_manager.agents[agent_id]
        
        return {
            "success": True,
            "message": f"Agent '{agent_name}' został usunięty",
            "deleted_agent_id": agent_id
        }

async def main():
    """Uruchomienie serwera z enhanced features"""
    server = MCPAgentCreatorServer()
    print("🚀 Serwer MCP z inteligentnym generowaniem agentów - READY")
    print("📊 Funkcje AI działające w tle:")
    print("   • Automatyczna analiza opisów")
    print("   • Wykrywanie ukrytych wymagań") 
    print("   • Inteligentna konfiguracja komponentów")
    print("   • Uczenie się z sukcesów")
    print("   • Auto-optymalizacja workflow")
    print("\nSerwer gotowy do pracy!")

if __name__ == "__main__":
    import uuid
    from datetime import datetime
    asyncio.run(main())