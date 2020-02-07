def cy(ch, n):
    if n >= 0:
       bits = 8
       shifted_no = ch * (2 ** bits)

    else:
       bits=8
       shifted_no = ch /(2**bits)


    ch_bin = "{0:8b}".format(shifted_no)
    print(shifted_no)
    print(ch_bin)

cy(92,-4)