'''
	[문제]
		어느 농장에는 토끼와 오리가 모두 35마리가 있다. 
		토끼와 오리의 다리의 수의 합이 96개일 때, 
		토끼와 오리는 각각 몇 마리 인지 주석으로 표현하시오.
	[정답]
		토끼 = 13
		오리 = 22
'''
'''
토끼 a 
오리 b 
a + b = 35
b = 35 - a

4a + 2b = 96
4a + 2(35 - a) = 96
4a + 70 - 2a = 96
2a = 26

a = 13
b = 22
'''
total = 35 
leg_total = 96
rabit = 13
duck = 22

print(rabit + duck == total and rabit * 4 + duck * 2 == leg_total)