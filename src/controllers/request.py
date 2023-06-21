import controllers.user as u

def req(args):
  # Create a new user if doesn't exist
  if args['n'] != None and args['p'] != None:
    u.create_user(args['n'], args['p'])
  # Authenticate a user
  if args['a'] != None and args['p'] != None:
    u.auth(args['a'], args['p'])