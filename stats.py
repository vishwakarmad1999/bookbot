from typing import Dict, List, Any


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def get_num_words(path: str) -> int:
    text = get_book_text(path)
    return len(text.split())


def get_characters_dict(path: str) -> Dict[str, int]:
    d = {}
    text = get_book_text(path).lower()
    for ch in text:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    
    return d

def get_sorted_chars_list(path: str) -> List[Dict[str, Any]]:
    d = get_characters_dict(path)
    l = []
    for k, v in d.items():
        l.append({
            "char": k,
            "num": v,
        })
        l.sort(reverse=True, key=lambda x: x["num"])

    return l
