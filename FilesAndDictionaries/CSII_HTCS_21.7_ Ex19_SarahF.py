#HTCS 12.7 Exercise 19
#Sarah Friedman
#9/17/17

pirate = {}                         #Creates dictionary of english words in pirate

pirate['sir'] = ['matey']
pirate['hotel'] = ['fleabag inn']
pirate['student'] = ['swabbie']
pirate['boy'] = ['matey']
pirate['madam'] = ['proud beauty']
pirate['professor'] = ['foul blaggart']
pirate['restaurant'] = ['galley']
pirate['your'] = ['yer']
pirate['excuse'] = ['arr']
pirate['students'] = ['swabbies']
pirate['are'] = ['be']
pirate['lawyer'] = ['foul blaggart']
pirate['the'] = ['th']
pirate['restroom'] = ['head']
pirate['my'] = ['me']
pirate['hello'] = ['avast']
pirate['is'] = ['be']
pirate['man'] = ['matey']

sentenceInput = input("Please input a sentence in English to be translated into Pirate: ")  #asks user what sentence they want to translate

sentence = []
words = sentenceInput.split()

for word in words:          #it checks if any of the words in the sentence are in the pirate dictionary, and creates the translated sentece
    if word in pirate:
        sentence.append(pirate[word])       #if it is, the new translated pirate word is added to the 'sentence' list
    else:
        sentence.append(word)               #if not, the english word is added to the 'sentence' list

print(sentence)
