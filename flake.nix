{
  description = "Generative Starter Project";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-23.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
      ourPython = pkgs.python311;
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
      checks = {
        lint-shell =
          pkgs.runCommand "shellcheck"
          {buildInputs = [pkgs.shellcheck];}
          ''
            mkdir $out
            echo "⏳ Running shellcheck on:"
            find ${./.} -iname "*.sh" -print -exec shellcheck {} \+
          '';

        lint-nix =
          pkgs.runCommand "alejandra"
          {buildInputs = [pkgs.alejandra];}
          ''
            mkdir $out
            echo "⏳ Running alejandra"
            alejandra --check ${./.}
          '';
        lint-python =
          pkgs.runCommand "ruff"
          {buildInputs = [pkgs.ruff];}
          ''
            mkdir $out
            echo "⏳ Running Ruff"
            ruff check ${./src} ${./tests}
          '';
        lint-docker =
          pkgs.runCommand "hadolint"
          {buildInputs = [pkgs.hadolint];}
          ''
            mkdir $out
            echo "⏳ Running hadolint"
            find ${./.} -name "*Dockerfile*" -print -execdir hadolint {} +
          '';
      };
      formatter = pkgs.alejandra;
    });
}
