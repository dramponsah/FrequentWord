def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        words.append(key)
    return words

Text='ACGTTGCATGTCGCATGATGCATGAGAGCT'
k=5
print(FrequentWords(Text,k),FrequentMap(Text,k))
