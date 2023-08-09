from cube.parametrisation import RectangularPrismGenerator, CubeGenerator, PrismDimensions


def test_prism_parametrisation() -> None:
    spec = PrismDimensions(specified_width=5, specified_length=7)
    output = RectangularPrismGenerator().run(spec)
    assert output.width == 5
    assert output.length == 7


def test_cube_parametrisation() -> None:
    assert CubeGenerator()
