def normalize_name(raw):
    parts = raw.strip().split()
    return " ".join(word.title() for word in parts)
print(normalize_name("  rafi   islam  "))