from pytest import fixture

from cube.geometry import Cuboid
from pathlib import Path


CUBE_TESTS_DIR = Path(__file__).parent


@fixture
def step_file() -> Path:
    return CUBE_TESTS_DIR / "data" / "cube.step"


@fixture
def a_cuboid() -> Cuboid:
    return Cuboid(length=2, width=3, height=5)
