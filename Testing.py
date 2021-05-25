s = "Hello"

def toLowerCase(s: str) -> str:
    if len(s) <= 1 or len(s) >= 100:
        return s

    return s.lower()

print(toLowerCase("Hello"))

#print(s.lower())
