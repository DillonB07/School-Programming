import os

with open('pms.txt', 'w') as f:
    data = """
Previous 5 Prime Ministers as of 12/10/22

Liz Truss 2022 -
Boris Johnson 2019 - 2022
Theresa May 2016 - 2019
David Cameron 2010 - 2016
Gordon Brown 2007 - 2010
"""
    f.write(data)

with open('pms.txt', 'r') as f:
    for line in f:
        print(line)

