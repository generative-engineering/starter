from time import sleep, time

from cube.export import (
    cad_query_renderer,
    CommonExporterInputs,
    cad_query_step_exporter,
    RenderInputs,
)
import cadquery as cq


def test_cuboid_renderer(a_cad_query_cuboid: cq.Workplane):
    inputs = RenderInputs(
        common=CommonExporterInputs(
            cad_query_workplane=a_cad_query_cuboid,
            file_name="render",
            output_subdirectory_name="render",
        )
    )
    outputs = cad_query_renderer(inputs)
    assert outputs.exists()


def test_cuboid_step_export(a_cad_query_cuboid: cq.Workplane):
    then = time()
    sleep(0.1)  # disk caches are weird
    inputs = CommonExporterInputs(
        cad_query_workplane=a_cad_query_cuboid,
        file_name="render",
        output_subdirectory_name="render",
    )
    step = cad_query_step_exporter(inputs)
    assert step.exists()
    assert step.stat().st_mtime > then, "Didn't produce a new file?"
