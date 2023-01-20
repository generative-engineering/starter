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

See our
[Poetry setup guide](https://generative.gitlab.io/team/documentation/technical/languages/python/python-setup.html#poetry).

Running First Exploration
--------------------

Once you have set up (as above), try the following to "compile" the design file:
```shell
poetry run explorer compile --fabric src designs/cube.yaml --compiled-file designs/cube.compiled.yaml
```
If this succeeds (it won't print anything, but no errors should be raised),
you can inspect the "completed" design file at `designs/cube.compiled.yaml`.
If not, you may not have followed the setup instructions properly.

If this works, you can run an exploration with the following:
```shell
poetry run explorer run --fabric src designs/cube.yaml --output-file output/results.json
```

What's Next?
------------

Start hacking! Replace the simple cube models with something wild.
