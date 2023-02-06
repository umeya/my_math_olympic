# coding: utf-8
import argparse
from itertools import permutations

def mo2023p9(N:int)->tuple: # (Sn, Pn, [A], [B], [C])
	"""
	 p1 + |p2-p1| + ... + |p_n - p_(n-1)| + p_n = Sn
	 を満たす順列を求める
	:return:
	 Sn : 定義式の和
	 Pn : 適する順列の総数
	 A  : p1=1, p_n=nの順列
	 B  : Aの順列と逆順の順列(p1=n,p_n=1)
	 C  : 項の値がn-1の前または後の項の値がnの順列
	"""
	S = N * 2 + 2
	P1n = [i for i in range(1, N+1)]
	count, A, B, C = 0, [], [], []
	for v in permutations(P1n):
		if v == (3,2,4,1):
			print('*')
		S0 = v[0] + v[-1]
		for i in range(N - 1):
			S0 += abs(v[i+1] - v[i])
		if S0 == S:
			count += 1
			if v[0] == 1:
				A.append(v)
			elif v[-1] == 1:
				B.append(v)
			else:
				C.append(v)
	return (S, count, A, B,  C)

for N in range(3,7):
	Sn, Pn, A, B, C = mo2023p9(N)
	print(f'{N=}, S{N}={Sn}, P{N}={Pn}  ----------------')
	print('  -- A')
	for no, L in enumerate(A, 1):
		print(f'   {no=} , {L}')
	print('  -- B')
	for no, L in enumerate(B, 1):
		print(f'   {no=} , {L}')
	print('  -- C')
	for no, L in enumerate(C, 1):
		print(f'   {no=} , {L}')
