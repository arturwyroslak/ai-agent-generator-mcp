from .ai_components import get_ai_components
from .integrations import get_integration_components
from .data_tools import get_data_components
from .workflow_tools import get_workflow_components
from .workflow_templates import get_workflow_templates

def get_all_available_components():
    """Zwraca wszystkie dostępne komponenty podzielone na kategorie"""
    return {
        "ai_processing": get_ai_components(),
        "integrations": get_integration_components(),
        "data_tools": get_data_components(),
        "workflow_control": get_workflow_components(),
        "templates": get_workflow_templates()
    }

def get_components_by_category(category):
    """Zwraca komponenty dla konkretnej kategorii"""
    all_components = get_all_available_components()
    return all_components.get(category, [])

def get_component_by_id(component_id):
    """Znajduje komponent po ID"""
    all_components = get_all_available_components()
    
    for category_name, components in all_components.items():
        for component in components:
            if component.get("component_id") == component_id or component.get("template_id") == component_id:
                return component
    
    return None

def search_components(query, category=None):
    """Wyszukuje komponenty po nazwie lub opisie"""
    results = []
    all_components = get_all_available_components()
    
    query_lower = query.lower()
    
    for category_name, components in all_components.items():
        if category and category != category_name:
            continue
            
        for component in components:
            # Szukaj w nazwie
            if query_lower in component.get("name", "").lower():
                results.append({**component, "category": category_name})
                continue
                
            # Szukaj w opisie
            if query_lower in component.get("description", "").lower():
                results.append({**component, "category": category_name})
                continue
                
            # Szukaj w capabilities
            capabilities = component.get("capabilities", [])
            if any(query_lower in cap.lower() for cap in capabilities):
                results.append({**component, "category": category_name})
                continue
    
    return results

def get_components_stats():
    """Zwraca statystyki komponentów"""
    all_components = get_all_available_components()
    
    stats = {
        "total_components": 0,
        "by_category": {},
        "by_type": {},
        "total_capabilities": set()
    }
    
    for category_name, components in all_components.items():
        stats["by_category"][category_name] = len(components)
        stats["total_components"] += len(components)
        
        for component in components:
            component_type = component.get("type", "unknown")
            stats["by_type"][component_type] = stats["by_type"].get(component_type, 0) + 1
            
            # Zbierz wszystkie capabilities
            capabilities = component.get("capabilities", [])
            stats["total_capabilities"].update(capabilities)
    
    stats["total_capabilities"] = len(stats["total_capabilities"])
    
    return stats