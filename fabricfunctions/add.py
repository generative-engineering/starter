from generative.fabric import fabric_function


@fabric_function
def add(a: float, b: float) -> float:
    return a + b
