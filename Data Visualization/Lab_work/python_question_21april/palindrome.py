def palindrome_analyzer(sentences):
    freq = {}

    for sentence in sentences:
        words = sentence.lower().split()

        for word in words:
            clean = word.strip('.,!?')

            if clean == clean[::-1]:
                freq[clean] = freq.get(clean, 0) + 1

    return freq