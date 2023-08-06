import hashlib

# VP1000b: de2a4ec338f3d03fe9a8dc44db61d756a1bf7906

key = input('Provide part of the known password only: ')
hash_value = input('Provide the password\'s hash: ')
totalN = input('Provide the full masked password: ')
abc = 'qazxswedcvfrtgbnhyujmkiolpPOLIKMJUYHNBGTRFVCDEWSXZAQ!@#$%^&*()-+1234567890'

def cal(newstr):
    global hash_value, hexa

    for letter in abc:
        current_str = newstr + letter

        if len(current_str) < len(totalN):
            cal(current_str)
        else:
            encode = current_str.encode()
            hashed = hashlib.sha1(encode)
            hexa = hashed.hexdigest()
            if hash_value == hexa:
                print('\n\rThe clear-text password: '+current_str + '\n\rThe hash: ' + hexa)
                return

cal(key)
