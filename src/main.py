from argparse            import ArgumentParser
from var.args            import args
from controllers.request import req

def define_args():
  """
  Defines arguments using the ArgumentParser module
  """
  p = ArgumentParser(description='Arguments for Sharenv')

  for arg in args:
    for a in arg.keys():
      p.add_argument(
        f'{arg[a]["command"]}',
        f'{arg[a]["short"]}',
        required=arg[a]['required'],
        help=arg[a]['help'],
        action=arg[a]['action'],
        type=arg[a]['type'],
      )

  Args = p.parse_args()
  return Args

def proc_args(args):
  data = {
    'n':args.new_user,
    'a':args.auth,
    'p':args.passw,
  }
  a = req(data)
  return a