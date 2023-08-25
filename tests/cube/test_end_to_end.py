import pytest
from generative.fabric import TestingAsset

from cube.analysis import geometric_property_analysis
from cube.geometry import generate_cuboid_cad
from cube.renderer import step_renderer
from tests.assets import download_asset


@pytest.mark.parametrize("cuboid_fixture", ["a_cube", "a_cuboid"])
def test_end_to_end_cuboid(cuboid_fixture: str, request: pytest.FixtureRequest):
    cuboid = request.getfixturevalue(cuboid_fixture)

    step_asset = TestingAsset.from_asset(generate_cuboid_cad(cuboid))
    rendered_image = step_renderer(step_asset)
    geom_props = geometric_property_analysis(cuboid)

    # Assert analysis ran
    assert download_asset(step_asset).exists()
    assert download_asset(rendered_image).exists()

    # Assert analysis results are as expected
    le, w, h = cuboid.length, cuboid.width, cuboid.height
    assert geom_props.volume == le * w * h
    assert geom_props.surface_area == 2 * (le * w + w * h + h * le)
