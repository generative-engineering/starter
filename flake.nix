{
  description = "Generative Starter Project";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = inputs:
    with inputs;
      flake-utils.lib.eachDefaultSystem (system: let
        pkgs = import nixpkgs {
          inherit system;
        };
      in rec {
        devShell = pkgs.mkShell {
          packages = with pkgs; [
            python310
            (poetry.override {python3 = python310;})
          ];
        };
        apps = {
          poetry = flake-utils.lib.mkApp {drv = pkgs.poetry;};
        };
        formatter = pkgs.alejandra;
      });
}
