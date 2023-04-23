![Demo](demo_video.gif)

## Introduction

This dashboard is a web app designed with Streamlit. This web-interface is built for your personal virtual assistantance for Stock Market Investments. From the visualization of recent stock price variations for any of the current Top 100 NASDAQ companies, to recent articles about these companies, you can explore sources of information to make accurate decisions for your next trades.

## Installation

Firstly, ensure that you have pip install. In which case follow these steps using the command line:

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

Then install the required libraries listed in the requirements.txt
```
pip install -r requirements.txt
```

## Requirements

Create an account on [newsapi](https://newsapi.org/) to get an API key. Then add it to the file *api_key.json*. I have used my own API key as of now for demo purposes so you can run it without needing an API key.

## Usage Example
```
streamlit run app.py
```
