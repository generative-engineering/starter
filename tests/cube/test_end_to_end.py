from cube.parametrisation import cube_generator
from cube.geometry import FileNameAndLocation, cuboid_cad_generator
from cube.renderer import step_renderer
from cube.analysis import geometric_property_analysis


def test_end_to_end():
    side_length = 5
    cube = cube_generator(side_length=side_length)
    step_output = FileNameAndLocation(name="test_cube", directory="output", subdirectory="step")
    step = cuboid_cad_generator(cube, step_output)
    rendered_image = step_renderer(
        step_file=step,
        output_file=FileNameAndLocation(
            name="test_cube_render",
            directory="output",
            subdirectory="render",
        ),
    )
    geom_props = geometric_property_analysis(cube)

    assert step.exists()
    assert rendered_image.exists()
    assert geom_props.volume == side_length**3
    assert geom_props.surface_area == 6 * side_length**2
