from pathlib import Path

from generative.fabric import TestingAsset

from tests.assets import download_asset
from cube.renderer import (
    step_renderer,
)


def test_cuboid_renderer(step_file: Path):
    outputs = step_renderer(TestingAsset(step_file))
    assert download_asset(outputs).exists()
