from typing import Any, Dict, Tuple
from generative.fabric import fabric_function, FabricType, FileAsset

from pydantic import Field
import cadquery as cq
from cube.utils import timestamped_file_path


class SvgExportOptions(FabricType):
    width: float = Field(default=800)
    height: float = Field(default=240)
    margin_left: float = Field(default=200)
    margin_top: float = Field(default=20)
    projection_dir: Tuple[float, float, float] = Field(default=(-1.75, 1.1, 5))
    show_axes: bool = Field(default=True)
    stroke_width: float = Field(default=-1.0, description="-1 = calculated based on unitScale")
    stroke_color: Tuple[float, float, float] = Field(default=(0, 0, 0), description="RGB 0-255")
    hidden_color: Tuple[float, float, float] = Field(
        default=(160, 160, 160), description="RGB 0-255"
    )
    show_hidden: bool = Field(default=True)
    focus: bool = Field(default=None)

    def camel_case_dict(self) -> Dict[str, Any]:
        def snake_to_camel_case(s: str) -> str:
            return "".join(w.capitalize() for w in s.split("_"))

        data = self.model_dump()
        return {snake_to_camel_case(key): value for key, value in data.items()}


class CommonExporterInputs(FabricType):
    cad_query_workplane: cq.Workplane
    file_name: str
    output_directory_name: str = Field(default="output")
    output_subdirectory_name: str


class RenderInputs(FabricType):
    common: CommonExporterInputs
    render_options: SvgExportOptions = Field(default=SvgExportOptions())


@fabric_function
def cad_query_renderer(inputs: RenderInputs) -> FileAsset:
    image_path = timestamped_file_path(
        inputs.common.file_name,
        "svg",
        inputs.common.output_subdirectory_name,
        inputs.common.output_directory_name,
    )
    cq.exporters.export(
        inputs.common.cad_query_workplane,
        str(image_path),
        opt=inputs.render_options.camel_case_dict(),
    )

    return FileAsset(image_path)


@fabric_function
def cad_query_step_exporter(inputs: CommonExporterInputs) -> FileAsset:
    step_path = timestamped_file_path(
        inputs.file_name, "step", inputs.output_subdirectory_name, inputs.output_directory_name
    )
    cq.exporters.export(inputs.cad_query_workplane, str(step_path))
    return FileAsset(step_path)
