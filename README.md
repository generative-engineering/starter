# Microtechnology Skeleton

## Pre-setup

- [ ] Create a new repository through terraform. Follow instructions in our [gitlab infrastructure repo](https://gitlab.com/generative/infra/gitlab-bootstrap).
- [ ] If you already have something, then copy the contents of this repository into your new one to get started.

The steps below can be kept in the new repo too.

## Setup

- [ ] Follow our [poetry setup guide](https://generative.gitlab.io/team/documentation/technical/languages/python/python-setup.html#poetry).


## Running First Exploration

- [ ] Create a new design file, such as `designs/cube.yaml`
- [ ] Run an explorer compile to make sure it is valid, run the command:
	
```shell
poetry run explorer compile --fabric src designs/cube.yaml
```
- It won't print anything, but no errors should be raised. You can inspect the "completed" design file at `designs/cube.compiled.yaml`.
	- If it fails, then you may not have followed the setup instructions properly.
- [ ] Run an exploration: 

```shell
poetry run explorer run --fabric src designs/cube.yaml
```

## What's Next?

- Start hacking! Replace the simple `cube` models with something wild.
- When pushing to the cloud, append `--save-to-cloud` to the explorer run command above:
```shell
poetry run explorer run --fabric src designs/cube.yaml --save-to-cloud
```