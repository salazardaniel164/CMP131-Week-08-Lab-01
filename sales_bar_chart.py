# Daniel E Salazar Gomez
# CMP-131-86520
# Week 8
# Lab 01
# Assignment 8
# 11/5/2026
Ast=""
store= int(input("Enter number of stores "))
for i in range (store):
    sale=int(input("Enter today's sales for store " + str(i+1)+":"))
    Ast = Ast + "Store " + str(i+1) + ":"
    sale=sale/100
    for j in range(int(sale)):
        Ast=Ast + "*"
    Ast=Ast+"\n" 
print(Ast)