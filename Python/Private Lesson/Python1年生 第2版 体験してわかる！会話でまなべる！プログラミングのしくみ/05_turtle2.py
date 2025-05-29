# タートルグラフィックス
# まっすぐ進んで、「左に90度曲がる」という行動を4回くり返して、正方形を描くプログラム
from turtle import *
shape("turtle")
for i in range(4):
    forward(100)
    left(90)
done()