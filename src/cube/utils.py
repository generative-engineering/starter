###################################################################################################
# Some re-usable python functions to help manage storing data on your local filesystem.
###################################################################################################

from datetime import datetime
from pathlib import Path


def timestamped_file_path(
    fname: str,
    extension: str,
    sub_dir_name: str,
    output_dir_name: str = "output",
) -> Path:
    """Returns the timestamped path to file in sub directory inside output directory"""
    render_dir = guaranteed_dir(Path(output_dir_name) / sub_dir_name)
    return render_dir / f"{timestamp(fname)}.{extension}"


def guaranteed_dir(p: Path) -> Path:
    """Creates or recreates an empty directory"""
    dir_ = p.absolute()
    if not dir_.is_dir():
        if dir_.exists():
            dir_.unlink()
        dir_.mkdir(parents=True)
    return dir_


def timestamp(a_string: str) -> str:
    """
    Add a filepath-friendly timestamp to the end of a string.
    Useful to help distinguish files generated inside explorations in a human-readable way.
    """

    return datetime.utcnow().strftime(f"{a_string}_%Y%m%d%H%M%S%f")
