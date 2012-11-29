Debian 6, Chef, Django, Nose, Selenium & Behave VM, provision by Vagrant
------------------------------------------------------------------------

What this repo gives you
========================

This repo provides you with a working, template Django project with unit
("developer") tests running under Nose, and working, de-coupled Selenium
("customer") tests driven by Behave (a Cucumber / Lettuce style Behavioural
Testing harness).

This repo will work on Mac, Linux, or Windows, since all the execution and test
running takes place on a Debian Virtual Machine, run by VirtualBox/Vagrant.

The VM itself is configured by chef-solo. This ia all handled automatically by
this repo.


Installing this VM
==================

4 steps:

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

2. Install [Vagrant](http://downloads.vagrantup.com/)

3. Clone this repo:
    ```
    $ git clone git@github.com:mhenwood/django-selenium-vagrant.git
    ```

4. Vagrant up:
    ```
    $ cd django-selenium-vagrant
    $ vagrant up
    ```

This downloads the box image, imports it, runs it, applies the Chef recipes,
then installs the Python pip packages in requirements.txt and
test-requirements.txt. Allow about 10 minutes for this one-off setup step.

You then need to connect to an ssh session on that VM. On Mac / Linux, simply:
```
$ vagrant ssh
```

On Windows, download an ssh client such as [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html),
then connect an ssh session to 127.0.0.1:2222, with username 'vagrant' and
password 'vagrant'.

Whichever host OS you are using, once connected to the VM, run:
```
$ cd /vagrant
$ source ~/bin/activate
```

The /vagrant folder is a share to the project clone folder on your host machine
(in the standard Vagrant fashion).

Running the Developer (unit) tests
==================================

From the /vagrant directory, and with the virtualenv activated (as above):
```
$ ./run_developer_tests.sh
```

This PEP8s the codebase, then invokes the Django Nose test runner.

Running the Customer (Selenium) tests
=====================================

From the /vagrant directory, and with the virtualenv activated (as above):
```
$ python run_customer_tests.py
```

This starts up a Django testserver, and runs Behave against the feature files
in the 'features/' folder of this project. It runs Selenium headlessly on the
Debian VM using Xvfb.

The build layers
================

The build consists of 3 layers:

1. Debian 6 'vagrant' base box - this is downloaded from Dropbox upon
first run of ```vagrant up```.

2. Chef-Solo configuration of that box, which updates the apt repo, adds
Python setuptools, and Xvfb + Iceweasel for running the headless Selenium
tests. This is handled by the following:
    - recipes in the 'cookbooks/' folder of this project - add other chef
    cookbooks to this folder
    - ```add_recipe``` calls in the Vagrantfile - hook up other chef
    recipes by amending this

3. pip-based install of project requirements - this is handled by the
Vagrant VM's bootstrapping script which is located in 'dev-vm/setup.sh' in
this project. This shell script installs a virtualenv on the VM and
pip installs the packages listed in 'requirements.txt' and
'test-requirements.txt' in this project, all at initial boot up.

Test Output, from this repo
===========================

Developer Tests
```
$ source ~/bin/activate
$ cd /vagrant
$ ./run_developer_tests.sh
Cleaning .pyc files
Running PEP8 checks
Running django-nose tests
nosetests --verbosity 1 --exe
Creating test database for alias 'default'...
.
----------------------------------------------------------------------
Ran 1 test in 0.017s

OK
Destroying test database for alias 'default'...
django-nose tests passed
```

Customer Tests
```
$ source ~/bin/activate
$ cd /vagrant
$ python run_customer_tests.py
Starting django testserver
Starting Xvfb
Feature: I have a charming website # features/basic.feature:1

  Scenario: Saying "hello" to my website elicits a charming response  # features/basic.feature:3
    When I open the basic hello page                                  # features/steps/hello.py:8
    Then I receive an ambiguously flirtatious response                # features/steps/hello.py:13


1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
2 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.1s
Stopping django testserver
Stopping Xvfb
```

Caveat / chiz
=============

Ignore the ```[dix] font load error``` messages during the Customer tests. This
is a side-effect of using X Virtual Frame Buffer instead of a desktop
environment.
