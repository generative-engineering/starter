from pathlib import Path

from generative.fabric import FileAsset
from cube.geometry import FileNameAndLocation
from cube.renderer import (
    step_renderer,
)


def test_cuboid_renderer(step_file: Path):
    FileNameAndLocation(
        name="test_cube_render",
        relative_directory="output/render",
    )

    outputs = step_renderer(FileAsset(step_file))
    assert outputs.download().exists()
