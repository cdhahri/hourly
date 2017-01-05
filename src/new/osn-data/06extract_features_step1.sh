#!/bin/bash

cd extract_features_step1/
./01feature_count_all_capital.py
./02feature_count_exclamation_mark.py
./03feature_count_question_mark.py
./04feature_count_negative_word.py
./05feature_count_positive_word.py
./06feature_exist_more_than_three_dots.py
./07feature_exist_more_than_three_vowels.py
