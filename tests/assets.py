from pathlib import Path
from typing import Any

from generative.fabric import Asset, TestingAsset, FileAsset


async def download_asset(step_asset: Asset, **kwargs: Any) -> Path:
    """Effectively "downloads" a FileAsset by grabbing it locally (for testing only)"""
    assert isinstance(step_asset, FileAsset), f"Can't use {type(step_asset)}"
    ta = TestingAsset.from_asset(step_asset)
    return await ta.download(**kwargs)
