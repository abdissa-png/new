def seive(num):
	prime=[True for i in range(num)]
	p=2
	while(p*p<=num):
		for i in range(p*p,num,p):
			prime[i]=False
		p+=1
	for i in range(2,num):
		if prime[i]==True:
			print(i,end=",")
seive(100000)
