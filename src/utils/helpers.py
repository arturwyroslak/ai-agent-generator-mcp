import uuid
import json
import re
from typing import Any, Dict, List, Optional
from datetime import datetime

def generate_unique_id(prefix: str = "") -> str:
    """Generuje unikalny identyfikator"""
    unique_id = str(uuid.uuid4())
    if prefix:
        return f"{prefix}_{unique_id}"
    return unique_id

def validate_json_schema(data: Dict[str, Any], schema: Dict[str, Any]) -> Dict[str, Any]:
    """Podstawowa walidacja JSON schema"""
    errors = []
    
    # Sprawdź wymagane pola
    required_fields = schema.get("required", [])
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    
    # Sprawdź typy
    properties = schema.get("properties", {})
    for field, field_schema in properties.items():
        if field in data:
            expected_type = field_schema.get("type")
            actual_value = data[field]
            
            if not _validate_type(actual_value, expected_type):
                errors.append(f"Invalid type for field {field}: expected {expected_type}")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors
    }

def _validate_type(value: Any, expected_type: str) -> bool:
    """Waliduje typ wartości"""
    type_mapping = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict
    }
    
    expected_python_type = type_mapping.get(expected_type)
    if expected_python_type is None:
        return True  # Unknown type, assume valid
    
    return isinstance(value, expected_python_type)

def sanitize_string(text: str, max_length: int = 1000) -> str:
    """Czyści i sanityzuje tekst"""
    if not isinstance(text, str):
        text = str(text)
    
    # Usuń niebezpieczne znaki
    text = re.sub(r'[<>"\']', '', text)
    
    # Ogranicz długość
    if len(text) > max_length:
        text = text[:max_length] + "..."
    
    return text.strip()

def format_timestamp(dt: datetime = None) -> str:
    """Formatuje timestamp"""
    if dt is None:
        dt = datetime.now()
    return dt.isoformat()

def parse_configuration(config: Dict[str, Any], defaults: Dict[str, Any] = None) -> Dict[str, Any]:
    """Parsuje i waliduje konfigurację"""
    if defaults is None:
        defaults = {}
    
    # Scal z domyślnymi wartościami
    result = {**defaults, **config}
    
    # Waliduj kluczowe pola
    if "temperature" in result:
        temp = result["temperature"]
        if not isinstance(temp, (int, float)) or temp < 0 or temp > 2:
            result["temperature"] = 0.7
    
    if "max_tokens" in result:
        tokens = result["max_tokens"]
        if not isinstance(tokens, int) or tokens < 1:
            result["max_tokens"] = 1000
    
    return result

def extract_urls_from_text(text: str) -> List[str]:
    """Wyciąga URL-e z tekstu"""
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.findall(url_pattern, text)

def extract_emails_from_text(text: str) -> List[str]:
    """Wyciąga adresy email z tekstu"""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

def calculate_text_similarity(text1: str, text2: str) -> float:
    """Oblicza podobieństwo między tekstami (prosty algorytm)"""
    if not text1 or not text2:
        return 0.0
    
    # Konwertuj do małych liter i podziel na słowa
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    
    # Oblicz Jaccard similarity
    intersection = len(words1.intersection(words2))
    union = len(words1.union(words2))
    
    if union == 0:
        return 0.0
    
    return intersection / union

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    """Dzieli tekst na mniejsze części z nakładaniem"""
    if len(text) <= chunk_size:
        return [text]
    
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        
        # Znajdź najlepsze miejsce podziału (koniec zdania)
        if end < len(text):
            last_period = chunk.rfind('.')
            last_newline = chunk.rfind('\n')
            split_point = max(last_period, last_newline)
            
            if split_point > start + chunk_size // 2:
                chunk = text[start:start + split_point + 1]
                end = start + split_point + 1
        
        chunks.append(chunk.strip())
        start = end - overlap
        
        if start >= len(text):
            break
    
    return chunks

def estimate_tokens(text: str) -> int:
    """Szacuje liczbę tokenów w tekście"""
    # Prosty szacunek: ~4 znaki na token
    return len(text) // 4

def format_file_size(size_bytes: int) -> str:
    """Formatuje rozmiar pliku"""
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    import math
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    
    return f"{s} {size_names[i]}"

def is_valid_email(email: str) -> bool:
    """Sprawdza czy email ma poprawny format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_url(url: str) -> bool:
    """Sprawdza czy URL ma poprawny format"""
    pattern = r'^https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:\w*))?)?$'
    return re.match(pattern, url) is not None

def merge_dictionaries(dict1: Dict[str, Any], dict2: Dict[str, Any], deep: bool = True) -> Dict[str, Any]:
    """Łączy słowniki z opcją głębokiego łączenia"""
    if not deep:
        return {**dict1, **dict2}
    
    result = dict1.copy()
    
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dictionaries(result[key], value, deep=True)
        else:
            result[key] = value
    
    return result

def flatten_dictionary(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Spłaszcza zagnieżdżony słownik"""
    items = []
    
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        
        if isinstance(v, dict):
            items.extend(flatten_dictionary(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    
    return dict(items)

def safe_json_loads(json_str: str, default: Any = None) -> Any:
    """Bezpieczne parsowanie JSON"""
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, TypeError):
        return default

def safe_json_dumps(obj: Any, default: str = "{}") -> str:
    """Bezpieczne serializowanie JSON"""
    try:
        return json.dumps(obj, ensure_ascii=False, indent=2)
    except (TypeError, ValueError):
        return default