from nltk import word_tokenize, corpus
from nltk.corpus import conll2000
from nltk.stem import RSLPStemmer

class Main:
    def __init__(self):
        self.LANGUAGE = 'english'
        self.stopwords = set(corpus.stopwords.words(self.LANGUAGE))
        self.classifications = []

        for(word, classification) in conll2000.tagged_words():
            if '+' in classification:
                self.classification = classification[classification.index('+') + 1:]

            self.classifications.append((word.lower(), classification))

    def main(self, text):
        print('getting tokens: ')

        tokens = self.get_token(self, text)
        self.print_tokens(tokens)

        self.grammar_tag(self,tokens)

        print('removing stopwords: ')

        tokens = self.remove_stopwords(self, tokens)
        self.print_tokens(tokens)

        self.stematize(tokens)
    
    @staticmethod
    def get_token(self, text):
        tokens = word_tokenize(text, self.LANGUAGE)

        return tokens

    @staticmethod
    def print_tokens(tokens):
        for token in tokens:
            print(token)

    @staticmethod
    def remove_stopwords(self, tokens):
        filtered_tokens = []

        for token in tokens:
            if token not in self.stopwords:
                filtered_tokens.append(token)

        return filtered_tokens

    @staticmethod
    def grammar_tag(self, tokens):
        for token in tokens:
            for (word, classification) in self.classifications:
                if token == word:
                    print('token ' + token + ' = ', classification)

                    break

    @staticmethod
    def stematize(tokens):
        stemmer = RSLPStemmer()

        for token in tokens:
            print(stemmer.stem(token))
        
start = Main()
text = 'Hollywood is bleeding, vampires feeding Darkness turns to dust'

start.main(text)