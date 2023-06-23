from var.args            import args
from controllers.request import req
import click

arg = [arg for arg in args]

@click.group()
def cli():
  pass

@cli.command('user')
@click.option(args[arg[0]]['short'], args[arg[0]]['command'], help=args[arg[0]]['help'], type=args[arg[0]]['type'], required=args[arg[0]]['required'])
@click.option(args[arg[1]]['short'], args[arg[1]]['command'], help=args[arg[1]]['help'], type=args[arg[1]]['type'], required=args[arg[1]]['required'])
@click.option(args[arg[2]]['short'], args[arg[2]]['command'], help=args[arg[2]]['help'], type=args[arg[2]]['type'], required=args[arg[2]]['required'])
def user(user,auth,pasw):
  data = {
    'n': user,
    'a': auth,
    'p': pasw
  }
  res = req(data)
  print(res['message'])