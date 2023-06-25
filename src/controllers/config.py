import json
import os

default = {
  'version': 'v0.3',
  'user': '',
  'spaces': [],
  'files': []
}

def read_config():
  """
  This function reads a JSON configuration file and returns its contents, or creates an empty file if
  it doesn't exist.
  :return: The function `read_config()` returns the data read from the `_config.json` file located in
  the `./src/lib/` directory. If the file does not exist, it creates an empty file and returns an
  empty list.
  """
  if not os.path.isfile('./src/_config.json'):
    with open('./src/_config.json', 'w') as file:
      json.dump(default, file)
  with open('./src/_config.json', 'r') as file:
    data = json.load(file)
  return data

def write_config(prop, val):
  """
  This function writes a new property and its value to a JSON configuration file.
  
  :param prop: prop is a string representing the name of the property to be updated in the
  configuration file
  :param val: The value that you want to set for the specified property in the configuration file
  """
  f = read_config()
  f[prop] = val
  with open("./src/_config.json", "w") as file:  
    json.dump(f, file)