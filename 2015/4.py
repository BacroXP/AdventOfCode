import libs.input
import hashlib

word = libs.input.file()[0]
both = {}

i = 0
while len(both) != 2:
    if 1 in both:
        pass
    else:
        if hashlib.md5((word + str(i)).encode('utf-8')).hexdigest()[:5] == '00000':
            both[1] = i

    if 2 in both:
        pass
    else:
        if hashlib.md5((word + str(i)).encode('utf-8')).hexdigest()[:6] == '000000':
            both[2] = i
    
    i += 1

print(both[1])
print(both[2])
