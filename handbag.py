from logic import *

style = Symbol("stylish")
color = Symbol("colorful")

sentence = And(style, color)

print(sentence.formula())

