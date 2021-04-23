
def calculate_n_grams(text, n):
    ngrams = list()
    text = text.strip()
    for i in range(len(text)-n+1):
        tmp = [ text[j] for j in range(i,i+n) ]
        ngrams.append("".join(tmp))
    return ngrams

def most_frequent_n_gram(text, n):
    ngrams = calculate_n_grams(text,n)
    count = dict()
    current_max = 1
    answer = ''
    for gram in ngrams:
        if gram not in count:
            count[gram] = 1
        else:
            count[gram] += 1
            if count[gram] > current_max:
                current_max = count[gram]
                answer = gram
    return ans
