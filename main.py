import json
import os

with open('data/train.json') as f:
    data = json.load(f)
    ingredients = list(map(lambda x: ' '.join(x['ingredients']), data))

    with open('tmp.txt', 'w') as tmp:
        tmp.write('\n'.join(ingredients))
        os.system('./fasttext skipgram -input tmp.txt -output wordvec/skipgram -dim 300 -epoch 10000')

    os.remove('tmp.txt')
