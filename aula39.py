# Yield

def fazer_pizzas():
    yield "calabresa"
    yield "presunto"
    yield "frango"

for pizza in fazer_pizzas():
    print(f"sabor da pizza: {pizza}")