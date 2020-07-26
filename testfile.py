
def xor_crypt_string(data, key='vadesecure', encode=False, decode=False):
    from itertools import  cycle
    import base64

    if decode:
        data = data.decode("latin_1")
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(key)))

    if encode:
        return base64.encode(xored).strip()
    return xored
f=open("enonce.bin","rb")
data=f.read()
print(xor_crypt_string(data,decode = True))
