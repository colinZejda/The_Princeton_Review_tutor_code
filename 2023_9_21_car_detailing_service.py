costService1 = 0
costService2 = 0

print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

serviceSelection1 = input('Select first service: \n')
serviceSelection2 = input('\nSelect second service: \n')
print('\n')
print('Davy\'s auto shop invoice\n')
#Service 1
if serviceSelection1 == 'Oil change':
    print('Service 1: %s, $35' % serviceSelection1)
    costService1 =35

if serviceSelection1 == 'Tire rotation':
    print('Service 1: %s, $19' % serviceSelection1)
    costService1 = 19

if serviceSelection1 == 'Car wash':
    print('Service 1: %s, $7' % serviceSelection1)
    costService1 = 7

if serviceSelection1 == 'Car wax':
    print('Service 1: %s, $12' % serviceSelection1)
    costService1 = 12
    
if serviceSelection1 == '-':
    print('Service 1: No service')


#Service 2  
if serviceSelection2 == 'Oil change':
    print('Service 2: %s, $35' % serviceSelection2)
    costService2 =35

if serviceSelection2 == 'Tire rotation':
    print('Service 2: %s, $19' % serviceSelection2)
    costService2 = 19

if serviceSelection2 == 'Car wash':
    print('Service 2: %s, $7' % serviceSelection2)
    costService2 = 7

if serviceSelection2 == 'Car wax':
    print('Service 2: %s, $12' % serviceSelection2)
    costService2 = 12

if serviceSelection2 == '-':
    print('Service 2: No service')

Total = costService1 + costService2
print('\nTotal: $%d' % Total)
