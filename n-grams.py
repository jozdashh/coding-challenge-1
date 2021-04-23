# Coding challenge: n-gram algorithms
# Author: Josue Peña Atencio
# Date: 23-04-2021

# N: amount of characters in 'text'
# n: amount of n-grams

# Upper bound time-complexity: O(N) + O(N-n) + O(n) = O(N)
def calculate_n_grams(text, n):
    ngrams = list()
    # Remove leading and trailing whitespace
    text = text.strip() # O(N)
    for i in range(len(text)-n+1): # O(N-n)
        ngrams.append(text[i:i+n]) # O(n) Python list slices depend on both indices: i+n - i = n
    return ngrams


# Upper bound time-complexity: O(N) + O(N-n) = O(N)
def most_frequent_n_gram(text, n):
    ngrams = calculate_n_grams(text,n) # O(N)
    count = dict()
    current_max = 1
    answer = ''
    for gram in ngrams: # O(N-n)
        if gram not in count: # O(1) Python dictionary lookups are constant
            count[gram] = 1
        else:
            count[gram] += 1
            if count[gram] > current_max:
                current_max = count[gram]
                answer = gram
    return answer
