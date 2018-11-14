# TermExtractor

This is a term extraction tool for Icelandic written in Python. It was implemented using three different term extraction methods, namely the RAKE algorithm, PoS pattern matching (NP chunking) and tf-idf (term frequency * inverted document frequency). It can be used to produce a candidate list of terms from a given text document.

## Dependencies
The program runs in Python 3 and makes use of two natural language processing libraries, [NLTK](http://www.nltk.org/) and [IceNLP](https://github.com/hrafnl/icenlp). It also uses the [rake-nltk](https://github.com/csurfer/rake-nltk) implementation of the [RAKE algorithm](https://www.researchgate.net/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents). It is recommended to run the project in a virtual environment with Python 3.

To install the needed packages, run:

```pip install -r requirements.txt```

For IceNLP, download the .zip folder on [https://github.com/hrafnl/icenlp/releases](https://github.com/hrafnl/icenlp/releases). You also need to download a [JDK](https://www.oracle.com/technetwork/java/javase/downloads/index.html) to be able to run Java. The program needs the IceNLP project folder to be located in the same directory as the TermExtractor project folder in order to prepare the data, otherwise, adjustments are needed in the shell script ```prepare.sh```.


## Running the program
To use, run ```main.sh``` in the console with a ```.txt``` file containing some text to extract terms from, using the following command:

```$ ./main.sh <filename.txt>```

The script executes a series of scripts and produces four termlists in the folder output/\<filename\>/termlists, one for each approach used and a combined list from the other three.
  
Each Python script can also be run independently using Python 3.

