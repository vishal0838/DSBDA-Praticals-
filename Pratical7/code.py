# Install required libraries (Run once in terminal)
# pip install nltk scikit-learn

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Sample text
text = """
Natural Language Processing is a branch of Artificial Intelligence.
It helps computers understand human language.
"""

# 1. Tokenization
tokens = word_tokenize(text)

print("Tokens:")
print(tokens)

# 2. POS Tagging
pos = pos_tag(tokens)

print("\nPOS Tagging:")
print(pos)

# 3. Stop Words Removal
stop_words = set(stopwords.words('english'))

filtered_words = [word for word in tokens if word.lower() not in stop_words]

print("\nAfter Stop Words Removal:")
print(filtered_words)

# 4. Stemming
ps = PorterStemmer()

stemmed_words = [ps.stem(word) for word in filtered_words]

print("\nStemmed Words:")
print(stemmed_words)

# 5. Lemmatization
lemmatizer = WordNetLemmatizer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

print("\nLemmatized Words:")
print(lemmatized_words)

# 6. TF-IDF Representation
documents = [
    "Natural Language Processing helps computers understand language",
    "Machine Learning is part of Artificial Intelligence"
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

print("\nTF-IDF Feature Names:")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())