$script = <<SCRIPT
sudo apt-get update

# git
sudo apt-get -y install git

# mysql
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'
sudo apt-get install -y libmysqlclient-dev \
                        mysql-server
# sudo service mysql [status|start|stop|restart]

# python 3
sudo apt-get -y install build-essential \
                        python3 \
                        libxml2-dev \
                        libxslt1-dev \
                        python3-dev
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3.4 /usr/bin/python

# pip
sudo apt-get -y install python3-pip
sudo pip3 install --upgrade pip
sudo pip3 install schedule
sudo pip3 install pyquery
sudo pip3 install mysqlclient

# nginx
sudo apt-get install -y nginx

# WordNet deps
sudo apt-get install -y tk-dev
# http://wordnetcode.princeton.edu/3.0/WordNet-3.0.tar.gz
# vi src/stubs.c
# before #include <tcl.h>
# add #define USE_INTERP_RESULT 1
# export PATH="${PATH}:/usr/local/WordNet-3.0/bin
# export WORDNET_INSTALL=$(pwd)/WordNet-3.0
# LDFLAGS=-L${WORDNET_INSTALL}/lib
# LIBS=-lWN
# gcc ${LDFLAGS} -c marouen.c -o marouen ${LIBS} 

# nltk
#python -m nltk.downloader all

# machine learning
sudo pip install numpy
sudo pip install scipy
sudo pip install scikit-learn

# SentiStrengh
wget http://sentistrength.wlv.ac.uk/SentiStrengthCom.jar
wget http://sentistrength.wlv.ac.uk/SentStrength_Data_Sept2011.zip
# java -jar SentiStrengthCom.jar sentidata ./db/ text love+u
# java -jar SentiStrengthCom.jar sentidata ./db/ input input.txt

sudo pip install matplotlib
SCRIPT

Vagrant.configure("2") do |default|
  default.vm.box = "ubuntu/trusty64"
  default.vm.hostname = "hourly"

  default.vm.network "forwarded_port", guest: 80, host: 8888

  # shell provisioning
  default.vm.provision "shell", inline: $script

  default.vm.provider "virtualbox" do |vbox|
    vbox.name = "hourly"
    vbox.memory = 2048
  end
end
