import random

# Non borres este ficheiro, deixao como plantilla. Copia e pega para facer as túas vainas.
def add_randint(max_delta_val: int) -> None:
    # A parte de -> None sirve para indicar que a función non devolve nada. Ou máis ben 🤓 devolve nulo ou None.
    # Este print de inicio e o outro do final imos cambialos máis adiante por unha cousa chula pero de momento quedan así
    print(f"Now entering function named: {add_randint.__name__} with max increment of {max_delta_val}.")

    curr_val = 0
    for i in range(3):
        curr_val = curr_val + random.randint(0, max_delta_val)
        print(f"\tCurrent value is {curr_val}")

    print(f"Function named: {add_randint.__name__} completed!")
    return
