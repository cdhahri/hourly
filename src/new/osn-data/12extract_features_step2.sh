#!/bin/bash

cd extract_features_step2
./02feature_week.py
./02feature_day_night.py
./03feature_hashtags_count.py
./04feature_mentions_count.py
./05feature_favourites_count.py
./06feature_media_count.py
./07feature_source.py
./08feature_active_passive.py
./09feature_mentions.py
./12feature_coordinates.py
./13feature_top_mentions.py

cd ../extract_features_step3/
# ./01feature_count_all_capital.py
# ./02feature_count_exclamation_mark.py
# ./03feature_count_question_mark.py
# ./04feature_count_negative_word.py
# ./05feature_count_positive_word.py
# ./06feature_exist_more_than_three_dots.py
# ./07feature_exist_more_than_three_vowels.py
