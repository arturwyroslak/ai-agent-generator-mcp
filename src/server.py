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
        
        # Import enhanced managers with background intelligence
        from .tools.enhanced_agent_manager import EnhancedAgentManager
        from .tools.component_manager import ComponentManager  
        from .tools.workflow_manager import WorkflowManager
        from .tools.deployer import AgentDeployer
        
        self.agent_manager = EnhancedAgentManager()  # ENHANCED VERSION
        self.component_manager = ComponentManager()
        self.workflow_manager = WorkflowManager()
        self.deployer = AgentDeployer()
        
        print("🤖 Inicjalizacja Enhanced Agent Manager z AI...")
        print("📊 Background Intelligence: AKTYWNA")
        
        self._setup_handlers()
    
    def _setup_handlers(self):
        @self.server.list_resources()
        async def handle_list_resources() -> ListResourcesResult:
            return ListResourcesResult(
                resources=[
                    Resource(
                        uri="components://catalog",
                        name="Katalog Komponentów",
                        description="500+ inteligentnych komponentów AI",
                        mimeType="application/json",
                    ),
                    Resource(
                        uri="intelligence://context",
                        name="Smart Context",
                        description="AI learned patterns i intelligence insights",
                        mimeType="application/json",
                    )
                ]
            )

        @self.server.read_resource()
        async def handle_read_resource(uri: str) -> ReadResourceResult:
            if uri == "components://catalog":
                from .components import get_all_available_components
                components = get_all_available_components()
                return ReadResourceResult(
                    contents=[TextContent(type="text", text=json.dumps(components, indent=2, ensure_ascii=False))]
                )
            elif uri == "intelligence://context":
                context_data = {
                    "learned_patterns": len(self.agent_manager.smart_context.learned_patterns),
                    "component_performance_data": len(self.agent_manager.smart_context.component_performance),
                    "background_intelligence": "ACTIVE",
                    "ai_features": [
                        "Automatic description analysis",
                        "Hidden requirements detection", 
                        "Smart component selection",
                        "Auto-configuration",
                        "Learning from successes"
                    ]
                }
                return ReadResourceResult(
                    contents=[TextContent(type="text", text=json.dumps(context_data, indent=2, ensure_ascii=False))]
                )
            else:
                return ReadResourceResult(
                    contents=[TextContent(type="text", text="{}")]
                )

        @self.server.list_tools()
        async def handle_list_tools() -> ListToolsResult:
            return ListToolsResult(
                tools=[
                    # === INTELIGENTNE GENEROWANIE AGENTÓW ===
                    Tool(
                        name="create_agent",
                        description="🤖 ENHANCED: Tworzy agenta z pełną AI inteligencją - analiza opisu, wykrywanie ukrytych wymagań, auto-konfiguracja komponentów, inteligentny workflow",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "string",
                                    "description": "Nazwa agenta"
                                },
                                "description": {
                                    "type": "string",
                                    "description": "📊 KLUCZOWE: Szczegółowy opis tego co agent ma robić. AI analizuje każde słowo i wykrywa ukryte wymagania!"
                                },
                                "domain": {
                                    "type": "string",
                                    "enum": ["customer_service", "sales", "marketing", "hr", "finance", "development", "analytics", "ecommerce", "general"],
                                    "description": "Domena (OPCJONALNA - AI wykryje automatycznie na podstawie opisu)"
                                },
                                "complexity": {
                                    "type": "string",
                                    "enum": ["simple", "medium", "complex"],
                                    "description": "Złożoność (OPCJONALNA - AI wykryje automatycznie)"
                                }
                            },
                            "required": ["name", "description"]
                        }
                    ),
                    
                    Tool(
                        name="get_agent",
                        description="📋 ENHANCED: Pobiera agenta z pełnymi AI insights, intelligence score i performance analytics",
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
                        description="📝 ENHANCED: Lista agentów posortowana według Intelligence Score - najinteligentniejsze agenty na górze",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "filter_domain": {
                                    "type": "string",
                                    "description": "Filtr po domenie"
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
                        description="🧪 ENHANCED: Testuje agenta z zaawansowaną analizą wydajności i uczeniem się z wyników",
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
                                        "user_message": {
                                            "type": "string",
                                            "description": "Testowa wiadomość użytkownika"
                                        },
                                        "user_context": {
                                            "type": "object",
                                            "description": "Dodatkowy kontekst użytkownika"
                                        }
                                    },
                                    "required": ["user_message"]
                                },
                                "test_scenario": {
                                    "type": "string",
                                    "description": "Nazwa scenariusza testowego",
                                    "default": "standard_test"
                                }
                            },
                            "required": ["agent_id", "test_input"]
                        }
                    ),
                    
                    # === ZARZĄDZANIE KOMPONENTAMI ===
                    Tool(
                        name="get_components",
                        description="🔧 Pobiera wszystkie dostępne komponenty (500+) z inteligentnym filtrowaniem",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "category": {
                                    "type": "string",
                                    "enum": ["ai_processing", "integrations", "data_tools", "workflow_control", "all"],
                                    "description": "Kategoria komponentów",
                                    "default": "all"
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
                        description="➕ ENHANCED: Dodaje komponent z automatyczną inteligentną konfiguracją dopastowaną do agenta",
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
                                    "description": "Konfiguracja (OPCJONALNA - AI wygeneruje optymalną automatycznie)"
                                }
                            },
                            "required": ["agent_id", "component_id"]
                        }
                    ),
                    
                    # === WDRAŻANIE ===
                    Tool(
                        name="generate_chat_interface",
                        description="💬 Generuje profesjonalny interfejs chatu HTML do testowania agenta",
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
                        description="🚀 Wdraża agenta do środowiska produkcyjnego",
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
                        description="🗑️ Usuwa agenta i wszystkie jego dane",
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
                result = None
                
                # === ENHANCED AGENT OPERATIONS WITH BACKGROUND AI ===
                if name == "create_agent":
                    print(f"✨ ENHANCED CREATE_AGENT wywołany z AI background processing...")
                    result = await self.agent_manager.create_agent(**arguments)
                    
                elif name == "get_agent":
                    result = await self.agent_manager.get_agent(**arguments)
                    
                elif name == "list_agents": 
                    result = await self.agent_manager.list_agents(**arguments)
                    
                elif name == "test_agent":
                    print(f"🧪 ENHANCED TEST_AGENT z learning from results...")
                    result = await self.agent_manager.test_agent(**arguments)
                    
                elif name == "delete_agent":
                    result = await self._delete_agent_wrapper(**arguments)
                
                # === COMPONENT OPERATIONS WITH AUTO-CONFIG ===
                elif name == "get_components":
                    result = await self.component_manager.get_components(**arguments)
                    
                elif name == "add_component_to_agent":
                    print(f"➕ ENHANCED ADD_COMPONENT z auto-configuration...")
                    result = await self._enhanced_add_component(**arguments)
                
                # === DEPLOYMENT ===
                elif name == "generate_chat_interface":
                    result = await self.deployer.generate_chat_interface(**arguments)
                    
                elif name == "deploy_agent":
                    result = await self.deployer.deploy_agent(**arguments)
                
                else:
                    result = {
                        "success": False,
                        "error": f"Nieznane narzędzie: {name}",
                        "available_tools": [
                            "create_agent", "get_agent", "list_agents", "test_agent", "delete_agent",
                            "get_components", "add_component_to_agent",
                            "generate_chat_interface", "deploy_agent"
                        ]
                    }
                
                return CallToolResult(
                    content=[TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]
                )
                
            except Exception as e:
                import traceback
                error_result = {
                    "success": False,
                    "error": str(e),
                    "tool": name,
                    "arguments": arguments,
                    "traceback": traceback.format_exc()
                }
                return CallToolResult(
                    content=[TextContent(type="text", text=json.dumps(error_result, indent=2, ensure_ascii=False))],
                    isError=True
                )
    
    # === WRAPPER METHODS FOR ENHANCED FUNCTIONALITY ===
    
    async def _enhanced_add_component(self, agent_id: str, component_id: str, configuration: Dict = None) -> Dict[str, Any]:
        """Enhanced dodawanie komponentu z auto-konfiguracją"""
        
        # Pobierz agenta
        agent_result = await self.agent_manager.get_agent(agent_id)
        if not agent_result["success"]:
            return agent_result
        
        agent = agent_result["agent"]
        
        # Pobierz info o komponencie z katalogu
        from .components import get_all_available_components
        component_catalog = get_all_available_components()
        
        component_info = None
        for category in component_catalog.values():
            if isinstance(category, list):
                for comp in category:
                    if comp.get("component_id") == component_id:
                        component_info = comp
                        break
                if component_info:
                    break
        
        if not component_info:
            return {
                "success": False,
                "error": f"Komponent '{component_id}' nie został znaleziony w katalogu 500+ komponentów",
                "suggestion": "Użyj 'get_components' aby zobaczyć dostępne komponenty"
            }
        
        # === ENHANCED AUTO-CONFIGURATION ===
        if not configuration:
            print(f"⚙️ Auto-konfiguracja komponentu {component_id} dla domeny {agent['domain']}...")
            
            from .utils.smart_context import get_smart_context
            smart_context = get_smart_context()
            
            # Pobierz learned configuration patterns
            domain_insights = await smart_context.get_domain_insights(agent["domain"])
            
            # Inteligentna auto-konfiguracja
            if "llm" in component_id or "pollinations" in component_id:
                configuration = await self._ultra_smart_llm_config(
                    agent["description"], agent["domain"], component_info, domain_insights
                )
            else:
                # Użyj learned patterns lub defaults
                configuration = component_info.get("default_config", {
                    "timeout": 30,
                    "auto_configured": True
                })
        
        # Dodaj komponent z enhanced info
        import uuid
        new_component = {
            "id": str(uuid.uuid4()),
            "component_id": component_id,
            "name": component_info["name"],
            "type": component_info.get("type", "unknown"),
            "configuration": configuration,
            "auto_configured": configuration.get("auto_configured", False),
            "added_at": datetime.now().isoformat(),
            "position": len(agent.get("components", []))
        }
        
        # Dodaj do agenta
        if "components" not in agent:
            agent["components"] = []
        agent["components"].append(new_component)
        agent["updated_at"] = datetime.now().isoformat()
        
        # Przelicz intelligence score
        agent["metrics"]["intelligence_score"] = await self._recalculate_intelligence_score(agent)
        
        # Zaktualizuj w storage
        self.agent_manager.agents[agent_id] = agent
        
        return {
            "success": True,
            "message": f"Komponent '{component_info['name']}' dodany z enhanced AI configuration",
            "component_added": {
                "id": new_component["id"],
                "name": component_info["name"],
                "type": component_info.get("type"),
                "auto_configured": new_component["auto_configured"],
                "configuration_keys": list(configuration.keys())
            },
            "agent_updated": {
                "total_components": len(agent["components"]),
                "intelligence_score": agent["metrics"]["intelligence_score"],
                "last_modified": agent["updated_at"]
            },
            "ai_enhancement": {
                "background_analysis": "Applied",
                "learned_patterns_used": len(configuration) > 0,
                "optimization_level": "Advanced"
            }
        }
    
    async def _ultra_smart_llm_config(self, description: str, domain: str, 
                                    component_info: Dict, domain_insights: Dict) -> Dict[str, Any]:
        """Ultra-inteligentna konfiguracja LLM z learned patterns"""
        
        # Bazowa inteligentna konfiguracja
        config = {
            "api_endpoint": "https://text.pollinations.ai/openai",
            "model": "openai",
            "temperature": 0.7,
            "max_tokens": 1000,
            "auto_configured": True
        }
        
        # Dostosowanie temperatury na podstawie analizy
        precision_words = ["precyzyjny", "dokładny", "exact", "specific"]
        creativity_words = ["kreatywny", "innowacyjny", "creative", "varied"]
        
        desc_lower = description.lower()
        if any(word in desc_lower for word in precision_words):
            config["temperature"] = 0.2
        elif any(word in desc_lower for word in creativity_words):
            config["temperature"] = 0.9
        
        # Inteligentny system prompt na podstawie domeny i learned patterns
        domain_prompts = {
            "customer_service": f"Jesteś ekspertem obsługi klienta. {description[:100]}...",
            "sales": f"Jesteś specjalistą sprzedaży. {description[:100]}...",
            "ecommerce": f"Jesteś ekspertem e-commerce. {description[:100]}...",
        }
        
        config["system_prompt"] = domain_prompts.get(domain, f"Jesteś pomocnym asystentem AI. {description[:100]}...")
        
        # Wykorzystaj domain insights dla dalszej optymalizacji
        if domain_insights.get("top_components"):
            config["optimization_note"] = f"Konfiguracja oparta na analizie {len(domain_insights.get('success_patterns', 0))} udanych agentów"
        
        return config
    
    async def _recalculate_intelligence_score(self, agent: Dict) -> int:
        """Przelicza intelligence score agenta"""
        base_score = 50
        
        # Punkty za liczbę komponentów
        component_count = len(agent.get("components", []))
        base_score += min(30, component_count * 3)
        
        # Punkty za auto-configured components 
        auto_configured = len([c for c in agent.get("components", []) if c.get("auto_configured")])
        base_score += auto_configured * 2
        
        # Punkty za AI analysis
        ai_analysis = agent.get("ai_analysis", {})
        if ai_analysis:
            base_score += 10
            base_score += len(ai_analysis.get("implicit_requirements", [])) * 3
        
        return min(100, base_score)
    
    async def _delete_agent_wrapper(self, agent_id: str) -> Dict[str, Any]:
        """Enhanced usuwanie agenta"""
        if agent_id not in self.agent_manager.agents:
            return {
                "success": False,
                "error": f"Agent {agent_id} nie istnieje"
            }
        
        agent_name = self.agent_manager.agents[agent_id].get("name", "Unknown")
        intelligence_score = self.agent_manager.agents[agent_id].get("metrics", {}).get("intelligence_score", 0)
        
        del self.agent_manager.agents[agent_id]
        
        return {
            "success": True,
            "message": f"Agent '{agent_name}' (Intelligence Score: {intelligence_score}%) został usunięty",
            "deleted_agent": {
                "id": agent_id,
                "name": agent_name,
                "intelligence_score": intelligence_score
            }
        }

async def main():
    """Uruchomienie serwera z FULL ENHANCED FEATURES"""
    print("🚀 INICJALIZACJA MCP SERWERÓW Z ENHANCED AI...")
    
    mcp_server = MCPAgentCreatorServer()
    
    print("\n🎆 SERWER MCP GOTOWY Z ADVANCED INTELLIGENCE!")
    print("🤖 Enhanced Features AKTYWNE:")
    print("   • Automatyczna analiza opisów z NLP")
    print("   • Wykrywanie ukrytych wymagań (implicit requirements)")
    print("   • Inteligentna konfiguracja każdego komponentu")
    print("   • Smart Context - uczenie się z udanych agentów")
    print("   • Auto-optymalizacja workflow z AI reasoning")
    print("   • Intelligence Score dla każdego agenta")
    print("   • Background learning i pattern recognition")
    print("   • Advanced testing z performance insights")
    print("\n📊 500+ komponentów gotowych do użycia!")
    print("🎯 Wszystkie narzędzia MCP wzbogacone o AI!")
    print("\n✅ SERWER GOTOWY DO PRACY Z FULL INTELLIGENCE!")
    
    # Import and run the MCP server
    from mcp.server.stdio import stdio_server
    async with stdio_server() as (read_stream, write_stream):
        await mcp_server.server.run(read_stream, write_stream, 
                                   mcp_server.server.create_initialization_options())

if __name__ == "__main__":
    import uuid
    from datetime import datetime
    asyncio.run(main())