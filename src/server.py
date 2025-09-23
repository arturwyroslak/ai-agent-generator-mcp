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
    
    @server.resource("components://catalog")
    async def get_components_catalog(ctx: Context) -> str:
        """Katalog 500+ inteligentnych komponentów AI"""
        # Get configuration from session
        config = ctx.session_config
        
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
                "max_components_per_agent": config.max_components if config else 50
            }
            return json.dumps(context_data, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)
    
    @server.resource("intelligence://context")
    async def get_intelligence_context(ctx: Context) -> str:
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


# Keep the old main function for backward compatibility during development
async def main():
    """Uruchomienie serwera z FULL ENHANCED FEATURES - legacy mode"""
    print("🚀 LEGACY MODE: Using old server structure...")
    print("⚠️  For Smithery.ai deployment, use the create_server() function")
    
    # Create a simple FastMCP server for local testing
    server = create_server()
    
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
    
    # Run server using FastMCP's built-in functionality
    try:
        # Use the run method from FastMCP
        await server.run_stdio()
    except AttributeError:
        # Fallback to basic stdio if run_stdio is not available
        print("🔄 Using fallback stdio mode...")
        from mcp.server.stdio import stdio_server
        async with stdio_server() as (read_stream, write_stream):
            await server.run(read_stream, write_stream)

if __name__ == "__main__":
    import uuid
    from datetime import datetime
    asyncio.run(main())