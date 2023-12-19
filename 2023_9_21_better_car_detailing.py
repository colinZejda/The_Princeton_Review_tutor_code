# now, use a dictionary for prices
service_prices = {'Oil change' : 35, 
                  'Tire rotation' : 19,
                  'Car wash' : 7,
                  'Car wax' : 12}

# initial prints
print('Davy\'s auto shop services')
for service, price in service_prices.items():
    print(f"{service} -- ${price}")
print()     # extra newline

# get inputs
serviceSelection1 = input('Select first service: ')
serviceSelection2 = input('Select second service: ')

# function to help with invoices (the trick)
def display_service(one_or_two, service):
    if service in service_prices:
        print(f'Service {one_or_two}: {service}, ${service_prices[service]}')
        return service_prices[service]
    elif service == '-':
        print(f'Service {one_or_two}: No service')
    else:
        print("Invalid service")    # added this, error checking

# print invoices
costService1 = display_service(1, serviceSelection1)
costService2 = display_service(2, serviceSelection2)

# compute total, display it
Total = costService1 + costService2
print(f'\nTotal: ${Total}')