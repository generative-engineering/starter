from time import sleep, time
from cube.geometry import FileNameAndLocation, cuboid_cad_generator, Cuboid


def test_cube_generator(a_cuboid: Cuboid) -> None:
    then = time()
    sleep(0.1)  # disk caches are weird
    step_output = FileNameAndLocation(name="test_cube", directory="output", subdirectory="step")
    step = cuboid_cad_generator(a_cuboid, step_output)
    assert step.exists()
    assert step.stat().st_mtime > then, "Didn't produce a new file?"
