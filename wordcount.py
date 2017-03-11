from collections import Counter
import nltk
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))



# read sentence
lines = []
for line in open('building_global_community.txt'):
    # delete the blank and line feed at the begining and end
    line = line.strip()
    # add processed line text into list 'lines'
    lines.append(line)
	
# do Counter, 
# wordCounter : all words
# wordCounter_Noun : noun words
# wordCounter_Adj : Adj words
# wordCounter_verb : Verb words
# wordCounter_Other : other POS words
wordCounter = Counter()
wordCounter_verb =Counter()
wordCounter_Adj = Counter()
wordCounter_Noun = Counter()
wordCounter_Other = Counter()
wordCounter_adv = Counter()
word_punc_tokenizer = nltk.WordPunctTokenizer()
for sen in lines:
    # split sentence into words
    tokens = word_punc_tokenizer.tokenize(sen)
    #tokens = [word for word in nltk.word_tokenize(sen)]
    #tokens= filter(lambda word: word not in '[.,\/#!$%\^&\*;:{}-=\_`~()]', tokens)

    tmp_list = list()
    for token in tokens:
        if (token.isdigit()==False) and (token.isalpha()==True) and (token.lower() not in stopwords) :
            tmp_list.append(token.lower())
    for element in tmp_list:
        get_pos = nltk.pos_tag(element.split())
        word,pos = get_pos[0]
        if pos.startswith('NN'):
            wordCounter_Noun.update(word.split())
        elif pos.startswith('JJ'):
            wordCounter_Adj.update(word.split())
        elif pos.startswith('VB'):
            wordCounter_verb.update(word.split())
        elif pos.startswith('RB'):
            wordCounter_adv.update(word.split())
        else:
            wordCounter_Other.update(word.split())
    wordCounter.update(tmp_list)
	

# show the occurance of all words
print '## All wordcount TOP-20: '
#print wordCounter.most_common(20)

for word, count in wordCounter.most_common(20):
    print('{0}: {1}'.format(word, count))



# show the occurance of Noun words
print '## Noun words TOP-10: '
#print wordCounter_Noun.most_common(10)
for word, count in wordCounter_Noun.most_common(10):
    print('{0}: {1}'.format(word, count))


# show the occurance of Adj words
print '## Adj words TOP-10: '
#print wordCounter_Adj.most_common(10)
for word, count in wordCounter_Adj.most_common(10):
    print('{0}: {1}'.format(word, count))


# show the occurance of Adv words
print '## Adv Words TOP-10: '
#print wordCounter_adv.most_common(10)
for word, count in wordCounter_adv.most_common(10):
    print('{0}: {1}'.format(word, count))


# show the occurance of Other POS words
print '## Other POS words TOP-10: '
#print wordCounter_Other.most_common(10)
for word, count in wordCounter_Other.most_common(10):
    print('{0}: {1}'.format(word, count))
