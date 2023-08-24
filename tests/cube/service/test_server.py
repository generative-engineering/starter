import logging
from shutil import copyfile
from pytest import mark
from _pytest.logging import LogCaptureFixture
from generative.fabric import FabricFunction
from generative.fabric.definitions.function import fabric_function_class_from_function
from generative.fabric.http.registry import get_subclasses
from generative.fabric.http.service import operation_id_for, endpoint_path
from starlette.testclient import TestClient

from cube.geometry import generate_cuboid_cad, Cuboid
from cube.renderer import step_renderer


def test_cube_ffs_all_exposed(openapi_post_endpoint_operation_ids: list[str]):
    ids = openapi_post_endpoint_operation_ids
    ffs = get_subclasses(FabricFunction)
    assert ffs, "No FabricFunctions loaded in Python"
    assert len(list(ffs)) > 3, "Not enough FFs by my reckoning (have some been removed?)"
    missing = {operation_id_for(f) for f in ffs} - set(ids)
    assert not missing, f"Missing these: {missing}. Did they have errors loading?"


def test_generate_cuboid_cad_works(
    client: TestClient, caplog: LogCaptureFixture, a_cuboid: Cuboid
):
    with caplog.at_level(logging.INFO):
        path = endpoint_path(fabric_function_class_from_function(generate_cuboid_cad))
        resp = client.post(path, json={"cuboid": a_cuboid.as_dict()})
    assert_no_warnings(caplog)

    assert resp.status_code == 200, resp.json()["detail"]
    outputs = resp.json()["data"]["outputs"]
    assert outputs, f"Got no outputs in {resp.json()}"
    assert outputs.startswith("http://testserver/assets"), "doesn't look like an asset"


def assert_no_warnings(caplog: LogCaptureFixture):
    assert caplog.records, "Got no logging at all"
    issues = {r.message for r in caplog.records if r.levelno >= logging.WARNING}
    assert not issues


@mark.xfail(reason="Waiting for injectable HTTP clients FND-1620")
def test_step_renderer_works(client: TestClient, assets_dir, caplog: LogCaptureFixture, step_file):
    a_step_name = "test.step"
    step_asset_file = assets_dir / a_step_name
    copyfile(step_file, step_asset_file)
    assert step_asset_file.exists()
    assert client.get("http://testserver/assets/foo.step")
    path = endpoint_path(fabric_function_class_from_function(step_renderer))

    # Run our FF
    with caplog.at_level(logging.INFO):
        resp = client.post(path, json={"step_asset": f"http://testserver/assets/{a_step_name}"})
    assert_no_warnings(caplog)

    assert resp.status_code == 200, resp.json()["detail"]
    outputs = resp.json()["data"]["outputs"]
    assert outputs, f"Got no outputs in {resp.json()}"
    assert outputs.startswith("http://testserver/assets"), "doesn't look like an asset"
