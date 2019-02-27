#!/usr/bin/python3
import sys
import subprocess

# printing that the script has start
print("Starting script...")

# define some default variabiles
php_cli = ["php"]
default_force = ["-f"]
default_langs = ["en_US", "nl_NL"]
langs = sys.argv
magento_path = ["bin/magento"]

# enable any modules just installed?
# example: module_name


def enable_module(module_name):
    """
    Enable a Magento 2 module.
    """
    global php_cli
    global magento_path

#   print(f"Enable module {module_name}.")
    subprocess.run([php_cli, magento_path, "module:enable", module_name])
#	print("Setup upgrade.")
    subprocess.run([php_cli, magento_path, "setup:upgrade"])

def clear_data():
    """
    Remove Magento 2 static content.
    """
    directory_list = ["generated/*", "pub/static/*", "var/cache/*", "var/page_cache/*", "var/view_preprocessed/*", "var/tmp/*"]
	
	for directory in directory_list:
		print(f"Cleaning files from {directory} path.")
    	subprocess.run(["rm", "-rf", directory])

clear_data()
