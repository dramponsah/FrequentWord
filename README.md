# FrequentWord
This code accepts a string of  DNA sequence and k-mer length and returns the most frequent k-mer from the sequence.
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
