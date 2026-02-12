import turtle
import random

prozor = turtle.Screen()                                   # 1. Postavka ekrana
prozor.title("Velika trka: Marko vs Lena")
prozor.bgcolor("white")

marko = turtle.Turtle()                             # 2. Kreiranje objekta "Marko" (Instanciranje klase Turtle)
marko.color("blue")
marko.shape("turtle")
marko.penup() 
marko.goto(-200, 20) # Početna pozicija za Marka

lena = turtle.Turtle()                                    # 3. Kreiranje objekta "Lena" (Druga instanca iste klase)
lena.color("red")
lena.shape("turtle")
lena.penup()
lena.goto(-200, -20) # Početna pozicija za Lenu

marko.pendown() 
lena.pendown() 
while marko.xcor() < 200 and lena.xcor() < 200:        # 4. Logika trke (Korišćenje metoda objekata)
    marko.forward(random.randint(1, 10))
    lena.forward(random.randint(1, 10))

if marko.xcor() > lena.xcor():                                    # 5. Proglašenje pobednika
    print("Pobedio je Marko!")
    marko.write("  POBEDIO SAM!", font=("Arial", 16, "bold"))
else:
    print("Pobedila je Lena!")
    lena.write("  POBEDILA SAM!", font=("Arial", 16, "bold"))

prozor.exitonclick()
