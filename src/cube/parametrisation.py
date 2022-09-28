from generative.fabric import FabricFunction, FabricType, Field

from cube.analysis import Cuboid


class CubeDimensions(FabricType):
    specified_width: float = Field(gt=0)


class PrismDimensions(FabricType):
    specified_width: float = Field(gt=0)
    specified_length: float = Field(gt=0)


class CubeGenerator(FabricFunction[CubeDimensions, Cuboid]):
    def run(self, inputs: CubeDimensions) -> Cuboid:
        return Cuboid(
            width=inputs.specified_width,
            height=inputs.specified_width,
            length=inputs.specified_width,
        )


class RectangleOutputs(FabricType):
    cuboid: Cuboid


class RectangularPrismGenerator(FabricFunction[PrismDimensions, Cuboid]):
    def run(self, inputs: PrismDimensions) -> Cuboid:
        return Cuboid(
            width=inputs.specified_width,
            height=inputs.specified_width,
            length=inputs.specified_length,
        )
