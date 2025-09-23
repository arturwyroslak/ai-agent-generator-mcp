import sys
import os
from typing import Dict, Any, List

# Add the src directory to the path for absolute imports
current_dir = os.path.dirname(__file__)
src_dir = os.path.dirname(current_dir)
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

try:
    from components import get_all_available_components, search_components
except ImportError as e:
    print(f"Warning: Could not import components: {e}")
    
    def get_all_available_components():
        return {}
    
    def search_components(query, category=None):
        return []

class ComponentManager:
    def __init__(self):
        self.component_catalog = get_all_available_components()
    
    async def get_components(self, category: str = None, search: str = None) -> Dict[str, Any]:
        """Pobiera komponenty z inteligentnym filtrowaniem"""
        
        if search:
            components = search_components(search, category)
        else:
            if category and category != "all":
                components = self.component_catalog.get(category, [])
            else:
                # Flatten all components
                components = []
                for cat_name, cat_components in self.component_catalog.items():
                    if isinstance(cat_components, list):
                        for comp in cat_components:
                            comp["category_parent"] = cat_name
                            components.append(comp)
                    elif cat_name == "statistics":  # Skip stats
                        continue
        
        return {
            "success": True,
            "components": components[:100],  # Limit for performance
            "total_available": len(components),
            "category_filter": category,
            "search_query": search,
            "categories_available": list(self.component_catalog.keys())
        }