from cube.analysis import geometric_property_analysis
from cube.geometry import Cuboid

# TODO: actual tests here (more than just importing)


def test_volume_analysis(a_cuboid: Cuboid) -> None:
    assert geometric_property_analysis(a_cuboid)
