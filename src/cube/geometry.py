from generative.fabric import fabric_function, FabricType, FileAsset
from pydantic import Field

import cadquery as cq

from cube.utils import timestamped_file_path


class Cuboid(FabricType):
    length: float = Field(gt=0)
    width: float = Field(gt=0)
    height: float = Field(gt=0)


class FileNameAndLocation(FabricType):
    name: str
    relative_directory: str = "output"


@fabric_function
def generate_cuboid_cad(cuboid: Cuboid, output_file: FileNameAndLocation) -> FileAsset:
    body = cq.Workplane("XY").box(cuboid.length, cuboid.width, cuboid.height)
    step_path = timestamped_file_path(output_file.name, "step", output_file.relative_directory)
    cq.exporters.export(body, str(step_path))
    return FileAsset(step_path)
