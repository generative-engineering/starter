""" Some re-usable python functions to help manage storing data on your local filesystem. """

from datetime import datetime
from pathlib import Path
from typing import Optional


def timestamped_file_path(
    extension: str,
) -> Path:
    """Returns filepath with timestamp as the name, along with provided extension
    in output directory"""
    render_dir = guaranteed_dir(Path("output").absolute())
    return render_dir / f"{timestamp()}.{extension}"


def guaranteed_dir(p: Path) -> Path:
    """Creates or recreates an empty directory"""
    dir_ = p.absolute()
    if not dir_.is_dir():
        if dir_.exists():
            dir_.unlink()
        dir_.mkdir(parents=True)
    return dir_


def timestamp(prefix: Optional[str] = None) -> str:
    """
    Add a filepath-friendly timestamp to the end of a string.
    Useful to help distinguish files generated inside explorations in a human-readable way.
    """
    prefix = f"{prefix}_" if prefix else ""
    return datetime.utcnow().strftime(f"{prefix}%Y-%m-%d-%H%M-%S%f")
