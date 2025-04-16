to_do = True
while to_do == True:
    stock = 25
    shoe_price = 500
    ops = input('hello welcome to abc stores. what do you wanna do? \nclick "1" to buy shoe? \nclick "2" to return shoe?\n')
    if ops == '1':
        print('shoe price is $', shoe_price)
        print('we have', stock, 'shoes in stock')
        num_shoe = int(input('how many shoes do you want to buy?\n'))
        amount = num_shoe * shoe_price
        print('you will pay $', amount)
        print('we now have', stock - num_shoe, 'shoes left')
        done = input('Do you wanna perform another transaction? \nclick "1" for yes \nclick "2" for no \n')
        if done == '1':
              to_do == True
        else:
            to_do == False
            print('Thanks for using our service. have a nice day')
            break
    elif ops == '2':
        ret_shoe = int(input('how many shoes will you like to return?\n'))
        amount = ret_shoe * shoe_price
        print('your refund amount is $', amount)
        print('we now have', stock + ret_shoe, 'shoes left')
        done = input('Do you wanna perform another transaction? \nclick "1" for yes \nclick "2" for no \n')
        if done == '1':
              to_do == True
        else:
            to_do == False
            print ('thanks for using our service, have a nice day')
            break
              
          
