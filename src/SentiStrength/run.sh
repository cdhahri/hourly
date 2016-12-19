#!/bin/bash

java -jar SentiStrengthCom.jar sentidata ./db/ input ../rf/data_tmp/train/all_words.txt 
java -jar SentiStrengthCom.jar sentidata ./db/ input ../rf/data_tmp/test/all_words.txt 
