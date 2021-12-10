import nltk
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer


def clean_text(df, column):
    try:
        df['clean_text'] = df[column].str.replace('[^\w\s]','')
    except:
        pass
    return df

# clean_text(df, 'text')


def lowercase(df, column):
    try:
        df[column] = df[column].str.lower()
    except:
        pass
    return df

# lowercase(df, 'clean_text')


def remove_num(df, column):
    try:
        df[column] = df[column].str.replace('[\d+]', '')
    except:
        pass
    return df

# remove_num(df, 'clean_text')


def remove_stopwords(text):
    stop = set(stopwords.words('english'))
    word_tokens = word_tokenize(str(text))
    return ' '.join([i for i in word_tokens if i not in stop])

# df['clean_text'] = df['clean_text'].apply(remove_stopwords)


def word_lemmatizer(text):
    lemmatizer = WordNetLemmatizer()
    return ' '.join([lemmatizer.lemmatize(w) for w in text.split()])

# df['clean_text'] = df['clean_text'].apply(word_lemmatizer)
