# Markov_chains_gen_sentence
Use Marko chain to generate new sentence from training model

## Preparation

There are several libs you need to install first.

**jieba** -- For segementing the chinese sentence

```
pip install jeba

```

**pickle** -- save and open the training model

```
pip install pickle

```

And you should prepare training data (sentences), and save them into file **trainingset.txt**. After saving the raw sentences, you should clean up the data like removing symbols and space.

## How to Use

Once you clean up your training data, you can start to train your model

**Training the model first**

```
python train.py

```

## Performance

To be honest, this is just a very simple start. The generated sentence is very simple and naive. If you have any thoughts, plase let me know and let's improve it.


```
hangyan.leung@gmail.com

```








