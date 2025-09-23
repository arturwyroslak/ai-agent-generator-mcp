from typing import Dict, Any, List

class WorkflowManager:
    def __init__(self):
        pass
        
    async def get_workflow_templates(self, domain: str = None, complexity: str = None) -> Dict[str, Any]:
        """Pobiera szablony workflow"""
        import sys
        import os
        current_dir = os.path.dirname(__file__)
        src_dir = os.path.dirname(current_dir)
        if src_dir not in sys.path:
            sys.path.insert(0, src_dir)
            
        try:
            from components.workflow_templates import get_workflow_templates
            templates = get_workflow_templates()
        except ImportError:
            templates = []
        filtered = []
        
        for template in templates:
            # Filtrowanie po domenie
            if domain and template.get("domain") != domain:
                continue
            # Filtrowanie po złożoności  
            if complexity and template.get("complexity") != complexity:
                continue
            filtered.append(template)
        
        return {
            "success": True,
            "templates": filtered,
            "total_available": len(filtered)
        }