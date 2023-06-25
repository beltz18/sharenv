# Arguments

args = {
  'user': { #0
    'command': ['user', 'auth'],
    'short': ['-u', '-a'],
    'required': False,
    'help': [
      'Create a new user',
      'Receives a username to authenticate'
    ],
    'default': None,
    'action': None,
    'type': str
  },

  'space': { #1
    'command': ['create', 'add', 'rename', 'delete', 'user', 'file'],
    'short': ['-n', '-s', '-r', '-d', '-i', '-f'],
    'required': False,
    'help': [
      'Receives a name and creates a space with that name',
      'Receives a space to add a new member',
      'Rename the space given by name',
      'Delete the space with all the files inside',
      'Add or remove users from spaces',
      'List all of your available files in that space'
    ],
    'default': 'list',
    'action': None,
    'type': str
  },

  'file': { #2
    'command': ['new', 'name', 'space', 'list'],
    'short': ['-f', '-n', '-s', '-l'],
    'required': False,
    'help': 'Creates a new entry for an .env file',
    'default': None,
    'action': None,
    'type': str
  },

  'version': '' #3
}
