def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])
print(reverse_words("I go to school every day"))