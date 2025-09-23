#!/usr/bin/env python3
"""Zaawansowany serwer MCP do tworzenia agentów AI z inteligentnymi narzędziami - FastMCP version"""

import asyncio
import json
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP, Context
from smithery.decorators import smithery
from pydantic import BaseModel, Field

class ConfigSchema(BaseModel):
    """Configuration schema for the AI Agent Generator MCP server"""
    api_key: Optional[str] = Field(None, description="Optional API key for external services")
    default_domain: str = Field("general", description="Default domain for agent creation")
    max_components: int = Field(50, description="Maximum number of components per agent", ge=1, le=100)

@smithery.server(config_schema=ConfigSchema)
def create_server():
    """Create and return a FastMCP server instance with AI agent generation capabilities."""
    
    server = FastMCP(name="AI Agent Generator MCP")
    
    # Import enhanced managers with background intelligence
    from .tools.enhanced_agent_manager import EnhancedAgentManager
    from .tools.component_manager import ComponentManager  
    from .tools.workflow_manager import WorkflowManager
    from .tools.deployer import AgentDeployer
    
    agent_manager = EnhancedAgentManager()
    component_manager = ComponentManager()
    workflow_manager = WorkflowManager()
    deployer = AgentDeployer()
    
    print("🤖 Inicjalizacja Enhanced Agent Manager z AI...")
    print("📊 Background Intelligence: AKTYWNA")
    
    # Register resources using the decorator approach
    @server.resource("components://catalog", 
                    name="Katalog Komponentów",
                    description="500+ inteligentnych komponentów AI",
                    mime_type="application/json")
    async def get_components_catalog() -> str:
        """Katalog 500+ inteligentnych komponentów AI"""
        try:
            components = await component_manager.get_all_components()
            context_data = {
                "total_components": len(components),
                "categories": list(set([c.get("category", "unknown") for c in components])),
                "domains": ["customer_service", "sales", "marketing", "hr", "finance", "development", "analytics", "ecommerce", "general"],
                "intelligence_features": {
                    "nlp_analysis": True,
                    "auto_configuration": True,
                    "smart_suggestions": True,
                    "background_learning": True
                },
                "components_sample": components[:10] if components else [],
                "max_components_per_agent": 50
            }
            return json.dumps(context_data, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)
    
    @server.resource("intelligence://context",
                    name="Smart Context", 
                    description="AI learned patterns i intelligence insights",
                    mime_type="application/json")
    async def get_intelligence_context() -> str:
        """AI learned patterns i intelligence insights"""
        try:
            # Get smart context from agent manager
            if hasattr(agent_manager, 'smart_context'):
                context_data = await agent_manager.smart_context.get_intelligence_insights()
            else:
                context_data = {
                    "learned_patterns": [],
                    "success_metrics": {},
                    "optimization_suggestions": [],
                    "background_intelligence": "Active"
                }
            return json.dumps(context_data, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @server.tool()
    async def create_agent(
        name: str,
        description: str,
        domain: str = "general", 
        complexity: str = "medium",
        ctx: Context = None
    ) -> str:
        """🤖 ENHANCED: Tworzy inteligentnego agenta AI z automatyczną analizą NLP i wykrywaniem ukrytych wymagań"""
        try:
            # Get session configuration
            config = ctx.session_config if ctx else None
            
            result = await agent_manager.create_agent(
                name=name,
                description=description, 
                domain=domain,
                complexity=complexity
            )
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": str(e),
                "ai_analysis": "Failed to analyze agent requirements"
            }, indent=2, ensure_ascii=False)

    @server.tool()
    async def get_agent(agent_id: str, ctx: Context = None) -> str:
        """📊 ENHANCED: Pobiera szczegóły agenta z intelligence metrics i background insights"""
        try:
            result = await agent_manager.get_agent(agent_id)
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": str(e)
            }, indent=2, ensure_ascii=False)

    @server.tool()
    async def list_agents(
        domain: str = "all",
        status: str = "all", 
        sort_by: str = "created",
        ctx: Context = None
    ) -> str:
        """📋 ENHANCED: Lista agentów z inteligentnymi filtrami i sortowaniem według intelligence score"""
        try:
            result = await agent_manager.list_agents(domain, status, sort_by)
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": str(e)
            }, indent=2, ensure_ascii=False)

    @server.tool()
    async def test_agent(
        agent_id: str,
        test_input: Dict[str, Any],
        test_scenario: str = "standard_test",
        ctx: Context = None
    ) -> str:
        """🧪 ENHANCED: Testuje agenta z zaawansowaną analizą wydajności i uczeniem się z wyników"""
        try:
            result = await agent_manager.test_agent(agent_id, test_input, test_scenario)
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": str(e)
            }, indent=2, ensure_ascii=False)

    @server.tool()
    async def get_components(
        category: str = "all",
        domain: str = "all",
        search_query: str = "",
        ctx: Context = None
    ) -> str:
        """🔧 Pobiera wszystkie dostępne komponenty (500+) z inteligentnym filtrowaniem"""
        try:
            config = ctx.session_config if ctx else None
            max_components = config.max_components if config else 50
            
            result = await component_manager.get_components(
                category=category, 
                domain=domain, 
                search_query=search_query,
                limit=max_components
            )
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": str(e)
            }, indent=2, ensure_ascii=False)

    @server.tool()
    async def add_component_to_agent(
        agent_id: str,
        component_id: str,
        configuration: Optional[Dict[str, Any]] = None,
        ctx: Context = None
    ) -> str:
        """⚡ ENHANCED: Dodaje komponent do agenta z inteligentną auto-konfiguracją i walidacją kompatybilności"""
        try:
            result = await agent_manager.add_component_to_agent(
                agent_id, component_id, configuration
            )
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": str(e)
            }, indent=2, ensure_ascii=False)

    @server.tool()
    async def generate_chat_interface(
        agent_id: str,
        theme: str = "modern",
        ctx: Context = None
    ) -> str:
        """💬 Generuje responsywny interfejs czatu HTML5 z zaawansowanymi funkcjami"""
        try:
            result = await workflow_manager.generate_chat_interface(agent_id, theme)
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": str(e)
            }, indent=2, ensure_ascii=False)

    @server.tool()
    async def deploy_agent(
        agent_id: str,
        environment: str = "local",
        ctx: Context = None
    ) -> str:
        """🚀 Wdraża agenta do środowiska produkcyjnego"""
        try:
            result = await deployer.deploy_agent(agent_id, environment)
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": str(e)
            }, indent=2, ensure_ascii=False)

    @server.tool()
    async def delete_agent(agent_id: str, confirm: bool = False, ctx: Context = None) -> str:
        """🗑️ ENHANCED: Bezpieczne usuwanie agenta z weryfikacją i backup"""
        try:
            if not confirm:
                return json.dumps({
                    "success": False,
                    "error": "Confirmation required",
                    "message": "Set confirm=True to delete the agent"
                }, indent=2, ensure_ascii=False)
            
            result = await agent_manager.delete_agent(agent_id)
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": str(e)
            }, indent=2, ensure_ascii=False)

    print("✅ FastMCP Server created with all tools and resources!")
    return server