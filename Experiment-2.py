# using nltk package
from nltk.corpus import stopwords
import string
import nltk
from nltk.stem.porter import *
from collections import Counter
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import wordpunct_tokenize,sent_tokenize
# nltk.download('wordnet')
# nltk.download('omw-1.4')
lemmat = WordNetLemmatizer()
stemmer = PorterStemmer()

stops = set(stopwords.words('english'))
stops.add('')
# Hamlet doc
sentences = sent_tokenize(open('hamlet.txt','r').read().lower())
tokenized = []
for x in sentences:
    tokenized+=wordpunct_tokenize(x)
print(len(tokenized))
# Tokenize
fl = open('hamlet.txt','r').read().lower().replace('\n',' ').replace('\t','').translate(str.maketrans('','',string.punctuation)).split(' ')
filtered = [x for x in fl if x not in stops]
stemmed = [stemmer.stem(x) for x in filtered]
print(len(filtered))
print(Counter(stemmed).most_common(10))
# We see stemmer has left somethings out like delivery to deliv
# Thus lemmatizer
lemmed = [lemmat.lemmatize(x) for x in filtered]
print(len(lemmed))
print(Counter(lemmed).most_common(10))
tokenized_lemm = [lemmat.lemmatize(x) for x in tokenized if x not in stops]
print(Counter(tokenized_lemm).most_common(10))