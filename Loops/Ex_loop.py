data = {'color': 'red',
           'fruit': 'apple',
           'pet': 'dog',
          'car': 'van',
          }
keys = list(data.keys())
x = 0
while x < len(keys):
    key = keys[x]
    value = data[key]
    print(key + ':' + value)
    x+=1

