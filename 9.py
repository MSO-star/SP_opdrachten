def Cyclisch_verschuiven(ch, n):
    #ch_binary= ord(ch)
    ch_bin= "{0:8b}".format(ch)
    if n >=0 :
        res=((ch_bin)* 2**n)
        print(res)
    else:
        res=ch_bin/ 2**n
        print(res)

    print(res)
Cyclisch_verschuiven(88, 3)

def cy(ch,n):
    if n>=0:
        rest=ch* 2**n
        print(rest)
    else:
        rest= ch*2**n
        print(rest)

    ch_bin = "{0:8b}".format(rest)
    print(rest)

