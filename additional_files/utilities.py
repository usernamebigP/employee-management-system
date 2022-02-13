def read_file(filename):
      with open(filename, 'rb') as f:
          photo = f.read()
      return photo

def write_file(data,filename):
    with open(filename, 'wb') as f:
        f.write(data)