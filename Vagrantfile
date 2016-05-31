# -*- mode: ruby -*-
# vi: set ft=ruby :

box = "ubuntu/wily64"

Vagrant.configure(2) do |config|
  config.vm.box = box

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end

  config.vm.synced_folder ".", "/home/vagrant/app"

  config.vm.provision "shell", inline: <<-SHELL
    set -e
    sed -i.bak -e "s@http://us\.archive\.ubuntu\.com/ubuntu/@mirror://mirrors.ubuntu.com/mirrors.txt@g" /etc/apt/sources.list
    export DEBIAN_FRONTEND=noninteractive

    apt-get update
    apt-get install -y git

    # Python3.3
    apt-get install -y python3.3-dev python3.3-doc libpython3.3 python3-pymysql

    # PyPy compatible Python3.3
    wget https://bitbucket.org/pypy/pypy/downloads/pypy3.3-v5.2.0-alpha1-linux64.tar.bz2 -O pypy3.tar.bz2
    bzip2 -dc pypy3.tar.bz2 | tar xf -
    sudo mv pypy3 /opt/
    sudo ln -s /opt/pypy3/bin/pypy3 /usr/bin/pypy3
  SHELL
end
