# chancetoroll
I play tabletop RPGs (D&D, Dungeon World, ICRPG, and the like),
like to experiment with different rule systems, and I wanted a simple util
for determining the probability of rolling equal to or greater than a given
number on a variable number of polyhedral dice.

There are plenty of web based dice probability calculators for sums of dice,
but when I looked I couldn't find any for each dice taken individually, so I
built this simple util instead.

## Install
In it's current form there are no external package dependencies,
so installation is pretty easy.

```
$ python setup.py sdist
...
$ pip install dist/chancetoroll-<version-number>.tar.gz
...
```

## Usage

It's easy to use too. Just run chancetoroll as a module with the required params.

```
$ python -m chancetoroll 6 3 6
Rolling 3d6, probability of beating a 6 = 0.5

$ python -m chancetoroll 20 2 10
Rolling 2d20, probability of beating a 10 = 0.810526315789
```

### Positional Arguments
  * typedice    The type of dice to roll (4 = d4, 6 = d6, 20 = d20, etc.)
  * numdice     The number of dice to roll (1 = roll 1 dice, 2 = roll 2 dice, etc.)
  * targetside  The value a single dice must beat for success (e.g. 5 = rolls of 5 or higher are a success)
