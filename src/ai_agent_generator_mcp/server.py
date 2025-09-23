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
    
    # Simplified imports to avoid circular dependencies
    # Add the src directory to sys.path for absolute imports
    import sys
    import os
    current_dir = os.path.dirname(__file__)
    src_dir = os.path.dirname(os.path.dirname(current_dir))
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)
    
    try:
        from tools.enhanced_agent_manager import EnhancedAgentManager
        from tools.component_manager import ComponentManager  
        from tools.workflow_manager import WorkflowManager
        from tools.deployer import AgentDeployer
        
        agent_manager = EnhancedAgentManager()
        component_manager = ComponentManager()
        workflow_manager = WorkflowManager()
        deployer = AgentDeployer()
        
        print("🤖 Inicjalizacja Enhanced Agent Manager z AI...")
        print("📊 Background Intelligence: AKTYWNA")
    except ImportError as e:
        print(f"⚠️ Warning: Could not import advanced managers: {e}")
        print("🔄 Using basic functionality...")
        
        # Fallback to basic functionality
        agent_manager = None
        component_manager = None
        workflow_manager = None
        deployer = None
    
    # Register resources using the decorator approach
    @server.resource("components://catalog", 
                    name="Katalog Komponentów",
                    description="500+ inteligentnych komponentów AI",
                    mime_type="application/json")
    async def get_components_catalog() -> str:
        """Katalog 500+ inteligentnych komponentów AI"""
        try:
            if component_manager:
                components = await component_manager.get_all_components()
            else:
                components = []
            
            context_data = {
                "total_components": len(components),
                "categories": list(set([c.get("category", "unknown") for c in components])) if components else [],
                "domains": ["customer_service", "sales", "marketing", "hr", "finance", "development", "analytics", "ecommerce", "general"],
                "intelligence_features": {
                    "nlp_analysis": True,
                    "auto_configuration": True,
                    "smart_suggestions": True,
                    "background_learning": True
                },
                "components_sample": components[:10] if components else [],
                "max_components_per_agent": 50,
                "status": "full" if component_manager else "basic"
            }
            return json.dumps(context_data, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"error": str(e), "status": "error"}, indent=2)
    
    @server.resource("intelligence://context",
                    name="Smart Context", 
                    description="AI learned patterns i intelligence insights",
                    mime_type="application/json")
    async def get_intelligence_context() -> str:
        """AI learned patterns i intelligence insights"""
        try:
            # Get smart context from agent manager
            if agent_manager and hasattr(agent_manager, 'smart_context'):
                context_data = await agent_manager.smart_context.get_intelligence_insights()
            else:
                context_data = {
                    "learned_patterns": [],
                    "success_metrics": {},
                    "optimization_suggestions": [],
                    "background_intelligence": "Basic" if not agent_manager else "Active",
                    "status": "basic" if not agent_manager else "full"
                }
            return json.dumps(context_data, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"error": str(e), "status": "error"}, indent=2)

    @server.tool()
    async def create_agent(
        name: str,
        description: str,
        domain: str = "general", 
        complexity: str = "medium",
        ctx: Context = None
    ) -> str:
        """🤖 ENHANCED: Tworzy inteligentnego agenta AI z automatyczną analizą NLP, wykrywaniem wymagań i generowaniem interfejsu chatu"""
        try:
            # Get session configuration
            config = ctx.session_config if ctx else None
            
            if agent_manager:
                result = await agent_manager.create_agent(
                    name=name,
                    description=description, 
                    domain=domain,
                    complexity=complexity
                )
                
                # Add success message with specific guidance based on result
                if result.get("success") and result.get("chat_interface", {}).get("generated"):
                    result["message"] = f"🎉 Agent '{name}' został pomyślnie utworzony z pełną automatyczną konfiguracją! Interfejs chatu HTML jest gotowy do pobrania i testów."
                    result["ready_to_use"] = True
                elif result.get("success"):
                    result["message"] = f"✅ Agent '{name}' został utworzony z zaawansowaną inteligencją AI. Interfejs chatu można wygenerować osobno."
                    result["ready_to_use"] = True
                    
            else:
                # This should not happen in production, but provide fallback
                import uuid
                from datetime import datetime
                
                agent_id = str(uuid.uuid4())
                result = {
                    "success": False,
                    "error": "Advanced agent manager not available. Please check server configuration.",
                    "agent_id": None,
                    "ready_to_use": False,
                    "troubleshooting": {
                        "issue": "Enhanced AI components not loaded",
                        "solution": "Restart server or check import dependencies",
                        "fallback": "Manual component configuration required"
                    }
                }
            
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": str(e),
                "ai_analysis": "Failed to analyze agent requirements",
                "troubleshooting": {
                    "error_type": type(e).__name__,
                    "suggestion": "Check server logs for detailed error information"
                }
            }, indent=2, ensure_ascii=False)

    @server.tool()
    async def get_agent(agent_id: str, ctx: Context = None) -> str:
        """📊 ENHANCED: Pobiera szczegóły agenta z intelligence metrics i background insights"""
        try:
            if agent_manager:
                result = await agent_manager.get_agent(agent_id)
            else:
                result = {
                    "success": False,
                    "error": "Agent management not available in basic mode",
                    "basic_mode": True
                }
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
            if agent_manager:
                result = await agent_manager.list_agents(domain, status, sort_by)
            else:
                result = {
                    "success": True,
                    "agents": [],
                    "total_count": 0,
                    "basic_mode": True,
                    "message": "Agent listing not available in basic mode"
                }
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
            if agent_manager:
                result = await agent_manager.test_agent(agent_id, test_input, test_scenario)
            else:
                result = {
                    "success": False,
                    "error": "Agent testing not available in basic mode",
                    "basic_mode": True
                }
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
            
            if component_manager:
                result = await component_manager.get_components(
                    category=category, 
                    domain=domain, 
                    search_query=search_query,
                    limit=max_components
                )
            else:
                result = {
                    "success": False,
                    "error": "Component manager not available. Please check server configuration.",
                    "components": [],
                    "total_count": 0,
                    "troubleshooting": {
                        "issue": "Enhanced component system not loaded",
                        "solution": "Restart server or check import dependencies"
                    }
                }
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
            if agent_manager:
                result = await agent_manager.add_component_to_agent(
                    agent_id, component_id, configuration
                )
            else:
                result = {
                    "success": False,
                    "error": "Component addition not available - agent manager not initialized",
                    "troubleshooting": {
                        "issue": "Enhanced agent management system not loaded",
                        "solution": "Restart server or check import dependencies"
                    }
                }
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
            if deployer:
                result = await deployer.generate_chat_interface(agent_id, theme)
            else:
                result = {
                    "success": False,
                    "error": "Chat interface generation not available - deployer not initialized",
                    "fallback_available": False
                }
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
            if deployer:
                result = await deployer.deploy_agent(agent_id, environment)
            else:
                result = {
                    "success": False,
                    "error": "Agent deployment not available in basic mode",
                    "basic_mode": True
                }
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
            
            if agent_manager:
                result = await agent_manager.delete_agent(agent_id)
            else:
                result = {
                    "success": False,
                    "error": "Agent deletion not available in basic mode",
                    "basic_mode": True
                }
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": str(e)
            }, indent=2, ensure_ascii=False)

    print("✅ FastMCP Server created with all tools and resources!")
    return server