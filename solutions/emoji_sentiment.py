#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module converts a sentence into emojis based on the sentiment of the words.

Module Contents:
    - Positive words are represented by the 🌞 emoji.
    - Negative words are represented by the 🌧️ emoji.

created on 2025-12-29
@author: Alemayehu Desta
"""

import string


def emoji_sentiment(sentence: str) -> str:
    """
    Converts a sentence into emojis based on the sentiment of the words.

    Arguments:
        sentence (str): A sentence that will be analyzed for sentiment.

    Returns:
        str: A string where each word is replaced with an emoji based on its sentiment.

    Raises:
        ValueError: If the input is not a string or if the string is empty.

    Examples:
        >>> emoji_sentiment("I am happy and sunny!")
        'I am 🌞 and 🌞!'

        >>> emoji_sentiment("This is bad and rainy.")
        'This is 🌧️ and 🌧️.'

        >>> emoji_sentiment("I am Happy and SUNNY")
        'I am 🌞 and 🌞'
        # Case-insensitive matching of words.
    """

    if not isinstance(sentence, str):
        raise ValueError("Input must be a string.")

    if not sentence.strip():
        raise ValueError("Input string cannot be empty.")

    positive_words = {
        "happy",
        "joy",
        "love",
        "sunny",
        "great",
        "good",
        "excited",
        "amazing",
        "positive",
    }
    negative_words = {
        "sad",
        "angry",
        "bad",
        "worried",
        "unhappy",
        "hate",
        "rainy",
        "poor",
    }

    words = sentence.split()

    emoji_sentence = []
    for word in words:
        cleaned_word = word.lower().strip(string.punctuation)
        if cleaned_word in positive_words:
            emoji_sentence.append("🌞")
        elif cleaned_word in negative_words:
            emoji_sentence.append("🌧️")
        else:
            emoji_sentence.append(word)

    return " ".join(emoji_sentence)
