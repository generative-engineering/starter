Microtechnology Skeleton
------------------------

Pre-setup
---------

Create a new repository for your microtechnology through terraform,
by following instructions in our [gitlab infrastructure repo](https://gitlab.com/generative/infra/gitlab-bootstrap).

Then, copy the contents of this repository into your new one to get started.

The steps below can be kept in the new repo too.

Setup
-----

### Poetry
Python dependencies are managed with [Poetry](https://python-poetry.org).
See their website for installation instructions if you don't have it.

First (if you haven't set this up already for another project), go to Gitlab and create
[a personal API token](https://gitlab.com/-/profile/personal_access_tokens).
Give it a name (e.g. _PyPI_), and grant it `read_api`.
Copy the secret value and **don't lose it**.

Then run these with the right values substituted for `...`:
```shell
export GENERATIVE_GITLAB_USER="..."
export GENERATIVE_GITLAB_TOKEN="..."
```

Then run:
```shell
poetry config virtualenvs.in-project true
poetry config http-basic.gitlab $GENERATIVE_GITLAB_USER "$GENERATIVE_GITLAB_TOKEN"
```
Further info [in their config docs](https://python-poetry.org/docs/configuration)

With this done, setting up the environment should be as simple as running
```shell
poetry install --extras visualisations
```
Note the `--extras visualisations` is optional if you do not want to run the visualisation dashboard.

For a minimal installation that just supports running the engine,
use
```shell
poetry install
```

Running First Exploration
--------------------

Once you have set up (as above), try the following to "compile" the design file:
```shell
poetry run engine compile --fabric src designs/cube_design.yaml --compiled-file designs/cube_design.compiled.yaml
```
If this succeeds (it won't print anything, but no errors should be raised),
you can inspect the "completed" design file at `designs/cube_design.compiled.yaml`.
If not, you may not have followed the setup instructions properly.

If this works, you can run an exploration with the following:
```shell
poetry run engine run --fabric src designs/cube_design.yaml --output-file output/results.json
```
which will save the overall exploration results in `ouptut/results.json`.
At the moment, custom visualisations for interpreting these results have to be built.

You can however see many files generated and put in the `output/renders` directory.
If you update the `CuboidRenderer` function to generate images of your microtechnology,
you will see them here.
