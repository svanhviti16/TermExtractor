#!/bin/bash

# A script that accepts a file as a command line argument, and 
# tokenizes it, PoS tags it and lemmatizes it using IceNLP.

# tokenizing the input
java -classpath ../IceNLP/dist/IceNLPCore.jar is.iclt.icenlp.runner.RunTokenizer -i $1 -o output/tokenized.txt

# tagging using IceTagger
java -classpath ../IceNLP/dist/IceNLPCore.jar is.iclt.icenlp.runner.RunIceTagger -i output/tokenized.txt -o output/tagged.txt

# extracting first two columns (to avoid UNKNOWN tag)
awk '{print $1 " " $2}' output/tagged.txt > output/tagged_clean.txt

# lemmatizing using Lemmald
java -classpath ../IceNLP/dist/IceNLPCore.jar is.iclt.icenlp.runner.RunLemmald -i output/tokenized.txt -o output/lemmatized.txt

# combining files to fit Gullstaðall format
awk '{print $1 " " $3 " " $2}' output/lemmatized.txt > output/lemmatized_clean.txt

# PoS tagging the original file sentence by sentence using IceTagger
# 2 2 stands for input with one sentence per line and output with one sentence per line
# TODO: try with raw text
# java -classpath ../IceNLP/dist/IceNLPCore.jar is.iclt.icenlp.runner.RunIceTagger -i output/tokenized.txt -o output/tagged_for_parsing.txt LINE_FORMAT=1 OUTPUT_FORMAT=2 FULL_OUTPUT=no
# TODO: remove empty lines
# java -classpath ../IceNLP/dist/IceNLPCore.jar is.iclt.icenlp.runner.RunIceParser -i  output/tagged_for_parsing.txt -o output/parsed.txt -f -l
