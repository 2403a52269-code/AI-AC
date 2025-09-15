import re

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'[^a-z0-9\-]', '', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    return text

samples = ['Hello World!', 'AI & You', 'Set1-C2']
slugs = [slugify(s) for s in samples]
print(','.join(f"'{s}'" for s in slugs))