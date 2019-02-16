import sys

import json
import random


def load_index_data(arguments):
    try:
        index_data_path = arguments[1]
    except IndexError:
        raise IndexError('You must specify index data path.')
    with open(index_data_path) as index_data:
        return json.load(index_data)


def get_polish_phrases_string(polish_phrases):
    polish_phrases_string = ''
    counter = 1
    for phrase in polish_phrases:
        polish_phrases_string = (
            polish_phrases_string + f'{counter}. {phrase}\n'
        )
        counter = counter + 1
    return polish_phrases_string


def ask_questions(index_data, polish_phrases_string, phrase=None):
    english_phrases = list(index_data.values())
    polish_phrases = list(index_data.keys())
    random_phrase = phrase or random.choice(list(english_phrases))

    user_input = input(
        f'\nWhat does "{random_phrase}" mean in Polish?\n'
        f'Possible choices:\n{polish_phrases_string}'
    )

    try:
        selected_phrase = polish_phrases[int(user_input)-1]
    except (IndexError, KeyError, ValueError):
        print(f'\n{user_input} is not proper phrase number from the list. '
              f'Please select the right one.\n')
        ask_questions(
            index_data, polish_phrases_string, random_phrase
        )

    if index_data.get(selected_phrase) == random_phrase:
        print('\nRIGHT ANSWER.\n')
    else:
        print('\nBAD ANSWER.\n')
    another = input('Do you want to draw another card? '
        '(press enter to continue or "q" to exit the application) ')
    if another == '':
        ask_questions(index_data, polish_phrases_string)
    elif another == 'q':
        exit()


index_data = load_index_data(sys.argv)
polish_phrases = index_data.keys()
polish_phrases_string = get_polish_phrases_string(polish_phrases)
ask_questions(index_data, polish_phrases_string)
