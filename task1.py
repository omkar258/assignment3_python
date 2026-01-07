def fact():
    
    facto = 1;
    num = int(input("Enter a number: "))
    for i in range (1 , num +1):
        facto = facto *i  
    print(f"Factorial of {num} is {facto}.")
    return facto;

fact()
