#6510615278 Wongsathorn Derochanawong
def fn1():
    fn2()
    x = 10
    print('fn1: x = %d' %x)

def fn2():
    x = 5
    print('fn2: x = %d' %x)

def main():
    x = 100
    fn1()
    print('main: x = %d' %x)

main()