import hashlib
BLOCKSIZE = 65536
def filesha1(path):
	hasher = hashlib.sha1()
	with open(path, 'rb') as afile:
	    buf = afile.read(BLOCKSIZE)
	    while len(buf) > 0:
	        hasher.update(buf)
	        buf = afile.read(BLOCKSIZE)
	print(hasher.hexdigest())


def filemd5(path):
	hasher = hashlib.md5()
	with open(path, 'rb') as afile:
	    buf = afile.read()
	    hasher.update(buf)
	print(hasher.hexdigest())


if __name__ == '__main__':
	print "1. Text."
	print "2. Hex"
	print "3. File"
		
	while True:
		k = input("Nhap k : ")	
		if (k == 1):
			s = raw_input("Nhap s:")
			print "Md5:",hashlib.md5(s).hexdigest()
			print "SHA1:",hashlib.sha1(s).hexdigest()
		if (k == 2):
			s = raw_input("Nhap s:")
			print "Md5:",hashlib.md5(s.decode("hex)")).hexdigest()
			print "SHA1:",hashlib.sha1(s.decode("hex")).hexdigest()
		if (k == 3):
			s = raw_input("Nhap path file:")
			print "Md5:", filemd5(s)
			print "SHA1:", filesha1(s)
		if (k > 3):
			break