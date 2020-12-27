# Animalsay

A Python version of the famous [cowsay](https://en.wikipedia.org/wiki/Cowsay) program by Tony Monroe. It is based in this other [Python package](https://github.com/VaasuDevanS/cowsay-python) but with cuter animals. If you like it, feel free to contribute and add your own animals. 

# Install

Animal-say requires Python 3.6 or higher to run. 

```sh
$ pip install animalsay
```

# Usage 

```sh
$ from animalsay.utils import say
$ say("cow", "hello world!")

  ____________
< hello world! >
  ============
       \
        \
          ^__^
          (oo)\_______
          (__)\       )\/\
              ||----w |
              ||     ||

```

It accepts both a short sentence and a [long text](https://www.lipsum.com/). 

# More Animals

To see the the list of available animals.

```sh
$ import animalsay
$ animalsay.utils.animals.keys()

dict_keys(['cow', 'bunny', 'cat'])

```