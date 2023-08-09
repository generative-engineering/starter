from cube.parametrisation import rectangular_prism_generator, cube_generator, PrismDimensions
from cube.geometry import Cuboid


def test_prism_parametrisation() -> None:
    inputs = PrismDimensions(specified_width=5, specified_length=7)
    output = rectangular_prism_generator(inputs)
    assert output.width == 5
    assert output.length == 7


def test_cube_parametrisation() -> None:
    assert cube_generator(side_length=5) == Cuboid(width=5, height=5, length=5)
