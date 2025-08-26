# タートルグラフィックス
# まっすぐ進んで、「左に144度曲がる」という行動を5回くり返して、星を描くプログラム
from turtle import *

shape("turtle")
col = ["orange", "limegreen", "gold", "plum", "tomato"]
for i in range(5):
    color(col[i])
    forward(200)
    left(144)
done()
