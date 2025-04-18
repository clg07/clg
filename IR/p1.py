import nltk
from nltk.corpus import stopwords

# Define the documents
document1 = "The quick brown fox jumped over the lazy dog"
document2 = "The lazy dog slept in the sun"

# Download stopwords and get the list for English
nltk.download('stopwords')
stopWords = stopwords.words('english')

# Tokenize and preprocess the documents
tokens1 = document1.lower().split()
tokens2 = document2.lower().split()

# Combine the tokens into a list of unique terms
terms = list(set(tokens1 + tokens2))

# Initialize dictionaries for the inverted index and occurrences
inverted_index = {}
occ_num_doc1 = {}
occ_num_doc2 = {}

# Build the inverted index
for term in terms:
    if term in stopWords:
        continue
    documents = []
    if term in tokens1:
        documents.append("Document 1")
        occ_num_doc1[term] = tokens1.count(term)
    if term in tokens2:
        inverted_index = build_index(documents)

# Example queries
query1 = ["apple", "banana"]  # AND query
query2 = ["apple", "orange"]  # OR query
query3 = "orange"             # NOT query

# Perform queries
result1 = boolean_and(query1, inverted_index)
result2 = boolean_or(query2, inverted_index)
result3 = boolean_not(query3, inverted_index, len(documents))

# Output results
print("Documents containing 'apple' AND 'banana':", result1)
print("Documents containing 'apple' OR 'orange':", result2)
print("Documents NOT containing 'orange':", result3)
print("Performed by 740_Pallavi & 743_Deepak")
