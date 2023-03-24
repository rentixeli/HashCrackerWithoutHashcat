import hashlib

key = 'VP10' # 3 missing
hash= 'de2a4ec338f3d03fe9a8dc44db61d756a1bf7906'
abc = 'qazxswedcvfrtgbnhyujmkiolpPOLIKMJUYHNBGTRFVCDEWSXZAQ!@#$%^&*()-+1234567890'

for i in abc:
	for j in abc:
		for l in abc:
			newstr = key + i + j + l
			encode = newstr.encode()
			hashed = hashlib.sha1(encode)
			hexa = hashed.hexdigest()
			if hash == hexa:
				print (newstr + ' : ' + hexa)
