{
  description = "Generative Starter Project";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = inputs: with inputs;
    flake-utils.lib.eachDefaultSystem (system:
    let
     pkgs = import nixpkgs {
        inherit system;
      };
     libPath = with pkgs; lib.makeLibraryPath [
        libGL
        stdenv.cc.cc
        xorg.libX11
     ];
    in
    rec {
      devShell =
        pkgs.mkShell {
          packages = with pkgs; [
            libGL
            xorg.libX11
            python39
            (poetry.override { python3 = python39; })
          ];
          # See https://github.com/albertgoncalves/ranim/blob/e59ee646c155fefba69b6f3b9aaad0402d360c2e/shell.nix#L37
          shellHook = ''
            export LD_LIBRARY_PATH="${libPath}:$LD_LIBRARY_PATH"
            # echo -e "Current LD_LIBRARY_PATH:\n$LD_LIBRARY_PATH" | tr ':' '\n'
          '';
        };
      apps = {
          poetry = flake-utils.lib.mkApp { drv = pkgs.poetry; };
        };
    });
}
