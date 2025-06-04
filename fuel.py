#creating a fuel gauge program to indicate the percentage of the fuel left 
# ask the user for 2 integers x ANd y 
# calculate x/y and percetnage and output to the user 

def main():
    print("instructions : add values that are only positive ")
    print("x should always be less than zero ")
    while True :
        try:
            x = int(input("whats x ? "))
            y = int(input("whats y ? "))
            if x>y or x<0 or y<0 :
                continue
            try :
                 z = x/y 
                 k = z * 100
                 if k == 100 :
                     print("F")
                 elif k== 0 :
                     print("E")
                 else :
                     print(k)  
                 break  
            except ZeroDivisionError :
                print("division by zero is not defined ")
        except ValueError :
            print("pls enter positve integers")                         
main()