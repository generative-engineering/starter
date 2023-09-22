from generative.fabric import fabric_function, FabricType, FileAsset, Asset
from pydantic import Field

import json
from cube.utils import timestamped_file_path


class Cuboid(FabricType):
    length: float = Field(gt=0)
    width: float = Field(gt=0)
    height: float = Field(gt=0)


@fabric_function
def generate_cuboid_cad(cuboid: Cuboid) -> Asset:
    file_path = timestamped_file_path("json")
    with open(file_path, "w") as outfile:
        json.dump(cuboid.as_json(), outfile)
    return FileAsset(file_path)
