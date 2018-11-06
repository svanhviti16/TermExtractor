# TermExtractor

This is a term extraction tool for Icelandic written in Python 3. It was implemented using three different term extraction methods, namely the RAKE algorithm, PoS pattern matching (NP chunking) and tf-idf (term frequency * inverted document frequency)

## Dependencies
The program makes use of two natural language processing tools [NLTK](http://www.nltk.org/) and [IceNLP](https://github.com/hrafnl/icenlp). It also uses the [rake-nltk](https://github.com/csurfer/rake-nltk) implementation of the [RAKE algorithm](https://www.researchgate.net/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents).

To install the needed packages, run:

```sudo pip install -U nltk```

```sudo pip install -U numpy```

```pip install rake-nltk```

For IceNLP, download the .zip folder on [https://github.com/hrafnl/icenlp/releases](https://github.com/hrafnl/icenlp/releases). The program needs the IceNLP project folder to be located in the same directory as the TermExtractor project folder in order to prepare the data, otherwise, adjustments are needed in the shell script ```prepare.sh```.


## Running the program
To use, run main.sh in the console with a .txt containing some text to extract terms from using the following commands:

```$ chmod +x main.sh```

```$ ./main.sh <filename.txt>```

The script executes a series of scripts and produces four termlists in the folder output/<filename>/termlists, one for each approach used and a combined list from the other three.
