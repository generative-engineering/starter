from pathlib import Path

from generative.fabric import fabric_function, FileAsset, Asset

import json


def dummy_convert(src: Path) -> Asset:
    """Effectively a no-op, for demonstration purposes only"""

    report = {
        "geometry": "cuboid",
        "src": str(src),
    }
    asset = FileAsset(extension="json")
    with asset.open("w") as f:
        json.dump(report, f)

    return asset


@fabric_function
def step_renderer(step_asset: Asset) -> Asset:
    """Use this function to, for example, convert STEP files to another format"""

    step_file = step_asset.download(extension="step")

    # Instead of reading a STEP file, we are reading a dummy json, so perform a dummy conversion
    return dummy_convert(step_file)
