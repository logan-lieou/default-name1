import json

def read_ds():
    with open("../data/dataset.json", 'r') as f:
        datastore = json.load(f)
        f.close()

    sentences = []
    labels = []
    urls = []

    for item in datastore:
        sentences.append(item['headline'])
        labels.append(item['is_sarcastic'])
        urls.append(item['article_link'])

    return sentences, labels, urls
