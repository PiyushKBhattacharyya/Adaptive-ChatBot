import re

def clean_text(text: str) -> str:
    """Removes special characters and excessive whitespace."""
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.lower()
