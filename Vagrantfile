Vagrant::Config.run do |config|
  config.vm.box = "vagrant_wheezy_3"
  config.vm.box_url = "http://vagrantboxes.footballradar.com/wheezy64.box"
  config.vm.provision :chef_solo do |chef|
      chef.cookbooks_path = "cookbooks"
      chef.add_recipe("apt")
      chef.add_recipe("python::setuptools")
      chef.add_recipe("testing::headless_selenium")
  end
  config.vm.provision :shell, :path => "dev-vm/setup.sh"
end
