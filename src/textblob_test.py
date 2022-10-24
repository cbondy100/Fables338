#Parsing text API practice
#test vs code git
#Might have to use a differnt NLP API

#importing TextBlob
from textblob import TextBlob

#TestBlob practice
test = TextBlob("A buck, pursued by hunters, concealed himself among the branches of a vine.")

print(test.tags)

kept_words = []
for tuple in test.tags:
    if 'NN' in tuple[1]:
        kept_words.append(tuple[0])

print(kept_words)
