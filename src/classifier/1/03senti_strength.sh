#!/bin/bash

rm data/04.txt
rm data/04_pos.txt
rm data/04_neg.txt

java -jar /vagrant/src/SentiStrength/SentiStrengthCom.jar sentidata /vagrant/src/SentiStrength/db/ input ./data/03.txt
mv data/030_out.txt data/04.txt
java -jar /vagrant/src/SentiStrength/SentiStrengthCom.jar sentidata /vagrant/src/SentiStrength/db/ input ./data/03_pos.txt
mv data/03_pos0_out.txt data/04_pos.txt
java -jar /vagrant/src/SentiStrength/SentiStrengthCom.jar sentidata /vagrant/src/SentiStrength/db/ input ./data/03_neg.txt
mv data/03_neg0_out.txt data/04_neg.txt