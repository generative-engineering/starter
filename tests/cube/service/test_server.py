import logging
import re
import shutil
from pathlib import Path

from _pytest.logging import LogCaptureFixture
from generative.fabric import FabricFunction
from generative.fabric.definitions.function import (
    fabric_function_class_from_function,
    FunctionVersion,
)
from generative.fabric.http.registry import get_subclasses
from generative.fabric.http.routers.functions.v5 import endpoint_path
from starlette.testclient import TestClient

from cube.geometry import generate_cuboid_cad, Cuboid
from cube.renderer import step_renderer

from tests.cube.service import ASSETS_API_VERSION


def test_cube_ffs_all_exposed(openapi_function_names):
    ids = set(openapi_function_names)
    ffs = list(get_subclasses(FabricFunction))
    assert len(ffs) > 3, "Not enough FFs by my reckoning (have some been removed?)"
    missing = {ff.qualified_name() for ff in ffs} - ids
    assert not missing, f"Missing these: {missing}. Did they have errors loading?"


def test_generate_cuboid_cad_works(
    client: TestClient, version: FunctionVersion, caplog: LogCaptureFixture, a_cuboid: Cuboid
):
    with caplog.at_level(logging.INFO):
        path = endpoint_path(fabric_function_class_from_function(generate_cuboid_cad), version)
        resp = client.post(path, json={"cuboid": a_cuboid.as_dict()})
    assert_no_warnings(caplog)

    assert resp.status_code == 200, resp.json()["detail"]
    outputs = resp.json()["data"]["outputs"]
    assert outputs, f"Got no outputs in {resp.json()}"


def assert_no_warnings(caplog: LogCaptureFixture):
    assert caplog.records, "Got no logging at all"
    issues = {r.message for r in caplog.records if r.levelno >= logging.WARNING}
    assert not issues


def test_step_renderer_works(
    client: TestClient,
    version: FunctionVersion,
    tmpdir,
    caplog: LogCaptureFixture,
    step_file: Path,
    server_base_url: str,
):
    asset_path = Path(tmpdir) / step_file.name
    shutil.copyfile(step_file, asset_path)
    # Run our FF
    path = endpoint_path(fabric_function_class_from_function(step_renderer), version)
    with caplog.at_level(logging.INFO):
        resp = client.post(path, json={"step_asset": f"{server_base_url}/{asset_path.name}"})

    assert_no_warnings(caplog)
    assert resp.status_code == 200, resp.json()["detail"]
    asset_uri = resp.json()["data"]["outputs"]
    assert asset_uri, f"Got no outputs in {resp.json()}"
    assert asset_uri.startswith("g8e://assets/"), "not a Generative asset?"
    url = assert_uri_to_api_path(asset_uri)
    resp = client.get(url)
    assert resp.status_code < 400, f"Failed getting URL {url}"
    assert resp.json(), "was expecting some dummy JSON here"


def assert_uri_to_api_path(asset_uri: str) -> str:
    return re.sub(
        r"^g8e://assets/(\w+)/(.+)$", rf"/{ASSETS_API_VERSION}/groups/\1/assets/\2", asset_uri
    )
