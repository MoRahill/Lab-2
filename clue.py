import termcolor
from logic import *

alice = Symbol("AliceSuspect")
bob = Symbol("BobSuspect")
carol = Symbol("CarolSuspect")
characters = [alice, bob, carol]

office = Symbol("office")
garage = Symbol("garage")
basement = Symbol("basement")
rooms = [office, garage, basement]

poison = Symbol("poison")
rope = Symbol("rope")
candlestick = Symbol("candlestick")
weapons = [poison, rope, candlestick]

symbols = characters + rooms + weapons

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


knowledge = And(
    Or(alice, bob, carol),
    Or(office, garage, basement),
    Or(poison, rope, candlestick)
)

knowledge.add(And(
    Not(alice), Not(office), Not(poison)
))

knowledge.add(Or(
    Not(bob), Not(garage), Not(rope)
))

knowledge.add(Not(candlestick))
knowledge.add(Not(basement))

check_knowledge(knowledge)
