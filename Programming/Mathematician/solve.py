import numpy as np
import re
import pwn

address = "109.232.232.225"
port = 15003
ans = ''

lines = []
summ = []
results = []

if __name__ == "__main__":
	r = pwn.remote(address, port)
	
	for i in range(100):
		recv = r.recvrepeat(1.2)
		recv = recv.decode()
		print(recv)
		datas = recv.split("\n")
		for line in datas:
			if "PASSWORD" in line:
				lines.append(line)
		for line in lines:
			line = line.replace('[+]', '')
			line = re.sub("\*[A-Z ]*\[\s*\d+\]\s*(\+|\=)", "", line)
			line = line.split()
			line = list(map(int, line))
			results.append(line.pop(-1))
			summ.append(line)
		
		x = np.linalg.solve(summ, results)
		y = list(map(round, x))
		for el in y:
			ans += chr(el)
		print(f"{i}: " + ans)
		r.sendline(ans.encode())
		summ = []
		lines = []
		results = []
		datas = []
		ans = ""
	print(recv)
	recv = r.recvrepeat(5)
	print(recv)