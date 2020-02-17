num = int(input("Give me a number: "))
mod = num%2

if(mod==0):

    if(num%4==0):
        print("Liczba jest wielokrotnością liczby 4!")
    else:
        print("Liczba jest pażysta.")
else:
    print("Liczba jest nie pażysta.")

check = int(input("Number for divide first num: "))

if(num%check!=0):
    print("Liczba nie dzieli się na równe części")
else:
    print("Liczba dzieli się na równe części")




# parzysta
# niepażysta
# wielokrotność 4
#