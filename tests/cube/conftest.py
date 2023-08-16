from pytest import fixture

from cube.geometry import Cuboid, FileNameAndLocation
from pathlib import Path


CUBE_TESTS_DIR = Path(__file__).parent


@fixture
def step_file() -> Path:
    return CUBE_TESTS_DIR / "data" / "cube.step"


@fixture
def a_cuboid() -> Cuboid:
    return Cuboid(length=2, width=3, height=5)


@fixture
def step_output_file_location() -> FileNameAndLocation:
    return FileNameAndLocation(name="test_step", relative_directory="output/step")


@fixture
def render_output_file_location() -> FileNameAndLocation:
    return FileNameAndLocation(name="test_render", relative_directory="output/render")
