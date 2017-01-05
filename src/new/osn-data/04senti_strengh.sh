#!/bin/bash

rm ./tweets_raw/words/*0_out.txt

for FILE in $(ls ./tweets_raw/words/*txt);
do
  java -jar /vagrant/src/SentiStrength/SentiStrengthCom.jar sentidata /vagrant/src/SentiStrength/db/ input ${FILE}
done
