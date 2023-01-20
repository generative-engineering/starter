from typing import Text

from generative.fabric import FabricFunction, FabricType, field


class Cuboid(FabricType):
    length: float = field(lower=0)
    width: float = field(lower=0)
    height: float = field(lower=0)


class GeometryVolume(FabricType):
    volume: float = field(lower=0)
    surface_area: float = field(lower=0)
    cuboid: Cuboid


class VolumeInput(FabricType):
    name: Text
    cuboid: Cuboid


class VolumeAnalysis(FabricFunction[VolumeInput, GeometryVolume]):
    def run(self, inputs: VolumeInput) -> GeometryVolume:
        return GeometryVolume(
            cuboid=inputs.cuboid,
            volume=inputs.cuboid.width * inputs.cuboid.height * inputs.cuboid.length,
            surface_area=(
                (2 * inputs.cuboid.width * inputs.cuboid.height)
                + (2 * inputs.cuboid.height * inputs.cuboid.length)
                + (2 * inputs.cuboid.width * inputs.cuboid.length)
            ),
        )
