from transformers import pipeline
import pandas as pd

sa = pipeline("sentiment-analysis")

sentence = "fuck you idiota"
result = sa(sentence)
print(result[0]['label'])
