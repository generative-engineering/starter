from pathlib import Path

from generative.fabric import FileAsset
from cube.geometry import FileNameAndLocation
from cube.renderer import (
    step_renderer,
)


def test_cuboid_renderer(step_file: Path):
    output_file = FileNameAndLocation(
        name="test_cube_render",
        relative_directory="output/render",
    )

    outputs = step_renderer(FileAsset(step_file), output_file)
    assert outputs.exists()
