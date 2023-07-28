import os
from datetime import datetime
from pathlib import Path

from generative.fabric import FabricFunction, FabricType, field

from cube.analysis import Cuboid


class CuboidRender(FabricType):
    image_file: str
    """Text representation of the file path that the image has been written to"""


class CubeRenderInputs(FabricType):
    cuboid: Cuboid
    render_name: str
    output_directory_name: str = field(default="output")
    render_directory_name: str = field(default="renders")


class CuboidRenderer(FabricFunction[CubeRenderInputs, CuboidRender]):
    def run(self, inputs: CubeRenderInputs) -> CuboidRender:
        image_file = _resolve_output_path(inputs.render_name, "txt")
        with open(image_file, "w") as f:
            f.write("Replace me with an image!")

        return CuboidRender(image_file=str(image_file))


###################################################################################################
# Some re-usable python functions to help manage storing data on your local filesystem.
###################################################################################################


def _resolve_output_path(
    name: str,
    extension: str,
    output_directory: str = "output",
    render_directory: str = "renders",
) -> Path:
    if not os.path.isdir(output_directory):
        if os.path.exists(output_directory):
            os.remove(output_directory)
        os.mkdir(output_directory)

    render_dir = os.path.join(output_directory, render_directory)
    if not os.path.isdir(render_dir):
        if os.path.exists(render_dir):
            os.remove(render_dir)
        os.mkdir(render_dir)

    return Path(os.path.abspath(os.path.join(render_dir, f"{timestamp(name)}.{extension}")))


def timestamp(a_string: str) -> str:
    """
    Add a filepath-friendly timestamp to the end of a string.
    Useful to help distinguish files generated inside explorations in a human-readable way.
    """

    return datetime.utcnow().strftime(f"{a_string}_%Y%m%d%H%M%S%f")
