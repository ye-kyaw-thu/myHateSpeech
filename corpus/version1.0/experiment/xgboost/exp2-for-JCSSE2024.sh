#!/bin/bash

## Written by Ye Kyaw Thu, LU Lab., Myanmar
## Experiment No.2 with long/short hate speech dataset
## for JCSSE 2024 Baseline
## Last updated: 7 April 2024

set -x;

## Evaluation with F1, P and R, Default Parameters for LONG HS
time python ./hs-xgboost.py --train_file ./long-data/ltrain.txt \
--test_file ./long-data/ltest.txt --feature tfidf \
--eval f1 --num_round 10 | tee -a exp2.log

time python ./hs-xgboost.py --train_file ./long-data/ltrain.txt \
--test_file ./long-data/ltest.txt --feature word2vec \
--eval f1 --num_round 10 | tee -a exp2.log

time python ./hs-xgboost.py --train_file ./long-data/ltrain.txt \
--test_file ./long-data/ltest.txt --feature fasttext  \
--eval f1 --num_round 10 | tee -a exp2.log

## Evaluation with F1, P and R, Default Parameters for SHORT HS
time python ./hs-xgboost.py --train_file ./short-data/strain.txt \
--test_file ./short-data/stest.txt --feature tfidf \
--eval f1 --num_round 10 | tee -a exp2.log

time python ./hs-xgboost.py --train_file ./short-data/strain.txt \
--test_file ./short-data/stest.txt --feature word2vec \
--eval f1 --num_round 10 | tee -a exp2.log

time python ./hs-xgboost.py --train_file ./short-data/strain.txt \
--test_file ./short-data/stest.txt --feature fasttext \
--eval f1 --num_round 10 | tee -a exp2.log

set +x;
