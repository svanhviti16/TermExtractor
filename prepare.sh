#!/bin/bash

# A script that accepts a file as a command line argument, and 
# tokenizes it, PoS tags it and lemmatizes it using IceNLP.

# tokenizing the input
java -classpath IceNLP/dist/IceNLPCore.jar is.iclt.icenlp.runner.RunTokenizer -i $1 -o output/tokenized.txt

# tagging using IceTagger
java -classpath IceNLP/dist/IceNLPCore.jar is.iclt.icenlp.runner.RunIceTagger -i output/tokenized.txt -o output/tagged.txt

# extracting first two columns (to avoid UNKNOWN tag)
awk '{print $1 " " $2}' output/tagged.txt > output/tagged_clean.txt

# lemmatizing using Lemmald
java -classpath IceNLP/dist/IceNLPCore.jar is.iclt.icenlp.runner.RunLemmald -i output/tagged_clean.txt -o output/lemmatized.txt

# reordering to fit Gullstaðall format
awk '{print $1 " " $3 " " $2}' output/lemmatized.txt > output/lemmatized_clean.txt

# TODO: þarf eina setningu í línu og láta parser virka
# parsing the original file using IceParser
# java -classpath IceNLP/dist/IceNLPCore.jar is.iclt.icenlp.runner.RunIceParser -i $1 -o output/parsed.txt -f -l
