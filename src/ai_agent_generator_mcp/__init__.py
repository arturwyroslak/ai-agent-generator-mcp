"""AI Agent Generator MCP - Create AI agents through natural language"""

__version__ = "1.0.0"
__author__ = "AI Agent Generator MCP"
__description__ = "MCP Server that enables AI to create other AI agents through natural language"

# Re-export main server function for easy access
from .server import create_server

__all__ = ["create_server"]