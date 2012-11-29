#/bin/bash
# Prepping the Vagrant VM Python environment after chef-solo
#
easy_install virtualenv
virtualenv --no-site-packages /home/vagrant
source /home/vagrant/bin/activate && pip install -r /vagrant/requirements.txt -r /vagrant/test-requirements.txt && deactivate
chown -R vagrant:vagrant /home/vagrant
