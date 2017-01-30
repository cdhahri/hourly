#!/bin/bash

rm data/04.txt
java -jar /vagrant/src/SentiStrength/SentiStrengthCom.jar sentidata /vagrant/src/SentiStrength/db/ input ./data/03.txt
mv data/030_out.txt data/04.txt
