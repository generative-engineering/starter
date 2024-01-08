from generative.fabric import fabric_function, FabricType, FileAsset, Asset
from pydantic import Field

import json


class Cuboid(FabricType):
    length: float = Field(gt=0)
    width: float = Field(gt=0)
    height: float = Field(gt=0)


@fabric_function
def generate_cuboid_cad(cuboid: Cuboid) -> Asset:
    asset = FileAsset(extension="json")
    with asset.open("w") as outfile:
        json.dump(cuboid.as_json(), outfile)
    return asset
