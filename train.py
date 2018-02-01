dataset_file = open('trainingset.txt','r')


model = {}

import jieba

for line in dataset_file:
    line = jieba.cut_for_search(line)
    line = list(line)
    for i, word in enumerate(line):
        if i == len(line)-1:   
            model['END'] = model.get('END', []) + [word]
        else:    
            if i == 0:
                model['START'] = model.get('START', []) + [word]
            model[word] = model.get(word, []) + [line[i+1]]

print model

import pickle

with open('model.pickle','wb') as handle:
	pickle.dump(model,handle,protocol=pickle.HIGHEST_PROTOCOL)
