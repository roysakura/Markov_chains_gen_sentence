import random 
import pickle

with open('model.pickle', 'rb') as handle:
    model = pickle.load(handle)

generated = []
while True:
    if not generated:
        words = model['START']
    elif generated[-1] in model['END']:
        break
    else:
        words = model[generated[-1]]
    generated.append(random.choice(words))

print ''.join(generated)