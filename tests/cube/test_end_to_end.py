from cube.parametrisation import cube_generator
from cube.geometry import cuboid_cad_generator
from cube.export import cad_query_renderer, CommonExporterInputs, RenderInputs
from cube.analysis import geometric_property_analysis


def test_end_to_end():
    side_length = 5
    cube = cube_generator(side_length=side_length)
    cad_output = cuboid_cad_generator(cube)
    rendered_image = cad_query_renderer(
        inputs=RenderInputs(
            common=CommonExporterInputs(
                cad_query_workplane=cad_output,
                file_name="test_cube_render",
                output_subdirectory_name="render",
            )
        )
    )
    geom_props = geometric_property_analysis(cube)
    assert rendered_image.exists()
    assert geom_props.volume == side_length**3
    assert geom_props.surface_area == 6 * side_length**2
