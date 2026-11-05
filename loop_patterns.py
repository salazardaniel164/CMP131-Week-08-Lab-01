# Daniel E Salazar Gomez
# CMP-131-86520
# Week 8
# Lab 01
# Assignment 8
# 11/5/2026
print("Increasing and Decreasing Patterns")
print()
print("Pattern A")
for row in range(1, 11):
    for column in range(row):
        print("+", end="")
    print()
print()
print("Pattern B")
for row in range(10, 0, -1):
    for column in range(row):
        print("+", end="")
    print()