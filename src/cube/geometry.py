from generative.fabric import FabricFunction, FabricType, FileAsset
from generative.geometry import (
    Angle,
    Body3d,
    Interval,
    Length,
    LineSegment2d,
    Point2d,
    Region2d,
    SketchPlane3d,
)

from cube.analysis import Cuboid
from cube.utils import get_render_path


class GeometryOutput(FabricType):
    stl_asset: FileAsset


class CubeCADGenerator(FabricFunction[Cuboid, GeometryOutput]):
    def run(self, inputs: Cuboid) -> GeometryOutput:
        x0 = Length.ZERO
        x1 = Length.meters(inputs.length)
        y0 = Length.ZERO
        y1 = Length.meters(inputs.width)

        p0 = Point2d.xy(x0, y0)
        p1 = Point2d.xy(x0, y1)
        p2 = Point2d.xy(x1, y1)
        p3 = Point2d.xy(x1, y0)

        square = Region2d.bounded_by(
            [
                LineSegment2d.with_endpoints(p0, p1),
                LineSegment2d.with_endpoints(p1, p2),
                LineSegment2d.with_endpoints(p2, p3),
                LineSegment2d.with_endpoints(p3, p0),
            ]
        )

        sketch_plane = SketchPlane3d.XY
        extent = Interval.with_endpoints(Length.ZERO, Length.meters(inputs.height))

        body = Body3d.extrude(square, sketch_plane, extent)

        stl_path = get_render_path("cube", "stl", "output", "geometry")

        body.save_stl(Length.millimeters(0.5), Angle.degrees(5.0), str(stl_path))

        return GeometryOutput(stl_asset=FileAsset(stl_path))
