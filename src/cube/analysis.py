from typing import Text

from generative.engine.fabric.function import FabricFunction
from generative.engine.fabric.type import FabricType, Field


class Cuboid(FabricType):
    length: float = Field(gt=0)
    width: float = Field(gt=0)
    height: float = Field(gt=0)


class GeometryVolume(FabricType):
    volume: float = Field(gt=0)
    surface_area: float = Field(gt=0)
    cuboid: Cuboid


class VolumeInput(FabricType):
    name: Text
    cuboid: Cuboid


class VolumeAnalysis(FabricFunction):

    def run(self, inputs: VolumeInput) -> GeometryVolume:
        return GeometryVolume(
            cuboid=inputs.cuboid,
            volume=inputs.cuboid.width * inputs.cuboid.height * inputs.cuboid.length,
            surface_area=(
                (2 *inputs.cuboid.width * inputs.cuboid.height) +
                (2 *inputs.cuboid.height * inputs.cuboid.length) +
                (2 *inputs.cuboid.width * inputs.cuboid.length)
            )
        )
