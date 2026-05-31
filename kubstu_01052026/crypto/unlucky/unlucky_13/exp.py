import hashlib, math, gmpy2
from decimal import Decimal
from Crypto.Util.number import long_to_bytes,bytes_to_long

# c is your large ciphertext integer

n = 13658633037131788032351618427072247476717954542396408633560773884364554559070511401338131068909519714863439032980842522861580506135888588760180791057787733146681063635707678102393673406833618170820088193214167654538266905388169622081314446011833404506211472257999343805354237884172011540789567531049972285279517155764888481047450059
e = 3
c = 58106402945252412885867908042116794819464305744971899578073020304067543548070807457178658563488157040731309267600804875202490191851964629071348907183348604959890636799938893288492152226256276862912678404321252232876509325092153164813635360471085498336853220078206620458027876601442698309483452313201963351276803179820555434275959791505894082437152805771101360567738286600728

#FLAG = open("flag.txt", "rb").read().strip()
FLAG=b"0000000000000000"

def cursed_prng(seed, length):
    state = seed
    stream = []
    for _ in range(length):
        state = (state * 1313 + 131313) % (2**32)
        stream.append(state & 0xFF)
    return bytes(stream)

UNLUCKY_NUMBER = 13

#layer1 = bytes(a ^ b for a, b in zip(
#    FLAG,
#    cursed_prng(UNLUCKY_NUMBER, 64)#len(FLAG))
#))

def get_flag(layer1):
    res = bytes(a ^ b for a,b in zip(layer1, cursed_prng(UNLUCKY_NUMBER,64)))
    return res

def forgotten_cipher(key, data):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    out = []
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(byte ^ S[(S[i] + S[j]) % 256])
    return bytes(out)


secret = b"Unlucky" + str(UNLUCKY_NUMBER).encode()
fc_key = hashlib.sha256(secret).digest()[:16]

m, exact = gmpy2.iroot(c, 3)
if exact:
    print("Message found:", m)
#m = math.cbrt(Decimal(c))
#print(m)
int_m = int(m)
layer1 = forgotten_cipher(fc_key, long_to_bytes(int_m))
FLAG = get_flag(layer1)
print(FLAG)


