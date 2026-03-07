try:     # Blok koji je samo pokušaj za slučaj da dođe do greške
    dividend = int(input("Enter the dividend: "))
    divisor  = int(input("Enter the divisor: "))
    result = dividend/divisor
except ZeroDivisionError: # Šta se radi ako dođe do izuzetka ZeroDivisionError
    print("You can't divide by 0!")
except ValueError:
    print("Enter only a number")
else:     # Ako je deljenje uspešno
    print(result)
