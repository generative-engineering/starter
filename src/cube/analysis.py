from generative.fabric import fabric_function, FabricType
from pydantic import Field
from cube.geometry import Cuboid


class GeometricProperties(FabricType):
    volume: float = Field(gt=0)
    surface_area: float = Field(gt=0)


@fabric_function
def geometric_property_analysis(inputs: Cuboid) -> GeometricProperties:
    volume = inputs.width * inputs.height * inputs.length
    surface_area = (
        (2 * inputs.width * inputs.height)
        + (2 * inputs.height * inputs.length)
        + (2 * inputs.width * inputs.length)
    )

    return GeometricProperties(
        volume=volume,
        surface_area=surface_area,
    )
