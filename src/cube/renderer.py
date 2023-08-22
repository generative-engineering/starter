from generative.fabric import fabric_function, FileAsset, Asset

import cadquery as cq
from cube.utils import timestamped_file_path


@fabric_function
def step_renderer(step_asset: Asset) -> Asset:
    step_file = step_asset.download(extension="step")
    body = cq.importers.importStep(str(step_file))  # type: ignore
    image_path = timestamped_file_path(
        "svg",
    )
    cq.exporters.export(body, str(image_path))

    return FileAsset(image_path)
