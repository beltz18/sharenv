import controllers.user   as u
import controllers.space  as s
import controllers.config as c

def req(args):
  # Create a new user if doesn't exist
  if args['n'] != None and args['p'] != None:
    a = u.create_user(args['n'], args['p'])
    if a['status'] == True:
      c.write_config('user', args['n'])
    return a
  
  # Authenticate a user
  elif args['a'] != None and args['p'] != None:
    a = u.auth(args['a'], args['p'])
    if a['status'] == True:
      c.write_config('user', args['a'])
    return a
  
  # Create a new Space
  elif args['c'] != None and args['o'] != None and args['i']:
    a = s.create_space(args['c'], args['o'], args['i'])
    if a['status'] == True:
      spaces = s.load_spaces(args['o'])
      c.write_config('spaces', spaces['data'])
    return a
  
  # Add new user to Space
  elif args['s'] != None and args['i'] != None:
    a = s.add_member(args['s'], args['i'])
    if a['status'] == True:
      spaces = s.load_spaces(args['o'])
      c.write_config('spaces', spaces['data'])
    return a
  
  else:
    return {
      'message' : "Invalid request",
      'status': False
    }