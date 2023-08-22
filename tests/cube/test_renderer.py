from pathlib import Path

from generative.fabric import TestingAsset
from cube.renderer import (
    step_renderer,
)


def test_cuboid_renderer(step_file: Path):
    outputs = step_renderer(TestingAsset(step_file))
    assert TestingAsset.from_asset(outputs).download().exists()
