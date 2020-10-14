# 8-suit Card Deck

A Python script to generate a full deck of playing cards with 8 suits:

* spades, hearts, diamonds & clovers
* cups, acorns, shields & roses

<image src="https://github.com/gcerutti/card_suits/blob/master/suits_BR.png" width="400px">

## Author:
* Guillaume Cerutti (<guillaume.cerutti@gmail.com>)

## Credits

* [Based on an original idea from the Dragon Company](http://www.dragoncompany.org/crafting-additional-playing-card-suits/)

## Installation

### Pre-requisite : Install conda

* Open a terminal window and type `conda`. If no error message appear (but a long how-to message) then you have successfully installed `conda`.

* Otherwise, you may choose to install either [the miniconda tool](https://docs.conda.io/en/latest/miniconda.html) or [the anaconda distribution](https://docs.anaconda.com/anaconda/install/) suitable for your OS.

### Download the source repository

#### Using the `git` command line tool

* Open a terminal window and navigate to the directory of your choice using the `cd` command.

* Copy the source repository using `git` by typing:

```
git clone https://github.com/gcerutti/card_suits.git
```

### Create a new conda environment

* In the terminal window, go to the directory where you copied the source repository:

```
cd card_suits
```

* Create a new environment containing all the script dependencies using the provided YAML file:

```
conda env create -f environment.yml
```

## Usage

### Activate the conda environment

* Each time you open a nw terminal window to use the script, you will need to activate the environment you created to access the dependencies

```
conda activate card_suits
```

### Run the generation script

* Go the script directory within the directory where you have copied the source repository

```
cd path/to/card_suits/script
```

> **NOTE:** you need to replace `path/to` with the actual file path in your file system 

* Run the generation script:

```
python card_suits.py
```

> **NOTE:** the deck will be generated as separate `.png` files under the `cards` folder. 


