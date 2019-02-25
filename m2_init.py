#!/usr/bin/python3
import sys
import subprocess

arguments = sys.argv
del arguments[0]
print("[ + ] Arguments list added:", arguments[0:], "\n")

def clear_data():
    """
    This function will remove Magento 2 static content.
    """
    dir_list = ["generated/*", "pub/static/*", "var/cache/*", "var/page_cache/*", "var/view_preprocessed/*", "var/tmp/*"]

    for item in dir_list:
        print("[ - ] Removing", item, "\n")
        subprocess.run(["rm", "-rf", item])

def init_func(args):
    """
    This function will initialize the Magento 2 content and update
    the new installed modules.
    """
    try:
        print("[ + ] Updating modules!\n")
        subprocess.run(["php", "bin/magento", "setup:upgrade"])
        print("[ + ] Compiling!\n")
        subprocess.run(["php", "bin/magento", "setup:di:compile"])

        for arg in args:
            print("Deploy using", arg)
            subprocess.run(["php", "bin/magento", "setup:static-content:deploy", "-f", arg])
    except FileNotFoundError:
        print("Wrong file or file path for php!")

def main():
    clear_data()
    init_func(arguments)

main()
