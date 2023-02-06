# coding: utf-8

"""
2023年度問12
mo2023P12T1.pyの結果から、n=3,4,5,6でのf(g(x))=g(f(g(x)))の検算
"""

def mo2023P12T2():
	# n=3
	Nn = [[[0, 3, 2, 2], [0, 2, 2, 2]], [[0, 2, 2, 2], [0, 2, 2, 1]]]
	mo2023P12T2PP(Nn)
	# n= 4
	Nn=[[[0, 4, 4, 3, 3], [0, 4, 3, 3, 3], [0, 3, 3, 3, 3]],
		[[0, 4, 2, 2, 2], [0, 3, 2, 2, 2], [0, 2, 2, 2, 2]],
		[[0, 3, 3, 3, 3], [0, 3, 3, 3, 2], [0, 3, 3, 3, 1]],
		[[0, 2, 2, 2, 2], [0, 2, 2, 2, 1], [0, 2, 2, 1, 1]]]
	mo2023P12T2PP(Nn)
	# n=5
	Nn=[[[0, 5, 5, 3, 3, 3], [0, 5, 4, 3, 3, 3], [0, 5, 3, 3, 3, 3],
		 [0, 4, 4, 3, 3, 3], [0, 4, 3, 3, 3, 3], [0, 3, 3, 3, 3, 3]],
		[[0, 3, 3, 3, 3, 3], [0, 3, 3, 3, 3, 2], [0, 3, 3, 3, 3, 1],
		 [0, 3, 3, 3, 2, 2], [0, 3, 3, 3, 2, 1], [0, 3, 3, 3, 1, 1]]]
	mo2023P12T2PP(Nn)
	n=6
	Nn=[[[0, 6, 6, 6, 4, 4, 4], [0, 6, 6, 5, 4, 4, 4], [0, 6, 6, 4, 4, 4, 4],
		 [0, 6, 5, 5, 4, 4, 4], [0, 6, 5, 4, 4, 4, 4], [0, 6, 4, 4, 4, 4, 4],
		 [0, 5, 5, 5, 4, 4, 4], [0, 5, 5, 4, 4, 4, 4], [0, 5, 4, 4, 4, 4, 4],
		 [0, 4, 4, 4, 4, 4, 4]],
		[[0, 6, 6, 3, 3, 3, 3], [0, 6, 5, 3, 3, 3, 3], [0, 6, 4, 3, 3, 3, 3],
		 [0, 6, 3, 3, 3, 3, 3], [0, 5, 5, 3, 3, 3, 3], [0, 5, 4, 3, 3, 3, 3],
		 [0, 5, 3, 3, 3, 3, 3], [0, 4, 4, 3, 3, 3, 3], [0, 4, 3, 3, 3, 3, 3],
		 [0, 3, 3, 3, 3, 3, 3]],
		[[0, 4, 4, 4, 4, 4, 4], [0, 4, 4, 4, 4, 4, 3], [0, 4, 4, 4, 4, 4, 2],
		 [0, 4, 4, 4, 4, 4, 1], [0, 4, 4, 4, 4, 3, 3], [0, 4, 4, 4, 4, 3, 2],
		 [0, 4, 4, 4, 4, 3, 1], [0, 4, 4, 4, 4, 2, 2], [0, 4, 4, 4, 4, 2, 1],
		 [0, 4, 4, 4, 4, 1, 1]],
		[[0, 3, 3, 3, 3, 3, 3], [0, 3, 3, 3, 3, 3, 2],[0, 3, 3, 3, 3, 3, 1],
		 [0, 3, 3, 3, 3, 2, 2], [0, 3, 3, 3, 3, 2, 1], [0, 3, 3, 3, 3, 1, 1],
		 [0, 3, 3, 3, 2, 2, 2], [0, 3, 3, 3, 2, 2, 1], [0, 3, 3, 3, 2, 1, 1],
		 [0, 3, 3, 3, 1, 1, 1]]]
	mo2023P12T2PP(Nn)

def mo2023P12T2PP(Nn:list):
	print('MO2023P12 f(g(x))=g(f(g(x))) check')
	print(f'n={len(Nn[0][0]) - 1}')
	for i in range(len(Nn)):
		n4fg(Nn[i])


def n4fg(fg:list):
	fg_str0 = []
	for f in fg:
		fg_str0.append('(' +  ','.join([str(y) for y in f[1:]])  + ')' )
	fg_str1 = '{' + ','.join(fg_str0) + '}'
	print(f'A={fg_str1}')
	n,el = len(fg),len(fg[0])
	x = ' ' + ''.join([str(i) for i in range(1,el)]) + ' ,'
	for g in fg:
		print(f'{"x":^14},{x * n}')
		print(f'{"g(x)":^14},{(" " + "".join([f"{g[i]:1}" for i in range(1,el)]) + " ,")*n}')
		print(f'{"f(x)":^14},', end='')
		for f in fg:
			print(f'{" " + "".join([f"{f[i]:1}" for i in range(1, el)]) + " ,"}', end='')
		print()
		print(f'{"f(g(x))":^14},', end='')
		for f in fg:
			print(f'{" " + "".join([f"{f[g[i]]:1}" for i in range(1, el)]) + " ,"}', end='')
		print()
		print(f'{"g(f(g(x)))":^14},', end='')
		for f in fg:
			print(f'{" " + "".join([f"{g[f[g[i]]]:1}" for i in range(1, el)]) + " ,"}', end='')
		print()
		print()

"""
"""

mo2023P12T2()