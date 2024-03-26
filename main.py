import turtle
import random
import time

# Pencere oluşturma
wn = turtle.Screen()
wn.title("Kaplumbağa Oyunu")
wn.bgcolor("lightgreen")
wn.setup(width=600, height=600)

# Skor
score = 0

# Skor yazısı
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Skor: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Geri sayım
countdown = 10

# Geri sayım yazısı
countdown_pen = turtle.Turtle()
countdown_pen.speed(0)
countdown_pen.color("white")
countdown_pen.penup()
countdown_pen.hideturtle()
countdown_pen.goto(0, 220)

# Kaplumbağa
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(0)
t.penup()

# Kaplumbağa hareket fonksiyonu
def move_turtle():
    t.goto(random.randint(-290, 290), random.randint(-290, 290))

def increase_score(x, y):
    global score
    score += 1
    score_pen.clear()
    score_pen.write("Skor: {}".format(score), align="center", font=("Courier", 24, "normal"))
    move_turtle()

t.onclick(increase_score)

# Geri sayım fonksiyonu
def countdown_timer():
    global countdown
    if countdown > 0:
        countdown -= 1
        countdown_pen.clear()
        countdown_pen.write("Geri sayım: {}".format(countdown), align="center", font=("Courier", 24, "normal"))
        wn.ontimer(countdown_timer, 1000)
    else:
        countdown_pen.clear()
        countdown_pen.goto(0, 0)
        countdown_pen.write("Oyun bitti!", align="center", font=("Courier", 36, "normal"))
        time.sleep(2)
        wn.bye()  # Ekranı kapat

# Geri sayımı başlat
countdown_timer()

# İlk kaplumbağanın yerleştirilmesi
move_turtle()

# Ana döngü
while True:
    wn.update()  # Pencereyi güncelle

# Main loop'u çalıştır
turtle.mainloop()
