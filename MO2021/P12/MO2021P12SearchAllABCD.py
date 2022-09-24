# coding: utf-8

from copy import copy
import time

class MO2021P12SearchAll():
	def __init__(self, board_size:int = 7, expected_coins_number=7*7):
		self.board_size = board_size
		self.board_with, self.board_height = self.board_size - 1, self.board_size - 1
		pos = self.board_with // 2
		self.expected_coins_number = expected_coins_number
		self.nodes = [ ([pos], []) ]
		self.coins_dic = {(pos): 1}
		self.max_coins, self.max_coins_path = -1, dict()

	def pos2xy(self, pos:int)->tuple:
		y0, x0 = divmod(pos, self.board_size)
		return (x0+1, y0+1)

	def op_abcd(self, op:str, pos:int, coins:list)->list:
		y, x = divmod(pos, self.board_size)
		ret = []
		if op == 'a':
			pos1 = (y+1)*self.board_size + x
			if y+1 > self.board_height or pos1 in coins:
				return []
			else:
				return [pos1]
		elif op == 'b':
			for dxy in range(1, self.board_height+1):
				pos1 = (y + dxy) * self.board_size + (x - dxy)
				if x-dxy < 0 or y+dxy > self.board_height:
					break
				if pos1 not in coins:
					ret.append(pos1)
			return ret
		elif op == 'c':
			for dxy in range(1, self.board_height + 1):
				pos1 = (y+dxy)*self.board_size + (x+dxy)
				if x + dxy > self.board_with or y + dxy > self.board_height:
					return ret
				if pos1 not in coins:
					ret.append(pos1)
			return ret
		else:  #  op=='d'
			if y+1 > self.board_height:
				return []
			pos1 = (y+1)*self.board_size + (x-1)
			if x - 1 >= 0 and pos1 not in coins:
				ret.append(pos1)
			pos2 = (y+1)*self.board_size + (x+1)
			if x + 1 <= self.board_with and pos2 not in coins:
				ret.append(pos2)
			return ret

	def search_max_coins(self):
		while True:
			if len(self.nodes) == 0:
				print('searched all')
				return (self.max_coins, self.max_coins_path)
			if (self.max_coins == self.expected_coins_number): #  and len(self.max_coins_path) >= 5):
				print('reached the expected coins : ', self.expected_coins_number )
				return (self.max_coins, self.max_coins_path)
			coins, path = self.nodes.pop()
			l = len(coins)
			if l == 0:
				continue
			for i in range(l):
				coins1 = copy(coins)
				pos:int = coins1[i]
				pos_y = pos // self.board_size
				if pos_y >= self.board_height:
					continue
				del coins1[i]
				for op in ('a', 'b', 'c', 'd'):
					coins_1: list = copy(coins1)
					ret = self.op_abcd(op, pos, coins_1)
					path_1:list = copy(path)
					path_1.append((pos, op))
					coins_1.extend(ret)
					if len(coins_1) > self.max_coins:
						self.max_coins = len(coins_1)
						self.max_coins_path= {tuple(sorted(coins_1)): [path_1]}
						# self.max_coins_path = [(coins_1, path_1)]
					elif len(coins_1) == self.max_coins:
						t = tuple(sorted(coins_1))
						if t in self.max_coins_path:
							self.max_coins_path[t].append(path_1)
						else:
							self.max_coins_path[t] = [path_1]
					coins_t = tuple(sorted(coins_1))
					if (coins_t not in self.coins_dic):
						self.coins_dic[coins_t] = 1
						self.nodes.append((coins_1, path_1))
					else:
						self.coins_dic[coins_t] += 1


if __name__ == '__main__':
	m2021p12 = MO2021P12SearchAll(7, 20)
	st = time.time()
	ret =  m2021p12.search_max_coins()
	t = int(time.time() - st)
	tm, ts = divmod(t, 60)
	th, tm = divmod(tm, 60)
	print(f'elapsed time  {th}:{tm}:{ts}')
	path_total=0
	for paths in ret[1].values():
		path_total += len(paths)
	print(f'max: {ret[0]} coins ------ {len(ret[1])} conins examples, {path_total} paths')
	no = 0
	for coins, paths in ret[1].items():
		no += 1
		print(f'\ncoins No{no} ', end=' ')
		for pos in coins[:-1]:
			print(f'{(m2021p12.pos2xy(pos))}', end=',')
		print(f'{(m2021p12.pos2xy(coins[-1]))}')
		print(f'{len(paths)} paths')
		for path in paths:
			for pos_dir in path[:-1]:
				print(f'{(m2021p12.pos2xy(pos_dir[0]))}{pos_dir[1]}', end=', ')
			print(f'{(m2021p12.pos2xy(path[-1][0]))}{path[-1][1]}')

