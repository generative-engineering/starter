from cube.geometry import cuboid_cad_generator, Cuboid


def test_cube_generator(a_cuboid: Cuboid) -> None:
    output = cuboid_cad_generator(a_cuboid)
    assert output
