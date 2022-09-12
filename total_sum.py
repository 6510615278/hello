
total = 0 
i = 0 
for num in range(2, 101, 2):
    print(f'{num:4d}', end='')
    total += num
    i += 1
    if i % 10 == 0:
        print() 
print()
print('total = %d' %(total))