from Crypto.Cipher import DES3,DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

var_1 = b"N1nt3ndo"
var_2 = b"S3cur1ty"
#print(bytes.fromhex("4b33792132303236").decode('utf-8'))
var_3 = b"K3y!2026"

key = var_1 + var_2 + var_3


ivx = bytes.fromhex("0a001f0273760054")
ivm  = b"M4r10Br0"
iv = bytes([a ^ b for a,b in zip(ivx,ivm)])
#print(iv) #b'G4m3C4rd'

cipher = bytes.fromhex("072a8e75459a545679f3aa56a9fafb38871022de0c9bd5d7ef55e8dad7861662eb0fb630d9cdf9dd8c64a3a8ac28b86a")

cipher_decrypt = DES3.new(key, DES3.MODE_CBC, iv)
decrypted_padded = cipher_decrypt.decrypt(cipher)
# Remove padding
original_data = unpad(decrypted_padded, DES3.block_size, style='pkcs7')

#print(f"Original Message: {original_data}")
print(f"Original Message: {original_data.decode('utf-8')}")

