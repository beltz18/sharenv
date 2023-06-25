import controllers.user   as u
import controllers.config as c

def req(args):
  # Create a new user if doesn't exist
  if args['n'] != None and args['p'] != None:
    a = u.create_user(args['n'], args['p'])
    if a['status'] == True:
      c.write_config('user', args['n'])
    return a
  # Authenticate a user
  if args['a'] != None and args['p'] != None:
    a = u.auth(args['a'], args['p'])
    if a['status'] == True:
      c.write_config('user', args['a'])
    return a