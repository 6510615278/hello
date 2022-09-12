#6510615278 Wongsathorn Derochanawong
total = 0
count = 0

score = int(input('Input score (-1 to end): '))
while score != -1:
  if 0 <= score <= 100:
    total = total + score
    count = count + 1
    score = int(input('Input score (-1 to end): '))
  else:
    print('invalid input')
    score = int(input('Input score (-1 to end): '))



average = total/count
print('total = %d' %total)
print('count = %d' %count)
print('average = %d' %average)