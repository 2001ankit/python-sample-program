#Import the libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os

#Get the article
article = Article('https://www.coursera.org/articles/what-is-python-used-for-a-beginners-guide-to-using-python')

nltk.download('punkt')
article.nlp()

#Get the articles text
mytext = article.text
language = 'en' #English

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("read_article.mp3")

os.system("start read_article.mp3")