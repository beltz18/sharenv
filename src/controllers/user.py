import bcrypt
import requests
import json

salt = bcrypt.gensalt()

def create_user(user,passw):
  """
  This function creates a user with a hashed password and sends a POST request to a specified API
  endpoint.
  
  :param user: The username of the user that needs to be created
  :param passw: The password of the user that needs to be hashed and stored securely
  :return: the response from the API call to create a new user in JSON format.
  """
  bytes = passw.encode('utf-8')
  user = {
    "user": user,
    "pasw": str(bcrypt.hashpw(bytes, salt))
  }
  res = requests.post('https://sharenv-api.onrender.com/user/create', json=user).text
  return json.loads(res)

def auth(user,passw):
  """
  This function authenticates a user by sending a POST request to an API endpoint and checking if the
  password matches the hashed password stored in the user's data.
  
  :param user: The username of the user trying to authenticate
  :param passw: The password of the user trying to authenticate
  :return: either a dictionary containing a success message and user data if the authentication is
  successful, or a dictionary containing an error message if the authentication fails.
  """
  bytes = passw.encode('utf-8')
  user = {
    "user": user
  }
  res = requests.post('https://sharenv-api.onrender.com/user/auth', json=user).text
  res = json.loads(res)

  if 'data' in res:
    userData = res['data']

    if bcrypt.checkpw(bytes, userData['password'][2:-1].encode('utf-8')):
      return res
    else:
      return { 'message': 'Wrong password' }

  return res