#!/usr/bin/python4.6
import sys
import subprocess

# printing that the script has start
print("Starting script...\n")

# defined some default variabiles
php_cli = ["php"]
default_force = ["-f"]
default_langs = ["en_US", "nl_NL"]
langs = sys.argv
magento_path = ["bin/magento"]

# enable modules just installed?
# example: module_name


def enable_module(module_name):
    """
    Enable a Magento 2 module.
    """
    global php_cli
    global magento_path

    print(f"Enable module {module_name}.")
    subprocess.run([php_cli, magento_path, "module:enable", module_name])
    print("Setup upgrade.")
    subprocess.run([php_cli, magento_path, "setup:upgrade"])


def clear_data():
    """
    Remove Magento 2 static content.
    """
    directory_list = ["generated/*", "pub/static/*", "var/cache/*", "var/page_cache/*", "var/view_preprocessed/*", "var/tmp/*"]

    print("Cleaning up Magento 2 static content...\n")

    for directory in directory_list:
        print(f"Cleaning files from {directory} path.")
        subprocess.run(["rm", "-rf", directory])

def static_deploy():
    """
    Deploying Magento 2 languges.
    """
    global langs
    global default_langs

    print("Setup di:compile.")
    subprocess.run([php_cli, magento_path, "setup:di:compile"])

    if langs == True:
        for item in langs:
            subprocess.run([php_cli, magento_path, "setup:static-content:deploy", default_force, item])
    else:
        for item in default_langs:
            subprocess.run([php_cli, magento_path, "setup:static-content:deploy", default_force, item])

def composer_require(module_name):
    """
    Install modules for Magento 2 using composer.
    """
    subprocess.run(["composer", "require", module_name])

enable_module("Etailors_Startup")
