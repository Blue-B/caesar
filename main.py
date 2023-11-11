import string
alp = string.ascii_letters+string.digits

text=input('평문 : ')
while(1):
	try:
		key = int(input('문자열 이동 횟수'))
		break;
	except:
		print('숫자만 입력하세요.')

def encrypt():
	entext=''
	for i in range(len(text)):
		entext+=alp[alp.find(text[i])+key%len(alp)]
	return entext
	
print(f'암호화결과 : {encrypt()}')
