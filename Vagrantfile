$script = <<SCRIPT
sudo apt-get update

# git
sudo apt-get -y install git

# python 3
sudo apt-get -y install build-essential \
                        python3 \
                        python3-dev
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3.4 /usr/bin/python

# pip
sudo apt-get -y install python3-pip
sudo pip3 install --upgrade pip
sudo pip3 install pyquery

# mysql
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'
sudo apt-get install -y mysql-server
# sudo service mysql [status|start|stop|restart]
SCRIPT

Vagrant.configure("2") do |default|
  default.vm.box = "ubuntu/trusty64"
  default.vm.hostname = "hourly"

  # shell provisioning
  default.vm.provision "shell", inline: $script

  default.vm.provider "virtualbox" do |vbox|
    vbox.name = "hourly"
    vbox.memory = 1024
  end
end
