# Coding challenge: n-gram algorithms
# Author: Josue Peña Atencio
# Date: 23-04-2021

# N: amount of characters in 'text'
# n: amount of n-grams

# Even if n = N, time complexity is still bounded by N

# Upper bound time complexity: O(N) + O(N-n)*O(n)
def calculate_n_grams(text, n):
    assert 0 < n <= len(text)
    ngrams = list()
    # Remove leading and trailing whitespace
    text = text.strip() # O(N)
    for i in range(len(text)-n+1): # O(N-n)
        ngrams.append(text[i:i+n]) # O(n) Python list slices depend on both indexes: (i+n) - (i) = n
    return ngrams


# Upper bound time complexity: O(N) + O(N-n) + O(N-n)*O(n)
def most_frequent_n_gram(text, n):
    assert 0 < n <= len(text)
    ngrams = calculate_n_grams(text,n) # O(N) + O(N-n)*O(n)
    count = dict()
    current_max = 1
    answer = ngrams[0]
    for gram in ngrams: # O(N-n)
        if gram not in count: # O(1) Python dictionary lookups are constant
            count[gram] = 1
        else:
            count[gram] += 1
            if count[gram] > current_max:
                current_max = count[gram]
                answer = gram
    return answer
