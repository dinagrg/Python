from collections import defaultdict, Counter
import pprint

# Define corpus
corpus = [
    ["<s>", "a", "b", "c", "</s>"],
    ["<s>", "a", "b", "d", "</s>"],
    ["<s>", "x", "y", "z", "</s>"],
    ["<s>", "x", "b", "c", "</s>"]
]
# Flatten corpus to get all tokens for unigram count
tokens = [token for sentence in corpus for token in sentence]

# Step 1: Unigram and Bigram counts
unigram_counts = Counter(tokens)
bigram_counts = Counter()

for sentence in corpus:
    for i in range(len(sentence) - 1):
        bigram = (sentence[i], sentence[i + 1])
        bigram_counts[bigram] += 1

# Vocabulary
vocabulary = sorted(set(tokens))
V = len(vocabulary)

# Print Vocabulary and Counts
print(f"\nVocabulary (V = {V}):\n{vocabulary}\n")
print("Unigram Counts:")
pprint.pprint(dict(unigram_counts))
print("\nBigram Counts:")
pprint.pprint(dict(bigram_counts))

# Define bigrams to calculate
bigram_list = [("a", "b"), ("b", "c"), ("y", "z"), ("x", "y"), ("a", "d"), ("x", "a")]

# Task 2: MLE
print("\n--- Task 2: MLE ---")
for w1, w2 in bigram_list:
    prob = bigram_counts.get((w1, w2), 0) / unigram_counts.get(w1, 1)  # avoid zero-division
    print(f"P({w2}|{w1}) = {prob:.4f}")

# Task 3: Add-one Smoothing
print("\n--- Task 3: Add-one Smoothing ---")
for w1, w2 in bigram_list:
    numerator = bigram_counts.get((w1, w2), 0) + 1
    denominator = unigram_counts.get(w1, 0) + V
    prob = numerator / denominator
    print(f"P({w2}|{w1}) = {prob:.4f}")

# Task 4: Add-k Smoothing (k = 0.1)
k = 0.1
print(f"\n--- Task 4: Add-k Smoothing (k = {k}) ---")
for w1, w2 in bigram_list:
    numerator = bigram_counts.get((w1, w2), 0) + k
    denominator = unigram_counts.get(w1, 0) + k * V
    prob = numerator / denominator
    print(f"P({w2}|{w1}) = {prob:.4f}")