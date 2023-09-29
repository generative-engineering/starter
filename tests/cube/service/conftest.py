import functools
import re
import tempfile
from collections.abc import Iterable
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
from typing import Any, cast

from fastapi import FastAPI
from generative.fabric.http.app import create_app
from generative.fabric.http.dependencies import get_settings, Settings
from pydantic import AnyUrl
from pytest import fixture
from starlette.testclient import TestClient

TEST_BASE_URL = AnyUrl("http://testserver")
"""Used by TestClient"""


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
def version() -> str:
    return "TESTING"


@fixture(scope="module")
def app(ensure_tests_imported, version: str, assets_dir: Path) -> FastAPI:
    def get_custom_settings():
        return Settings(base_url=TEST_BASE_URL, assets_dir=assets_dir)

    app = create_app(version, assets_dir, TEST_BASE_URL, dirs={Path("tests")})
    app.dependency_overrides[get_settings] = get_custom_settings
    return app


@fixture(scope="module")
def client(app: FastAPI):
    return TestClient(app)


@fixture(scope="module")
def openapi_path():
    return "/openapi.json"


@fixture(scope="module")
def openapi_post_endpoints(client: TestClient, openapi_path: str) -> Iterable[dict[str, Any]]:
    resp = client.get(openapi_path)
    assert resp.status_code == 200
    endpoints = resp.json().get("paths", None)

    assert endpoints, f"No OpenAPI paths defined: {resp}"
    return [
        operation["post"]
        for path, operation in endpoints.items()
        if "post" in operation and "/v3/functions" in path
    ]


@fixture(scope="module")
def openapi_function_names(openapi_post_endpoints) -> list[str]:
    return [_get_class_from_operation_id(ff["operationId"]) for ff in openapi_post_endpoints]


def _get_class_from_operation_id(operation_id: str) -> str:
    return re.sub(r"^(.*)\.[^.]+\.evaluate$", r"\1", operation_id)


@fixture
def server(tmpdir):
    handler_cls = functools.partial(SimpleHTTPRequestHandler, directory=tmpdir)
    server = HTTPServer(("localhost", 0), handler_cls)
    yield server
    server.shutdown()


@fixture
def server_thread(server):
    t = Thread(target=server.serve_forever)
    t.start()
    yield
    server.shutdown()
    t.join()


@fixture
def server_base_url(server: HTTPServer, server_thread) -> str:
    host, port = server.server_address
    return f"http://{cast(str, host)}:{port}"
