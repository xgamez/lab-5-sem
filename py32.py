
import random

def gen_random(num_count: int, begin: int, end: int) -> iter:
   
    for i in range(num_count):
        yield random.randint(begin, end)

if __name__ == '__main__':
    print(str(list(gen_random(5, 1, 4)))[1:-1])
