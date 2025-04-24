#!/bin/bash

## Written by Ye Kyaw Thu, LU Lab., Myanmar
## Experiment with short hate speech dataset
## Last updated: 7 April 2024

set -x;

## Evaluation with F1, P and R
time python ./hs-xgboost.py --train_file ./short-data/strain.txt \
--test_file ./short-data/stest.txt --feature tfidf --num_round 30 \
--eval f1 | tee tfidf-f1-short.log

time python ./hs-xgboost.py --train_file ./short-data/strain.txt \
--test_file ./short-data/stest.txt --feature word2vec --num_round 30 \
--eval f1 | tee w2v-f1-short.log

time python ./hs-xgboost.py --train_file ./short-data/strain.txt \
--test_file ./short-data/stest.txt --feature fasttext --num_round 30 \
--eval f1 | tee fasttext-f1-short.log

## Evaluation with Logloss
time python ./hs-xgboost.py --train_file ./short-data/strain.txt \
--test_file ./short-data/stest.txt --feature tfidf --num_round 30 \
--eval logloss | tee tfidf-logloss-short.log

time python ./hs-xgboost.py --train_file ./short-data/strain.txt \
--test_file ./short-data/stest.txt --feature word2vec --num_round 30 \
--eval logloss | tee w2v-logloss-short.log

time python ./hs-xgboost.py --train_file ./short-data/strain.txt \
--test_file ./short-data/stest.txt --feature fasttext --num_round 30 \
--eval logloss | tee fasttext-logloss-short.log

## Evaluation with Error
time python ./hs-xgboost.py --train_file ./short-data/strain.txt \
--test_file ./short-data/stest.txt --feature tfidf --num_round 30 \
--eval error | tee tfidf-error-short.log

time python ./hs-xgboost.py --train_file ./short-data/strain.txt \
--test_file ./short-data/stest.txt --feature word2vec --num_round 30 \
--eval error | tee w2v-error-short.log

time python ./hs-xgboost.py --train_file ./short-data/strain.txt \
--test_file ./short-data/stest.txt --feature fasttext --num_round 30 \
--eval error | tee fasttext-error-short.log

set +x;
