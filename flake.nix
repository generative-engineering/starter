{
  description = "Generative Starter Project";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-24.05";
    flake-utils.url = "github:numtide/flake-utils";
    treefmt-nix = {
      url = "github:numtide/treefmt-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    treefmt-nix,
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
      treefmtEval = treefmt-nix.lib.evalModule pkgs ./treefmt.nix;
      treefmt = treefmtEval.config.build.wrapper;
      ourPython = pkgs.python311;
      ourPoetry = pkgs.poetry.override {python3 = ourPython;};
    in rec {
      devShells.default = pkgs.mkShell {
        packages = [
          ourPython
          ourPoetry
          pkgs.curl
        ];
      };
      # Used for `nix flake check`
      checks = {
        formatting = treefmtEval.config.build.check self;
      };
      # Used in `nix fmt`
      formatter = treefmt;
    });
}
