# Artificial Neural Network

Currently contains implementations of algorithms based on single-layer perceptron (SLP).
Mainly inspired by the book "[The Nature of Code](http://natureofcode.com)" by Daniel Shiffman

### Prerequisites

```
cd ann
pigar
sudo pip3 install -r requirements.txt
```


see [pigar](https://github.com/damnever/pigar.git) (Generates reqs)


### Installing/Running

Just run scripts with

```
python3 simple_perceptron.py
python3 next_perceptron.py
```

### What is that ?

This is an implementation of a single-layer perceptron. This algorithm is based on one of the many principles in machine learning: the perceptron. To understand what's behind the code, you should check the book "The Nature of Code" that I mentionned earlier and from where that algorithm had been based on.

BUT with that said, the main purpose is the following:
Given a set of points distributed over a predefined area ( origin-centered unit square, points randomly initialized and weighted ), the perceptron trains itself with the points (input data) and then tries to guess what is the original distribution function ( red by default) by tweaking weights of each points in enrichment steps/iterations (please press any Key to enrich) and drawing the resulted guess curve.

A picture is worth a thousand words, just run the code and do your own modification.


### What's next ?

The main goal of this is to understand the very basics of neural network and to do a first implementation.
The next thing to do is to implement a multi-layer perceptron (MLP). Stay in touch with this Github repo
