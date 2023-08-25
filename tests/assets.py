from pathlib import Path
from typing import Any

from generative.fabric import Asset, TestingAsset


def download_asset(step_asset: Asset, **kwargs: Any) -> Path:
    """Effectively "downloads" a FileAsset by grabbing it locally (for testing only)"""
    return TestingAsset.from_asset(step_asset).download(**kwargs)
