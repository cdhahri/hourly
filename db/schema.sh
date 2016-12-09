#!/bin/bash

mysql -uroot -proot -hlocalhost -P3306 < /vagrant/db/schema.sql
