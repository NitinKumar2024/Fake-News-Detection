# Fake News Detection Model with Flask Web App

![Fake News Detection]([https://ieee-dataport.org/sites/default/files/WhatsApp%20Image%202020-08-17%20at%2010.32.28%20PM_1.jpeg])

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Datasets](#datasets)
- [Model](#model)
- [Web Application](#web-application)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This repository contains the code for a Fake News Detection Model using machine learning, integrated with a Flask web application. The goal of this project is to detect fake news articles using a trained machine learning model and provide a user-friendly web interface for users to check the authenticity of news articles.

## Features

- **Data Preprocessing**: Cleans and prepares the dataset for training and testing.
- **Feature Extraction**: Uses techniques like TF-IDF to extract features from the text.
- **Model Training**: Implements Logistic Regression for detecting fake news.
- **Model Evaluation**: Evaluates the performance of the model using metrics like accuracy, precision, recall, and F1 score.
- **Web Application**: Flask web app for users to input news URLs or text and get predictions.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/nitinkumar2024/fake-news-detection.git
    cd fake-news-detection
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure you have the model and vectorizer files (`fake_news_model.pkl` and `tfidf_vectorizer.pkl`) in the project directory. If not, train the model and save these files.

## Usage

### Running the Web Application

1. Start the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000` to access the web application.

### Using the Web Application

- **Check News via URL**:
    1. Enter the URL of the news article in the provided form.
    2. Click "Predict" to get the prediction.

- **Check News via Text**:
    1. Enter the title and content of the news article in the provided form.
    2. Click "Predict" to get the prediction.

## Datasets

The datasets used in this project should contain labeled news articles with columns like `text` and `label`, where `label` indicates whether the news is real or fake. Example sources include:

- [Kaggle Fake News Dataset](https://www.kaggle.com/c/fake-news/data)
- [LIAR: A Benchmark Dataset for Fake News Detection](https://www.cs.ucsb.edu/~william/lie_data.html)

## Model

The project utilizes Logistic Regression to detect fake news. The main steps involved are:

1. **Data Preprocessing**: Cleaning and normalizing the text data.
2. **Feature Extraction**: Using TF-IDF vectorization to convert text to numerical features.
3. **Model Training**: Training the model using Logistic Regression.
4. **Model Evaluation**: Evaluating the model performance on the test set.

## Web Application

The web application is built using Flask and provides a user-friendly interface for detecting fake news. Key functionalities include:

- **Scraping News Content**: Extracting the main heading and content of news articles from URLs.
- **Prediction**: Using the trained machine learning model to predict if the news is real or fake.
