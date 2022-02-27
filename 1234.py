while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print('Bad' * 8)
    elif:
        num = int(reply)
        if num < 20:
            print('Low')
    else:
        print(int(reply) ** 2)
print( 'Bye' )
