#PizzaApp.py
#Programmer: Vijay Prasad

def welcome():
    print('Welcome to Vijay Pizza\n~~~~~~~~~~~~~~~~~~~~~~\n\n')

def displayPizzas(pizzas):
    if pizzas.len() == 0:
        print('No pizzas as of yet. ')
    
    #list pizzas
    else:
        index = 1
        for pizza in pizzas:
            #using join to combined , and space with toppings list separated by ,
            print(f"{index}: {pizza[0]}, pizza with {', '.join(pizza[1])}.") 
            index += 1
def userChoice():
    choice = input('(A)dd a pizza \n(R)emove a pizza \n(S)ave pizza order \n (O)pen pizza order \n(E)xit')[0].upper()
    return choice

def addPizza():
    size = input('Please enter the pizz size (S, M, L): ')[0].upper()
    print('Toppings')
    toppings = []
    while True:
        topping = input('Please enter your toppings or enter to stop: ')
        if topping =='': break
        toppings.append(topping)
    
    pizza = (size, toppings) #creating a pizza tuple to include the size and toppings list
    pizzas.append(pizza) # adding the pizza tuple to the pizzas list
    
    #no need to return here since the data structures are automatically updated inside the function.

def removePizza(pizzas):       
    #get pizza to remove from the user
    removeIndex = int(input('Please enter the number of the pizza to remove: '))
    if(removeIndex > 0 and removeIndex <= pizzas.len()):
        del pizzas[removeIndex-1]
    else:
        print('Invalid Pizza number entered. ')
    
def bye():
    print('Thank you for visiting Vijay Pizza')
    
if __name__ =="__main__":
    #display welcome
    welcome()
    
    #create a list to hold pizzas
    pizzas = []
    
    while True:
        #display pizzas
        displayPizzas(pizzas)       
        # get user's choice
        choice = userChoice()
        # (A)dd a pizza
        if choice == 'A':
            addPizza(pizzas)
        # (R)emove a pizza
        elif choice == 'R':
            removePizza(pizzas)
        # (S)ave pizza order
        # (O)pen pizza order
        # (E)xit
        if choice == 'E': break

    #dislay thanks
    bye()