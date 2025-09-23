"""AI Agent Generator MCP Server

A sophisticated MCP server for creating and managing AI agents
with intelligent background processing and advanced component system.
"""

__version__ = "1.0.0"
__author__ = "AI Agent Generator MCP"

from .ai_agent_generator_mcp.server import create_server

__all__ = ["create_server"]