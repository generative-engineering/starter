from pathlib import Path

from generative.fabric import fabric_function, FileAsset, Asset

from cube.utils import timestamped_file_path
import json


def dummy_convert(src: Path) -> Path:
    """Effectively a no-op, for demonstration purposes only"""

    report = {
        "geometry": "cuboid",
        "src": str(src),
    }

    dst_file = timestamped_file_path("json")
    with open(dst_file, "w") as outfile:
        json.dump(report, outfile)

    return dst_file


@fabric_function
async def step_renderer(step_asset: Asset) -> Asset:
    """Use this function to, for example, convert STEP files to another format"""

    step_file = await step_asset.download(extension="step")

    # Instead of reading a STEP file, we are reading a dummy json, so perform a dummy conversion
    dst_file = dummy_convert(step_file)

    return FileAsset(dst_file)
