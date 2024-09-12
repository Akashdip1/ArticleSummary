import tkinter as tk 
import nltk
from textblob import TextBlob
from newspaper import Article 

nltk.download('punkt')
nltk.download('punkt_tab')

url = 'https://odishatv.in/news/odisha/daughters-of-odisha-govt-employees-to-get-compassionate-appointment-243989'

article =  Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication date: {article.publish_date}')
print(f'Summary : {article.summary}')

