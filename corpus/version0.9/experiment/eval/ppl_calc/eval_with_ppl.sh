#!/bin/bash

## Written by Ye Kyaw Thu, LU Lab., Myanmar
## You have to install KenLM in advance.
## For evaluation with PPL on GPT-2 Hatespeech Model generated sentences
## Last updated: 23 Oct 2023

# Check if the folder name argument is provided
if [[ -z "$1" ]]; then
    echo "Error: No folder name provided."
    echo "Usage: $0 <folder-name>"
    exit 1
fi

# Ensure the folder exists
if [[ ! -d "$1" ]]; then
    echo "Error: Folder '$1' does not exist."
    exit 1
fi

# Loop through all .syl files in the specified folder, in alphabetical order
for file in $(find "$1" -name '*.syl' | sort); do
    echo "Evaluation on: $file"
    command="/home/nang/kenlm/build/bin/query -v summary ./lm.5gram.arpa < $file"
    echo "Running: $command"
    eval $command
    echo "==========";
    echo "";
done

