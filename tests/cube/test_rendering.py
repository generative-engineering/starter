from pathlib import Path
from time import time, sleep
from pytest import fixture

from cube.geometry import CubeCADGenerator
from cube.analysis import Cuboid
from cube.rendering import CuboidRenderer, CuboidRenderInputs


@fixture
def a_cuboid() -> Cuboid:
    return Cuboid(length=2, width=3, height=5)


def test_cube_rendering(a_cuboid: Cuboid) -> None:
    then = time()
    sleep(0.1)  # disk caches are weird
    ff = CubeCADGenerator()

    output = ff.run(a_cuboid)
    stl = Path(output.stl_asset)
    assert stl.exists()
    assert stl.stat().st_mtime > then, "Didn't produce a new file?"


def test_cuboid_renderer(a_cuboid: Cuboid):
    ff = CuboidRenderer()
    inputs = CuboidRenderInputs(cuboid=a_cuboid, render_name="render")
    outputs = ff.run(inputs)
    assert outputs.image_file.exists()
