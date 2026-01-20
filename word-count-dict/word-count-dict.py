def word_count_dict(sentences):
    """
    sentences: list[list[str]]
    returns: dict[str, int]
    """
    freq = {}

    for sentence in sentences:
        for word in sentence:
            freq[word] = freq.get(word, 0) + 1

    return freq
