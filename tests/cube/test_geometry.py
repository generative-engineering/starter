from time import sleep, time
from cube.geometry import generate_cuboid_cad, Cuboid
from generative.fabric import TestingAsset


def test_cube_generator(a_cuboid: Cuboid) -> None:
    then = time()
    sleep(0.1)  # disk caches are weird
    step_asset = TestingAsset.from_asset(generate_cuboid_cad(a_cuboid))
    step_file = step_asset.download()
    assert step_file.exists()
    assert step_file.stat().st_mtime > then, "Didn't produce a new file?"
