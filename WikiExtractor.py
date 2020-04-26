import requests
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import operator



#One time download
#   nltk.download('wordnet')
nltk.download('punkt')

# print(nltk.corpus.__file__)

# wikisubjects=["Cricket","2011_Cricket_World_Cup","Ranji_Trophy","Indian_Premier_League"]
# for wikisubject in wikisubjects:
#     print( "loop ", wikisubject)
#     response = requests.get(
#         'https://en.wikipedia.org/w/api.php',
#         params={
#             'action': 'query',
#             'format': 'json',
#             'titles': wikisubject,
#             'prop': 'extracts',
#             'explaintext': True,
#         }
#     ).json()
#     page = next(iter(response['query']['pages'].values()))
#     f=open("C:\\uo\SWeb\Assignment 4\CricketData.txt", "a+",encoding="utf-8");
#     f.write(page['extract'].lower())
#     print(wikisubject," appended to file \n ")

####################################
# cricketCorpus = nltk.corpus.reader.PlaintextCorpusReader(
#     r"C:\Users\harip\AppData\Roaming\nltk_data\corpora\Cricket",
#     r'(?!\.).*\.txt',
#     encoding="ascii")
#
# print (cricketCorpus)

corpusdir = r"C:\Users\harip\AppData\Roaming\nltk_data\corpora\Cricket" # Directory of corpus.
newcorpus = PlaintextCorpusReader(corpusdir, '.*')
corpus=(newcorpus.raw())


# tokenized_words =word_tokenize(corpus)

# #tokenization
# RegexTokenizer = RegexpTokenizer(r'\w+')
# tokenized_words=RegexTokenizer.tokenize(corpus)
#
# #removing stop words
# stop_words=set(stopwords.words("english"))
# stop_words.add('The')
# # print(type(stop_words))
# # print(stop_words)
# filtered_words=[]
# for w in tokenized_words:
#     if w not in stop_words:
#         filtered_words.append(w)
# #print(filtered_words)
#
# #Stemming
# ps=PorterStemmer()
# stemmed_words=[]
# for word in filtered_words:
#     stemmmed_word=ps.stem(word)
#     #if(stemmmed_word not in stemmed_words):
#     stemmed_words.append(stemmmed_word)
# print ( "\nAfter removing stop words\n")
# print(filtered_words)
# print(len(filtered_words))
# print ( "\nAfter stemming\n")
# print(stemmed_words)
# print(len(stemmed_words))
#
#
# #Lemmatization
# lemmatized_words=[]
# lemma= WordNetLemmatizer()
# for word in filtered_words:
#     lemmatized_word=lemma.lemmatize(word)
#     #if(lemmatized_word not in lemmatized_word):
#     lemmatized_words.append(lemmatized_word)
#
# print ( "\nAfter lemmatization\n")
# print(lemmatized_words)
# print(len(lemmatized_words))
#
# # logic to calculate keywords
# keywords={}
# type(keywords)
# for word in lemmatized_words:
#     if (word not in keywords.keys()):
#         keywords[word]=1
#     else:
#         keywords[word]=keywords[word]+1;
#
# print (len(keywords))
# print (keywords)
# sorted_keywords= sorted(keywords.items(), key=operator.itemgetter(1),reverse=True)
# print(sorted_keywords[:200])
# print(" Extracted Key terms of the corpus")
# for key,value in sorted_keywords[:200]:
#      print (key, value)

#Taxonomy induction
listOfTaxonomyWordPatterns=['is a type of','is a kind of','such as','is a member of',
                            'is a player of','belongs to', 'is a ','type of','consist']
tokenizedSentences=sent_tokenize(corpus)

potentialSentencesWithTaxonomy=[]
for sentence in tokenizedSentences:
    for pattern in listOfTaxonomyWordPatterns:
        if pattern in sentence:
            potentialSentencesWithTaxonomy.append(sentence.replace(pattern,"<<"+pattern+">>"))

#print(potentialSentencesWithTaxonomy)

for sentence in potentialSentencesWithTaxonomy:
    print (sentence)















