from generative.fabric import fabric_function, FabricType

from cube.geometry import Cuboid
from pydantic import Field


class PrismDimensions(FabricType):
    specified_width: float = Field(gt=0)
    specified_length: float = Field(gt=0)


@fabric_function
def cube_generator(side_length: float) -> Cuboid:
    return Cuboid(
        width=side_length,
        height=side_length,
        length=side_length,
    )


class RectangleOutputs(FabricType):
    cuboid: Cuboid


def rectangular_prism_generator(inputs: PrismDimensions) -> Cuboid:
    return Cuboid(
        width=inputs.specified_width,
        height=inputs.specified_width,
        length=inputs.specified_length,
    )
