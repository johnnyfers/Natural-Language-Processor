from nltk import word_tokenize, corpus
from nltk.corpus import conll2000
from nltk.stem import RSLPStemmer

LANGUAGE = 'english'

def init():
    global stopwords
    global classifications

    stopwords = set(corpus.stopwords.words(LANGUAGE))
    classifications = []

    for(word, classification) in conll2000.tagged_words():
        if '+' in classification:
            classification = classification[classification.index('+') + 1:]

        classifications.append((word.lower(), classification))


def get_token(text):
    tokens = word_tokenize(text, LANGUAGE)

    return tokens

def print_tokens(tokens):
    for token in tokens:
        print(token)


def remove_stopwords(tokens):
    global stopwords
    
    filtered_tokens = []
    
    for token in tokens:
        if token not in stopwords:
            filtered_tokens.append(token)
    
    return filtered_tokens


def grammar_tag(tokens):
    global classifications
    
    for token in tokens:
        for (word, classification) in classifications:
            if token == word:
                print('token ' + token + ' = ', classification)
                
                break
                


def stematize(tokens):
    stemmer = RSLPStemmer()

    for token in tokens:
        print(stemmer.stem(token))

if __name__ == '__main__':
    init()

    text = 'Hollywood is bleeding, vampires feeding Darkness turns to dust' # post malone
    
    print('getting tokens: ')
    
    tokens = get_token(text)
    print_tokens(tokens)
    
    grammar_tag(tokens)

    print('removing stopwords: ')
    
    tokens = remove_stopwords(tokens)
    print_tokens(tokens)
    
    stematize(tokens)
