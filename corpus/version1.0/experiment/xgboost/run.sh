#!/bin/bash

## Written by Ye Kyaw Thu, LU Lab., Myanmar
## Experiment with long hate speech dataset
## Last updated: 7 April 2024

set -x;

## Evaluation with F1, P and R
time python ./hs-xgboost.py --train_file ./long-data/ltrain.txt \
--test_file ./long-data/ltest.txt --feature tfidf --num_round 30 \
--eval f1 | tee tfidf-f1.log

time python ./hs-xgboost.py --train_file ./long-data/ltrain.txt \
--test_file ./long-data/ltest.txt --feature word2vec --num_round 30 \
--eval f1 | tee w2v-f1.log

time python ./hs-xgboost.py --train_file ./long-data/ltrain.txt \
--test_file ./long-data/ltest.txt --feature fasttext --num_round 30 \
--eval f1 | tee fasttext-f1.log

## Evaluation with Logloss
time python ./hs-xgboost.py --train_file ./long-data/ltrain.txt \
--test_file ./long-data/ltest.txt --feature tfidf --num_round 30 \
--eval logloss | tee tfidf-logloss.log

time python ./hs-xgboost.py --train_file ./long-data/ltrain.txt \
--test_file ./long-data/ltest.txt --feature word2vec --num_round 30 \
--eval logloss | tee w2v-logloss.log

time python ./hs-xgboost.py --train_file ./long-data/ltrain.txt \
--test_file ./long-data/ltest.txt --feature fasttext --num_round 30 \
--eval logloss | tee fasttext-logloss.log

## Evaluation with Error
time python ./hs-xgboost.py --train_file ./long-data/ltrain.txt \
--test_file ./long-data/ltest.txt --feature tfidf --num_round 30 \
--eval error | tee tfidf-error.log

time python ./hs-xgboost.py --train_file ./long-data/ltrain.txt \
--test_file ./long-data/ltest.txt --feature word2vec --num_round 30 \
--eval error | tee w2v-error.log

time python ./hs-xgboost.py --train_file ./long-data/ltrain.txt \
--test_file ./long-data/ltest.txt --feature fasttext --num_round 30 \
--eval error | tee fasttext-error.log

set +x;
