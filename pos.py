
"""
Note: this code is AI assisted. It creates a random sample from a text file, analyzes the part of speech of the text,
counts the frequency of words in the text and displays a word cloud of the text.
"""


import pandas as pd
import random
import spacy
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from spacy import displacy



with open('pubmed_2020_sample.txt', 'r') as file:
    sample2020 = file.readlines()

with open('pubmed_2024_sample.txt', 'r') as file:
    sample2024 = file.readlines()

sample2020_df = pd.DataFrame(sample2020, columns=['text'])
sample2024_df = pd.DataFrame(sample2024, columns=['text'])

terms_2020 = len(sample2020_df)
terms_2024 = len(sample2024_df)


def random_number(n): #generate random number to pick the sample
    random_int = random.randint(0, n - 1)  
    return random_int


def create_sample(fullSampleYear, oldSampleLength, newSampleLength, newFileName): #create samples and save them to a new temporary file
    sample_list = []
    for i in range(newSampleLength):
        sample_list.append(fullSampleYear.iloc[random_number(oldSampleLength)])
    sample_df = pd.DataFrame(sample_list, columns=['text']) 
    sample_df.to_csv(newFileName, index=False)
    print("Sample saved to ", newFileName)
    return sample_list


text_file = create_sample(sample2024_df, terms_2020, 1000, 'sample2020_1000.txt')


def analyze_pos_file(text_list): #analyze the part of speech of the text
    nlp = spacy.load('en_core_web_sm')
    pos_list = []
    
    for abstract in text_list:
        cleantext = remove_non_alphabetic(abstract)
        doc = nlp(cleantext)
       
        for token in doc:
            pos_list.append(token.pos_)
        
        for entity in doc.ents:
            print(entity.text, entity.label_)
        
        for token in doc:
            print(f"{token.text}\t{token.pos_}")

    return pos_list


def analyze_pos_string(text_string): #analyze the part of speech of the text
    nlp = spacy.load('en_core_web_sm')
    pos_list = []
    doc = nlp(text_string)
   

    for token in doc:
        pos_list.append(token.pos_)
        
    for entity in doc.ents:
        print(entity.text, entity.label_)
        
    for token in doc:
        print(f"{token.text}\t{token.pos_}")
    
      
    displacy.serve(doc, style="dep")  
    return pos_list

def remove_non_alphabetic(text): #make the text processable
    text = text.lower()
    return re.sub(r'[^a-zA-Z\s]', '', text)


def wordfrequency(text_list): #count the frequency of words in the text
 
    combined_word_freq = {}

    for abstract in text_list:
        cleantext = remove_non_alphabetic(abstract)
        splittext = cleantext.split()
   
        for word in splittext:
            if word in combined_word_freq:
                combined_word_freq[word] += 1
            else:
                combined_word_freq[word] = 1

    arrange = sorted(combined_word_freq.items(), key=lambda x: x[1], reverse=False)

    for word, freq in arrange:
        print(f"{word}: {freq}")


#text_list = [item['text'] for item in text_file]
text_list = text_file[1]


# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
# wordcloud = WordCloud().generate(text_list[7])

# wordfrequency(text_list)
#analyze_pos_file(text_list)
analyze_pos_string("Asking for a sentence makes sentences hard to think of.")
