class Configuration:

  def get_configuration(choose):

    if(choose == 'local'):
      connect_value = dict(host='127.0.0.1',
        user='userid',
        password='password',
        database='database',
        port=3306,
        charset='utf8')

    elif(choose == 'aws'):
      connect_value = dict(host='rds.amazonaws.com',
        user='userid',
        password='password',
        database='password',
        port=3306,
        charset='utf8')

    else:
      print('Not Selected')
      connect_value = ''

    return connect_value
    
