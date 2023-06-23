# Arguments

args = {
  'create_user': {
    'command': 'user',
    'short': '-u',
    'required': False,
    'help': 'Create a new user',
    'default': None,
    'action': None,
    'type': str
  },

  'authenticate': {
    'command': 'auth',
    'short': '-a',
    'required': False,
    'help': 'Receives a username to authenticate',
    'default': None,
    'action': None,
    'type': str
  },

  'password': {
    'command': 'pasw',
    'short': '-p',
    'required': True,
    'help': 'Password for authentication',
    'action': None,
    'type': str
  },
}
