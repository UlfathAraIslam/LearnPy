def word_frequency(text):
    counts={}
    words = text.split()

    for word in words:
        # Get the value for this word. If it doesn't exist, give me 0.
        counts[word] = counts.get(word,0) + 1
    return counts
print (word_frequency("time series time forecast series time model"))