def reverse_words(sentence):
    words = sentence.split()
    reverse_words = words[::-1]
    return " " .join(reverse_words)
print(reverse_words("hello world"))