from generative.fabric import FabricFunction, FabricType, FileAsset

from cube.analysis import Cuboid
from pydantic import Field

from cube.utils import get_render_path


class CuboidRender(FabricType):
    image_file: FileAsset
    """The rendered image """


class CuboidRenderInputs(FabricType):
    cuboid: Cuboid
    render_name: str
    output_directory_name: str = Field(default="output")
    render_directory_name: str = Field(default="renders")


class CuboidRenderer(FabricFunction[CuboidRenderInputs, CuboidRender]):
    def run(self, inputs: CuboidRenderInputs) -> CuboidRender:
        image_file = get_render_path(inputs.render_name, "txt")
        with open(image_file, "w") as f:
            f.write("Replace me with an image!")

        return CuboidRender(image_file=FileAsset(image_file))
