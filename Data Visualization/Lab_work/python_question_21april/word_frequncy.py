def word_frequency(filename, stop_words):
    freq = {}

    with open(filename, 'r') as f:
        for line in f:
            words = line.lower().split()
            for word in words:
                word = word.strip('.,!?')

                if word in stop_words or not word:
                    continue

                freq[word] = freq.get(word, 0) + 1

    top_10 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_10