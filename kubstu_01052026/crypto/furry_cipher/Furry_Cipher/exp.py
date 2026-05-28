import string


def encrypt_custom(plaintext, key_values):
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    char_map = {ch: i for i, ch in enumerate(alphabet)} #A:0
    num_map = {i: ch for i, ch in enumerate(alphabet)}  #0:A
    #print("char_map",char_map)
    #print("num_map",num_map)

    result = []

    for i, char in enumerate(plaintext):
        #index i flows progressively
        #if it is one of them, hust appends 'em
        if char in '()_':
            result.append(char)

        elif char in char_map:
            num = char_map[char]
            key_val = key_values[i % 3]

            if i % 3 == 0:
                encrypted = (num * 13 + key_val * 7) % 62
            elif i % 3 == 1:
                encrypted = (num * 17 + key_val * 3 + 11) % 62
            else:
                encrypted = (num * 19 + (key_val ^ 42) + 23) % 62

            result.append(num_map[encrypted])
        else:
            result.append(char)

    return ''.join(result)


#in theory it returns the string
def decrypt(ciphertext,key_values):
    res = []
    index = 0
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    char_map = {ch: i for i, ch in enumerate(alphabet)} #A:0
    num_map = {i: ch for i, ch in enumerate(alphabet)}  #0:A
    for i, char in enumerate(ciphertext):
        if char in '()_':
            res.append(char)
        elif char in char_map:
            encrypted = char_map[char]    #index value of the character of the ciphertext wrt to alphabet
            key = key_values[i%3]
            #key?
            if i%3 == 0:
                num = (encrypted*(-19) - -19*7*key ) % 62
            elif i%3 == 1:
                num = (encrypted*11 - 11*(11 + 3*key) ) % 62
            else:
                num = (encrypted*(-13) - (-13)*(23 + 42^key) ) % 62 
            res.append(num_map[num])
        else:
            pass
        index += 1

    return "".join(res)
        





if __name__ == "__main__":
    flag = "XiEDJ5(9tV_qY3_v43_t9B3_o9vo_ESM_YR_YA_t_S5t8v_XYL4jt)"
    example_text = "Test123"
    example_key = [1, 2, 3]    #they wrap on 62
    encrypted_example = encrypt_custom(example_text, example_key)
    print(encrypted_example)
    #flag = 'Gfgiyko'
        

    for i in range(63):
        for j in range(63):
            for k in range(63):
                computed = decrypt(flag,[i,j,k])
                if "KubSTU" in computed:
                    print(decrypt(flag,[i,j,k]))
    
