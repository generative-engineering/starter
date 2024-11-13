{
  description = "Generative Starter Project";

  inputs = {
    base.url = "git+https://gitlab.com/generative/infra/nix.git";
    nixpkgs.follows = "base/nixpkgs";
  };

  outputs = inputs @ {
    flake-parts,
    base,
    ...
  }:
    flake-parts.lib.mkFlake {inherit inputs;} ({self, ...}: {
      imports = [
        base.flakeModules.default
        base.flakeModules.treefmt-mdl
        base.flakeModules.treefmt-mypy
      ];
      systems = [
        "aarch64-darwin"
        "x86_64-linux"
      ];

      perSystem = {
        config,
        pkgs,
        ...
      }: let
        python = pkgs.python311;
      in {
        poetry.settings = {
          project = {
            inherit python;
            projectDir = ./.;
          };
          app.doCheck = false;
          env.editablePackageSources = {
            cube = ./src;
            tests = ./tests;
          };
        };
        devShells.default = config.poetry.shell.overrideAttrs (old: {
          buildInputs = with pkgs;
            old.buildInputs
            or []
            ++ [
              pkgs.glibcLocales
              # We use this in CI
              pkgs.curl
            ];
          # Don't want the venv management here,
          # as pure Poetry is our main use-case
          shellHook = "";
          POETRY_VIRTUALENVS_CREATE = true;
        });
      };
    });
}
