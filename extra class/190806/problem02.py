import random


def make_manito(*args):
    for i in range(len(args)):
        if args[i] == args[-1]:
            print(f'{args[i]} => {args[0]}')
        else:
            print(f'{args[i]} => {args[i+1]}')

# 강강술래 => 컴퓨터적인 방식이 아니라 사람 생각이 가장 적합한 문제 

make_manito('a', 'b', 'c', 'd')  # a => c, d => a, b => d, c => b