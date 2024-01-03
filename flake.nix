{
  description = "Generative Starter Project";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-23.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = inputs:
    with inputs;
      flake-utils.lib.eachDefaultSystem (system: let
        pkgs = import nixpkgs {
          inherit system;
        };
        ourPython = pkgs.python310;
        ourPoetry = pkgs.poetry.override {python3 = ourPython;};
      in rec {
        devShell = pkgs.mkShell {
          packages = [
            ourPython
            ourPoetry
          ];
        };
        apps = {
          poetry = flake-utils.lib.mkApp {drv = ourPoetry;};
        };
        formatter = pkgs.alejandra;
      });
}
