# Animalsay

A Python version of the famous [cowsay](https://en.wikipedia.org/wiki/Cowsay) program by Tony Monroe. It is based in this other [Python package](https://github.com/VaasuDevanS/cowsay-python) with way cuter animals. If you like it, feel free to contribute and add your own animals. 

# Install

Animalsay requires Python 3.6 or higher to run. 

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

```sh
$ say("bunny", "Such a cutie pie!")
  _________________
< Such a cutie pie! >
  =================
                      \
                       \
                          (\_____/)
                          ( ' x ' )
                          c (")(")

```

It accepts both a short sentence and a [long text](https://www.lipsum.com/). 

```sh
$ say("cat", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam lacinia tellus eros, sit amet rhoncus sapien volutpat at. In odio justo, placerat at posuere ut, elementum eu ligula. Cras facilisis gravida tincidunt.")
  _________________________________________________
 /                                                 \
| Lorem ipsum dolor sit amet, consectetur adipiscin |
| g elit. Aliquam lacinia tellus eros, sit amet rho |
| ncus sapien volutpat at. In odio justo, placerat  |
| at posuere ut, elementum eu ligula. Cras facilisi |
| s gravida tincidunt.                              |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                           /\___/\
                                                          ( =^.^= )
                                                           (")(")_/

```

# More Animals

To see the the list of available animals.

```sh
$ from animalsay.utils import animals
$ animals.keys()

dict_keys(['cow', 'bunny', 'cat'])

```