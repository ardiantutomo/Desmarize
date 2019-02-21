from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
import re


def summarize(content):
    #token = sent_tokenize(content)
    content = sanitize_input(content)
    sentence_tokens, word_tokens = tokenize_content(content)  
    sentence_ranks = scoring(word_tokens, sentence_tokens)
    summarize_length = 1 #summarize to sentence that have same rank(max)

    indexes = nlargest(int(summarize_length), sentence_ranks, key=sentence_ranks.get)
    final_sentences = [sentence_tokens[j] for j in sorted(indexes)]
    result = ' '.join(final_sentences) 
    # re.sub("[[0-9]*]","",result)
    return ' '.join(result) 

def scoring(filterd_words, sentence_tokens):
    freq = FreqDist(filterd_words) # get frequency of word

    ranking = defaultdict(int)

    for i, sentence in enumerate(sentence_tokens):
        for word in word_tokenize(sentence.lower()):
            if word in freq:
                ranking[i] += freq[word]
                
    return ranking


def tokenize_content(content):
    stop_words = set(stopwords.words('english') + list(punctuation))
    words = word_tokenize(content.lower())    
    return [
        sent_tokenize(content),
        [word for word in words if word not in stop_words]    
    ]


def sanitize_input(data):
    replace = {
        ord('\f') : ' ',
        ord('\t') : ' ',
        ord('\n') : ' ',
        ord('\v') : ' ',
        ord('\r') : None
    }

    return data.translate(replace)

