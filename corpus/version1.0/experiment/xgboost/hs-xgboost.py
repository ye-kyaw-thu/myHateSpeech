"""
for hate speech classification with XGBoost
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 7 April 2024 
Usage:
(xgboost) yekyaw.thu@gpu:~/exp/xgboost$ python ./hs-xgboost.py --help
"""

import argparse
import numpy as np
import xgboost as xgb
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec, FastText
from sklearn.metrics import f1_score, precision_score, recall_score, log_loss, accuracy_score

# Function to load Burmese text data
def load_data(file_path):
    texts = []
    labels = []
    label_map = {}  # Dictionary to map text labels to integers
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_no, line in enumerate(file, start=1):
            parts = line.strip().split(' ', 1)
            if len(parts) < 2:
                print(f"Error: Line {line_no} in the file '{file_path}' does not contain both label and text. Skipping...")
                continue
            label = parts[0]
            text = parts[1]
            texts.append(text)
            # Extract label from the first column
            label = label.split('__label__')[-1].strip()  # Extracting label after '__label__'
            if label == "":
                label = "BLANK"  # Assigning a special label for blanks
            if label not in label_map:
                label_map[label] = len(label_map)  # Assign a unique integer to each label
            labels.append(label_map[label])  # Append the integer label
    return texts, labels, label_map

# Function to load stop words from file
def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        stopwords = file.read().splitlines()
    return stopwords

# Function to calculate text features
def calculate_features(train_texts, test_texts, feature_type, stopwords=None):
    if feature_type == 'tfidf':
        vectorizer = TfidfVectorizer(stop_words=stopwords)
        train_features = vectorizer.fit_transform(train_texts)
        test_features = vectorizer.transform(test_texts)
    elif feature_type == 'word2vec':
        word2vec_model = Word2Vec(sentences=[text.split() for text in train_texts], vector_size=100, window=5, min_count=1, workers=4)
        train_features = np.array([np.mean([word2vec_model.wv[word] for word in text.split() if word in word2vec_model.wv] or [np.zeros(100)], axis=0) for text in train_texts])
        test_features = np.array([np.mean([word2vec_model.wv[word] for word in text.split() if word in word2vec_model.wv] or [np.zeros(100)], axis=0) for text in test_texts])
    elif feature_type == 'fasttext':
        fasttext_model = FastText(sentences=[text.split() for text in train_texts], vector_size=100, window=5, min_count=1, workers=4)
        train_features = np.array([np.mean([fasttext_model.wv[word] for word in text.split() if word in fasttext_model.wv] or [np.zeros(100)], axis=0) for text in train_texts])
        test_features = np.array([np.mean([fasttext_model.wv[word] for word in text.split() if word in fasttext_model.wv] or [np.zeros(100)], axis=0) for text in test_texts])
    else:
        raise ValueError("Invalid feature type. Choose from 'tfidf', 'word2vec', or 'fasttext'.")
    return train_features, test_features

def main(args):
    # Load data
    train_texts, train_labels, label_map = load_data(args.train_file)
    test_texts, test_labels, _ = load_data(args.test_file)

    # Load stop words if provided
    stopwords = None
    if args.stopword_file:
        stopwords = load_stopwords(args.stopword_file)

    # Calculate features
    train_features, test_features = calculate_features(train_texts, test_texts, args.feature, stopwords)

    # Train XGBoost model
    xg_train = xgb.DMatrix(train_features, label=train_labels)
    xg_test = xgb.DMatrix(test_features, label=test_labels)

    # Setup parameters for XGBoost
    param = {'objective': 'multi:softmax', 'eta': args.learning_rate, 'max_depth': args.max_depth, 'nthread': 4, 'num_class': len(label_map)}
    # Define the watchlist with the train and test sets
    watchlist = [(xg_train, 'train'), (xg_test, 'test')]
    num_round = args.num_round

    # Train XGBoost model
    bst = xgb.train(param, xg_train, num_round, watchlist)

    # Get predictions
    pred_prob = bst.predict(xg_test, output_margin=True)
    pred_prob = np.apply_along_axis(lambda x: np.exp(x) / np.sum(np.exp(x)), 1, pred_prob)

    # Get predicted numeric labels
    pred_numeric_labels = pred_prob.argmax(axis=1)

    # Evaluate model based on specified metric
    if args.eval == 'f1':
        # Convert numeric labels to text labels for F1 calculation
        pred_text_labels = [list(label_map.keys())[label] for label in pred_numeric_labels]
        f1 = f1_score([list(label_map.keys())[label] for label in test_labels], pred_text_labels, average='weighted')
        precision = precision_score([list(label_map.keys())[label] for label in test_labels], pred_text_labels, average='weighted', zero_division=1)
        recall = recall_score([list(label_map.keys())[label] for label in test_labels], pred_text_labels, average='weighted')
        print(f"F1 Score: {f1}")
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
    elif args.eval == 'logloss':
        metric_score = log_loss(test_labels, pred_prob)
        print(f"Log Loss: {metric_score}")
    elif args.eval == 'error':
        # Calculate error rate directly from numeric labels
        metric_score = 1.0 - accuracy_score(test_labels, pred_numeric_labels)
        print(f"Error Rate: {metric_score}")
    else:
        raise ValueError("Invalid evaluation metric. Choose from 'f1', 'logloss', or 'error'.")

    # Print numeric labels and original label text for better understanding
    print("\nNumeric Label - Original Label")
    for numeric_label, text_label in label_map.items():
        print(f"{numeric_label} - {text_label}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Hate Speech Classification with XGBoost')
    parser.add_argument('--train_file', type=str, help='Path to training data file', required=True)
    parser.add_argument('--test_file', type=str, help='Path to testing data file', required=True)
    parser.add_argument('--feature', type=str, help='Text feature type: tfidf, word2vec, or fasttext', choices=['tfidf', 'word2vec', 'fasttext'], required=True)
    parser.add_argument('--stopword_file', type=str, help='Path to stopword file (optional)', default=None)
    parser.add_argument('--learning_rate', type=float, help='Learning rate (eta), default=0.1', default=0.1)
    parser.add_argument('--max_depth', type=int, help='Maximum depth of a tree, default=6', default=6)
    parser.add_argument('--num_round', type=int, help='Number of boosting rounds, default=5', default=5)
    parser.add_argument('--eval', type=str, help='Evaluation metric: f1, logloss, or error, default=f1', choices=['f1', 'logloss', 'error'], default='f1')
    args = parser.parse_args()
    main(args)

