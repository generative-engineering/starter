from generative.fabric import fabric_function, FabricType
from pydantic import Field

import cadquery as cq


class Cuboid(FabricType):
    length: float = Field(gt=0)
    width: float = Field(gt=0)
    height: float = Field(gt=0)


@fabric_function
def cuboid_cad_generator(inputs: Cuboid) -> cq.Workplane:
    return cq.Workplane("XY").box(inputs.length, inputs.width, inputs.height)
