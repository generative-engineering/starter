import pytest
from cube.geometry import generate_cuboid_cad
from cube.renderer import step_renderer
from cube.analysis import geometric_property_analysis
from generative.fabric import TestingAsset


@pytest.mark.parametrize("cuboid_fixture", ["a_cube", "a_cuboid"])
def test_end_to_end_cuboid(cuboid_fixture: str, request: pytest.FixtureRequest):
    cuboid = request.getfixturevalue(cuboid_fixture)

    step_asset = TestingAsset.from_asset(generate_cuboid_cad(cuboid))
    rendered_image = step_renderer(step_asset)
    geom_props = geometric_property_analysis(cuboid)

    # Assert analysis ran
    assert TestingAsset.from_asset(step_asset).download().exists()
    assert TestingAsset.from_asset(rendered_image).download().exists()

    # Assert analysis results are as expected
    le, w, h = cuboid.length, cuboid.width, cuboid.height
    assert geom_props.volume == le * w * h
    assert geom_props.surface_area == 2 * (le * w + w * h + h * le)
