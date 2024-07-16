from turtle import*
bgcolor("black")
a=180
#first make a ret
begin_fill()
fillcolor("white")
fd(200)
rt(90)
fd(a)
rt(90)
fd(200)
rt(90)
fd(a)
end_fill()
#now time to make this logo
up()
goto(65,-50)
down()
begin_fill()
fillcolor("red")
rt(90)
fd(70)
for x in range(9):
	rt(10)
	fd(5)
fd(30)
for y in range (9):
	rt(10)
	fd(5)
fd(70)
for y in range (9):
	rt(10)
	fd(5)
fd(30)
for y in range (9):
	rt(10)
	fd(5)
fd(20)
end_fill()


up()
rt(90)
fd(15)
down()
begin_fill()
fillcolor("white")
fd(50)


lt(120)
fd(50)

lt(120)
fd(50)
end_fill()
done()

