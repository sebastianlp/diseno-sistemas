# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04-i386"
  config.vm.network "forwarded_port", guest: 8000, host: 8000, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 5000, host: 5000, host_ip: "127.0.0.1"
  # Work around disconnected virtual network cable.
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--cableconnected1", "on"]
    vb.name = "DjangoTP"
  end
  config.vm.provision "shell", inline: <<-SHELL
    apt-get -qqy update
    apt-get -qqy upgrade
    apt-get -qqy install make zip unzip python3 python3-pip python python-pip postgresql
    pip3 install --upgrade pip
    pip2 install --upgrade pip
    echo "Done installing your virtual machine!"
  SHELL
end
