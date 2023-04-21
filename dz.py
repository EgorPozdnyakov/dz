
def ip(command=input('введите IP: ').split('.')):
    for i in command:
        result = all(map(lambda i: True if int(i) >=0 and int(i) <=155 else False,command))
    if result == True and len(command)==4:
        print(True)
    else:
        print(False)
    return result
ip()