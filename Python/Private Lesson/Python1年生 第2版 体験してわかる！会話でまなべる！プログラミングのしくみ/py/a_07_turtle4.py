# タートルグラフィックス
# くり返す中身を、「半径100の円を描いて、左に72度曲がる」という行動を5回くり返して、花を描くプログラム
from turtle import *
shape("turtle")
col = ["orange","limegreen","gold","plum","tomato"]
for i in range(5):
    color(col[i])
    circle(100)
    left(72)
done()