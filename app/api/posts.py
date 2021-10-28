# -*- coding: utf-8 -*-
from flask import jsonify, request, current_app
from . import api

import codecs
from textRank.textrank4zh.TextRank4Keyword import TextRank4Keyword
from textRank.textrank4zh.TextRank4Sentence import TextRank4Sentence


@api.route("/posts/classifier", methods=['POST'])
def classifier():
    title = request.get_json().get('title')
    abstract = request.get_json().get('abstract')
    keyword = request.get_json().get('keyword')
    text = request.get_json().get('text')
    tr4w = TextRank4Keyword()

    print("title's keyword")
    tr4w.analyze(text=title, lower=True, window=2)
    for item in tr4w.get_keywords(20, word_min_len=1):
        print(item.word, item.weight)

    print("abstract's keyword")
    tr4w.analyze(text=abstract, lower=True, window=2)
    for item in tr4w.get_keywords(20, word_min_len=1):
        print(item.word, item.weight)

    print("keyword's keyword")
    tr4w.analyze(text=keyword, lower=True, window=2)
    for item in tr4w.get_keywords(20, word_min_len=1):
        print(item.word, item.weight)

    print("text's keyword")
    tr4w.analyze(text=text, lower=True, window=2)
    for item in tr4w.get_keywords(20, word_min_len=1):
        print(item.word, item.weight)

    return jsonify({'category': tr4w.get_keywords(20, word_min_len=1)})
