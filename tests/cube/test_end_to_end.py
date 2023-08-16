import pytest
from cube.parametrisation import cube_generator
from cube.geometry import FileNameAndLocation, generate_cuboid_cad
from cube.renderer import step_renderer
from cube.analysis import geometric_property_analysis


@pytest.mark.parametrize("side_length", [1, 2, 3, 4, 5])
def test_end_to_end(
    step_output_file_location: FileNameAndLocation,
    render_output_file_location: FileNameAndLocation,
    side_length: float,
):
    cube = cube_generator(side_length=side_length)
    step = generate_cuboid_cad(cube, step_output_file_location)
    rendered_image = step_renderer(step_file=step, output_file=render_output_file_location)
    geom_props = geometric_property_analysis(cube)

    # Assert analysis ran
    assert step.exists()
    assert rendered_image.exists()

    # Assert analysis results are as expected
    assert geom_props.volume == side_length**3
    assert geom_props.surface_area == 6 * side_length**2
