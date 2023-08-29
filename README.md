Fabric Function Starter
========================

Developing your own Fabric Functions
------------------------------------

- Create a new repository through terraform. Follow instructions in our [gitlab infrastructure repo](https://gitlab.com/generative/infra/gitlab-bootstrap).
- Copy the contents of this repository to it. If you already have some functions to use, then copy them too.
    - Delete the `cube` example package (keeping the `utils.py` file if you want) once you're happy with how it works.
     Update the package name and path in `pyproject.toml` and `gitlab-ci.yml` files.
- Create your new Fabric Functions following the usage guide in the [Fabric Guide](https://gitlab.com/generative/fabric/fabric-definitions/-/blob/main/docs/fabric_guide.md).
    - Use `pytest` for unit tests and also for end-to-end tests for benchmarking or storing examples.
    As shown in the [example](/tests/cube/test_end_to_end.py),
    use fixtures to provide fabric function inputs, and call fabric functions in the order they'll be called during graph execution.
- Update the README to explain the functionality, keeping the relevant parts from below.

Setup
-----

- [ ] Follow our [poetry setup guide](https://generative.gitlab.io/team/documentation/technical/languages/python/python-setup.html#poetry).
- Run `poetry install` in the terminal to install all the relevant packages.
- We use a basic Nix flake for this project:
  `nix develop` gives you a shell with the right version of Python and Poetry.
  See the [Generative Nix guide](https://generative.gitlab.io/team/documentation/technical/software-development/nix.html)

Use
---

### Running function service

To run a local function service exposing the Fabric Functions defined in `src/cube`, run:

```shell
poetry run server src/cube
```

After navigating to the doc site of the port the server is bound to, e.g. `http://localhost:3000/docs`,
you will see the API of the Fabric Functions defined.

When this server is running, the UI (currently under development) will be able to use the Fabric Functions you've defined.
The server must be restarted to update the API endpoints with any changes made in the code.

### Linting
Use the script (via Poetry):

```shell
poetry run bin/lint.sh
```
