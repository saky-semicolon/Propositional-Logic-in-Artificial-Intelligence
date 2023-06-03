from logic import *

play = Symbol("Piano")  #I play piano.
study = Symbol("Logic") #I study logic.

sentence = And(play, study)

print(sentence.formula())