###################################################################################################
# Some re-usable python functions to help manage storing data on your local filesystem.
###################################################################################################

from datetime import datetime
from pathlib import Path


def get_render_path(
    name: str,
    extension: str,
    output_directory: str = "output",
    render_directory: str = "renders",
) -> Path:
    """Returns the renders directory"""
    render_dir = init_dir(Path(output_directory).absolute() / render_directory)
    return render_dir / f"{timestamp(name)}.{extension}"


def init_dir(p: Path) -> Path:
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
