from typing import Text

from generative.engine.fabric.function import FabricFunction
from generative.engine.fabric.type import FabricType

from cube.analysis import Cuboid


class GeometryOutput(FabricType):
    stl_file: Text


class CubeCADGenerator(FabricFunction):
    def run(self, inputs: Cuboid) -> GeometryOutput:

        # TODO: Add example use of generative python geometry wrappers

        return GeometryOutput(stl_file="todo")
