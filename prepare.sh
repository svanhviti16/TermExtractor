#!/bin/bash

# A script that accepts a file as a command line argument, and 
# tokenizes it, PoS tags it and lemmatizes it using IceNLP.

basename=$(basename $1)
x=${basename%.txt}
filepath=${x##*/}

mkdir output/$filepath


# tokenizing the input
java -classpath ../IceNLP/dist/IceNLPCore.jar is.iclt.icenlp.runner.RunTokenizer -i $1 -o output/$filepath/prepared/tokenized.txt

# tagging using IceTagger
java -classpath ../IceNLP/dist/IceNLPCore.jar is.iclt.icenlp.runner.RunIceTagger -i output/$filepath/prepared/tokenized.txt -o output/$filepath/prepared/tagged.txt

# extracting first two columns (to eliminate UNKNOWN tag)
awk '{print $1 " " $2}' output/$filepath/prepared/tagged.txt > output/$filepath/prepared/tagged_clean.txt

# lemmatizing using Lemmald
java -classpath ../IceNLP/dist/IceNLPCore.jar is.iclt.icenlp.runner.RunLemmald -i output/$filepath/prepared/tokenized.txt -o output/$filepath/prepared/lemmatized.txt

# combining files to fit Gullstaðall format
awk '{print $1 " " $3 " " $2}' output/$filepath/prepared/lemmatized.txt > output/$filepath/prepared/lemmatized_clean.txt

