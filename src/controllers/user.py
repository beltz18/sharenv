import bcrypt

salt = bcrypt.gensalt()

def create_user(user,passw):
  bytes = passw.encode('utf-8')
  hash  = bcrypt.hashpw(bytes, salt)
  with open('./src/lib/data.txt', mode='r', encoding='utf-8') as f:
    line = f.read()
    a = line.split(',')
    if user == a[0][5:]:
      print('this user already exists')
    else:
      with open('./src/lib/data.txt', mode='a', encoding='utf-8') as f:
        u = f'{user},{hash}\n'
        f.write(u)
      print(f'new user created: {user,hash}')

def auth(user,passw):
  bytes = passw.encode('utf-8')
  with open('./src/lib/data.txt', mode='r', encoding='utf-8') as f:
    l = f.read()
    a = l.split(',')
    if user == a[0] and bcrypt.checkpw(bytes, a[1][2:-2].encode('utf-8')):
      print('user authenticated succesfully')
    else:
      print('incorrect user or password')