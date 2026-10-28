"""Quick helpers."""

def load_lines(path):
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]

def clamp(value, low, high):
    return max(low, min(value, high))

if __name__ == "__main__":
    print(clamp(2, 0, 5))

# cleanup later
