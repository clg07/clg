from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.tokenizers import Tokenizer

text = """International Relations (IR) refers to the study of interactions between nations, states, and other actors on the global stage. 
It encompasses a broad range of topics, including diplomacy, foreign policy, conflict resolution, globalization, and international law. 
In this blog, we will delve into the meaning and definitions of IR, its history, features, importance, and India’s relations with major countries. """

parser = PlaintextParser(text,Tokenizer("english"))

summarizer = LsaSummarizer()
summary = summarizer(parser.document,2)

for sum in summary:
    print(" - ",sum)
