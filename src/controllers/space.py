import requests
import json
from controllers.config import read_config, write_config

config = read_config()

def create_space(s,o,i):
  """
  The function creates a new space with specified parameters and sends a POST request to an API
  endpoint.
  
  :param s: The name of the space being created
  :param o: The parameter 'o' in the function 'create_space' represents the owner of the space being
  created
  :param i: The parameter "i" in the function "create_space" represents the list of users who have
  been invited to the space
  :return: the response from a POST request to create a new space in a specified API endpoint. The
  response is in JSON format and contains information about the newly created space, including its
  name, owner, and invited members.
  """
  space = {
    'space': s,
    'owner': o,
    'invited': i
  }
  res = requests.post(f"{config['api']}/space/create", json=space).text
  res = json.loads(res)
  return res

def load_spaces(u):
  """
  The function loads a list of spaces associated with a given user from an API endpoint.
  
  :param u: The parameter 'u' is likely a variable that represents a user object or identifier. It is
  used to create a dictionary called 'mySpaces' with the key 'user' and the value of the user object
  or identifier. This dictionary is then sent as a JSON payload in a POST request to a
  :return: a JSON response from an API endpoint that lists spaces associated with a given user.
  """
  mySpaces = { 'user': u }
  res = requests.post(f"{config['api']}/space/list", json=mySpaces).text
  res = json.loads(res)
  return res

def add_member(s,u):
  yourSpaces = config['spaces']['spacesOwned']
  if not s in yourSpaces:
    return {
      'message': 'Space does not exists or you are not the owner',
      'status': False
    }
  
  add = {
    'space': s,
    'invited': u
  }
  res = requests.post(f"{config['api']}/space/update", json=add).text
  res = json.loads(res)
  return res