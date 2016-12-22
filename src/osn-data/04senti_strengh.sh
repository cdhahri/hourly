#!/bin/bash

rm /vagrant/data/osn-data/tweets/words/*0_out.txt

for FILE in $(ls /vagrant/data/osn-data/tweets/words/*txt);
do
  java -jar /vagrant/src/SentiStrength/SentiStrengthCom.jar sentidata /vagrant/src/SentiStrength/db/ input ${FILE}
done
