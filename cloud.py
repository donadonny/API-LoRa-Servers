import urllib3.contrib.pyopenssl
import encodings
import requests
import json
from config import Config
import socket
import sys
import signal
from time import sleep
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.contrib.pyopenssl.inject_into_urllib3()


def handler(signum, frame):
    print("Function timeout was called!")
    raise Exception("func timeout")


class Cloud:
    """
    This is the constructor for the Gateway object.
    It will create a the object from the EUI given and will fetch other parameters from the database if the object already exist, based on the EUI.
    :return: the gateway object itself
    """
    def __init__(self):
        self.config_data = Config()
        self.post_counter = 0
        signal.signal(signal.SIGALRM, handler)


    def post_data(self, post_data):

        #signal.alarm(5)
        try:
            self.config_data.get_post_url() is not None
        except TypeError:
            print("Post URL is a Null value")
            return False

        try:
            json_data = json.dumps(post_data)
        except ValueError:
            print('Decoding JSON has failed')
            return False

        except TypeError:
            print("Not a valid json data")
            return False

        else:
            try:
                r = requests.post(self.config_data.get_post_url(), json_data, timeout=5, verify=False)
            except requests.exceptions.RequestException as e:
                print(e)
            except requests.exceptions.SSLError as e:
                print("That domain looks super sketchy. Error : ", str(e))
            except requests.HTTPError as e:
                print("HTTP Error ", str(e))
            except socket.gaierror:
                print("Unexpected error:", sys.exc_info()[0])
            except requests.exceptions.ConnectionError as e:
                print("Domain error , ", str(e))
            except Exception as e:
                print("Post error, reason: ", str(e))

            else:
                if r is not None:
                    #print("json: ", r.json)
                    return r
                else:
                    print("Error received: ", r.json)


    def get_data(self):
        
        #signal.alarm(5)
        try:
            self.config_data.get_get_url() is not None
        except TypeError:
            print("Post URL is a Null value")
            return False

        else:
            try:
                r = requests.get(self.config_data.get_get_url(), timeout=5, verify=False)
            except requests.exceptions.ConnectTimeout as e:
                print("Server took too long to respond!", str(e))
            except requests.exceptions.ConnectionError as e:
                print("These aren't the domains we're looking for. Error: ", str(e))       

            else:
                if r is not None:
                    #print("json: ", r.json)
                    return r
                else:
                    print("Error received: ", r.json)





