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

    # Python3.5
    apt-get install -y python3.5-dev python3.5-doc libpython3.5 python3-pymysql

    # PyPy compatible Python3.3
    wget https://bitbucket.org/pypy/pypy/downloads/pypy3.3-v5.2.0-alpha1-linux64.tar.bz2
    bzip2 -dc pypy3.3-v5.2.0-alpha1-linux64.tar.bz2 | tar xf -
    mv pypy3.3-v5.2.0-alpha1-linux64 /opt/pypy3.3
    ln -s /opt/pypy3/bin/pypy3.3 /usr/bin/pypy3.3

    # create virtual env
    apt-get install -y git python-pip
    pip install virtualenv virtualenvwrapper

    echo "export WORKON_HOME=~/.virtualenvs" >> . bashrc
    echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python" >> .bashrc
    echo "export VIRTUALENVWRAPPER_VIRTUALENV=/home/vagrant/.local/bin/virtualenv" >> .bashrc
    echo "source /home/vagrant/.local/bin/virtualenvwrapper.sh" >> .bashrc

    source .bashrc
    mkvirtualenv -p /opt/pypy3.3/bin/pypy3.3 pypy && deactivate
    mkvirtualenv -p /usr/bin/python3.5 python3 && deactivate
  SHELL
end
