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
    print("*" * 10)
    for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num=2):
        print(phrase)

    print("abstract's keyword")
    tr4w.analyze(text=abstract, lower=True, window=2)
    for item in tr4w.get_keywords(20, word_min_len=1):
        print(item.word, item.weight)
    print("*" * 10)
    for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num=2):
        print(phrase)

    print("keyword's keyword")
    tr4w.analyze(text=keyword, lower=True, window=2)
    for item in tr4w.get_keywords(20, word_min_len=1):
        print(item.word, item.weight)
    print("*" * 10)
    for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num=2):
        print(phrase)

    print("text's keyword")
    tr4w.analyze(text=text, lower=True, window=2)
    text_keyword = tr4w.get_keywords(10, word_min_len=1)
    for item in text_keyword:
        print(item.word, item.weight)
    print("*"*10)
    text_keyPhrases = tr4w.get_keyphrases(keywords_num=10, min_occur_num=2)
    for phrase in text_keyPhrases:
        print(phrase)

    result = "演示结果"
    msg = "分类成功"
    return jsonify({
        'code': 1,
        'message': msg,
        'keywords': text_keyword,
        'keyPhrases': text_keyPhrases,
        'category': result
    })
