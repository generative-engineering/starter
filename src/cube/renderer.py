from generative.fabric import fabric_function, FileAsset

import cadquery as cq
from cube.geometry import FileNameAndLocation
from cube.utils import timestamped_file_path


@fabric_function
def step_renderer(step_file: FileAsset, output_file: FileNameAndLocation) -> FileAsset:
    body = cq.importers.importStep(str(step_file))  # type: ignore
    image_path = timestamped_file_path(
        output_file.name,
        "svg",
        output_file.subdirectory,
        output_file.directory,
    )
    cq.exporters.export(body, str(image_path))

    return FileAsset(image_path)
