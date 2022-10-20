#Parsing text API practice
#test git push

#importing TextBlob
from textblob import TextBlob

#TestBlob practice
test = TextBlob("A buck, pursued by hunters, concealed himself among the branches of a vine.")

print(test.tags)

kept_words = []
for tuple in test.tags:
    if tuple[1] == 'NN':
        kept_words.append(tuple[0])

print(kept_words)
