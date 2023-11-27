from pathlib import Path

from generative.fabric import FileAsset

from cube.renderer import step_renderer


def test_cuboid_renderer(step_file: Path):
    in_asset = FileAsset(step_file)
    out_asset = step_renderer(in_asset)
    assert (out_asset.download()).exists()
