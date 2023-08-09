Microtechnology Skeleton
========================

Developing your own Fabric Functions
---------

- Create a new repository through terraform. Follow instructions in our [gitlab infrastructure repo](https://gitlab.com/generative/infra/gitlab-bootstrap).
- Copy the contents of the this repository to it. If you already have some functions to use, then copy them too.
- Create your new Fabric Functions following the usage guide in the [Fabric Definitions README](https://gitlab.com/generative/fabric/fabric-definitions/-/blob/main/README.md?ref_type=heads#usage).
    - Use `pytest` for end-to-end tests and to store example uses.
- Update the README to explain the functionality, keeping the relevant parts from below.

Setup
-----

- [ ] Follow our [poetry setup guide](https://generative.gitlab.io/team/documentation/technical/languages/python/python-setup.html#poetry).
- Run `poetry install` in the terminal to install all the relevant packages.

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
