import datetime
import os
from pathlib import Path
from typing import Text

from generative.engine.fabric.function import FabricFunction
from generative.engine.fabric.type import FabricType, Field

from cube.analysis import Cuboid


class CuboidRender(FabricType):
    image_file: Text = Field(
        description="Text representation of the file path that the image has been written to"
    )


class CubeRenderInputs(FabricType):
    cuboid: Cuboid
    render_name: Text
    output_directory_name: Text = Field(default="output")
    render_directory_name: Text = Field(default="renders")


class CuboidRenderer(FabricFunction):
    def run(self, inputs: CubeRenderInputs) -> CuboidRender:

        image_file = _resolve_output_path(inputs.render_name, "txt")
        with open(image_file, "w") as f:
            f.write("Replace me with an image!")

        return CuboidRender(image_file=str(image_file))


###################################################################################################
# Some re-usable python functions to help manage storing data on your local filesystem.
###################################################################################################


def _resolve_output_path(
    name: Text,
    extension: Text,
    output_directory: Text = "output",
    render_directory: Text = "renders",
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


def timestamp(a_string: Text) -> Text:
    """
    Add a filepath-friendly timestamp to the end of a string.
    Useful to help distinguish files generated inside explorations in a human-readable way.
    """

    return (
        a_string
        + "_"
        + str(datetime.datetime.now())
        .replace(" ", "")
        .replace(".", "")
        .replace(":", "")
        .replace("-", "")[0:-2]
    )
