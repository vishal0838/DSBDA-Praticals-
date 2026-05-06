# Install (run once if needed)
# pip install nltk

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag

# Download required datasets (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Sample document
text = "Data science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge from data."

# 1. Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# 2. POS Tagging
pos_tags = pos_tag(tokens)
print("\nPOS Tags:", pos_tags)

# 3. Stopwords Removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("\nAfter Stopword Removal:", filtered_tokens)

# 4. Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_tokens]
print("\nStemmed Words:", stemmed_words)

# 5. Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print("\nLemmatized Words:", lemmatized_words)