from selenium_codes import sub4sub_websites_selenium as sws
from configparser import ConfigParser
import os

heroku = "not available"
try:
    heroku = os.environ['HEROKU']
    print("Running HEROKU Version new account")
except KeyError:
    print("Running Local Version")
    pass

if __name__ == "__main__":
    sws.goviral_functions()
