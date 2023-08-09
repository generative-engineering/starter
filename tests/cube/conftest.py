from pytest import fixture
import cadquery as cq

from cube.geometry import Cuboid


@fixture
def a_cad_query_cuboid() -> cq.Workplane:
    return cq.Workplane("XY").box(length=2, width=3, height=5)


@fixture
def a_cuboid() -> Cuboid:
    return Cuboid(length=2, width=3, height=5)
