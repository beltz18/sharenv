def create_user(user,passw):
  with open('./src/lib/data.txt', mode='r', encoding='utf-8') as f:
    line = f.read()
    a = line.split(',')
    if user == a[0][5:]:
      print('this user already exists')
    else:
      with open('./src/lib/data.txt', mode='a', encoding='utf-8') as f:
        u = f'user:{user},'
        p = f'passw:{passw}\n'
        f.write(u)
        f.write(p)
      print(f'new user created: {user,passw}')

def auth(user,passw):
  with open('./src/lib/data.txt', mode='r', encoding='utf-8') as f:
    line = f.read()
    a = line.split(',')
    if user == a[0][5:] and passw == a[1][6:-1]:
      print('user authenticated succesfully')
    else:
      print('incorrect user or password')