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
        devShells.default = pkgs.mkShell {
          # Some Python deps need these available to install
          LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [pkgs.stdenv.cc.cc];
          packages = [
            ourPython
            ourPoetry
          ];
        };
        formatter = pkgs.alejandra;
      });
}
