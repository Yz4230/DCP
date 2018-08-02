def log(data):
    logfile = open('log.txt', 'w')
    logfile.write(str(data))
    print('Logfile was saved.')
