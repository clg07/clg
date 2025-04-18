from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
# nltk.download('punkt_tab')

text = """
Infromation Reteival is a field concerned with searching for relevant documents
within a large dataset. Text summerization is the process of reducing a
documents's
length while maintaining its meaning. Extractive methods identify 
and extract
key snetences, while abstractive methods generate summeries in their
own words.

"""

parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LsaSummarizer()
print(parser.document)
summary = summarizer(parser.document, 2)

for sentence in summary:
    print(sentence)