def is_palindrome_phrase(phrase):
    cleaned = phrase.lower().replace(" ","")
    return cleaned == cleaned[::-1]