import tempfile
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from fastapi import FastAPI
from generative.fabric.http.app import create_app
from pydantic_core._pydantic_core import Url
from pytest import fixture
from starlette.testclient import TestClient


@fixture(scope="module")
def ensure_tests_imported():
    from cube import geometry, parametrisation, renderer

    assert geometry
    assert parametrisation
    assert renderer


@fixture(scope="module")
def assets_dir() -> Path:
    return Path(tempfile.mkdtemp(prefix="assets-"))


@fixture(scope="module")
def app(ensure_tests_imported, assets_dir: Path):
    return create_app(assets_dir, Url("http://testserver"), dirs={Path("tests")})


@fixture(scope="module")
def client(app: FastAPI):
    return TestClient(app)


@fixture(scope="module")
def openapi_path():
    return "/openapi.json"


@fixture(scope="module")
def openapi_post_paths(client: TestClient, openapi_path: str) -> Iterable[dict[str, Any]]:
    resp = client.get(openapi_path)
    assert resp.status_code == 200
    endpoints = resp.json().get("paths", None)

    assert endpoints, f"No OpenAPI paths defined: {resp}"
    return [operation["post"] for path, operation in endpoints.items() if "post" in operation]


@fixture(scope="module")
def openapi_post_endpoint_operation_ids(openapi_post_paths: Iterable[dict[str, Any]]) -> list[str]:
    return [ff["operationId"] for ff in openapi_post_paths]
