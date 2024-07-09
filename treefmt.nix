{
  pkgs,
  lib,
  ...
}: {
  # Used to find the project root
  projectRootFile = "flake.nix";
  programs.alejandra.enable = true;

  programs.ruff.check = true;
  programs.ruff.format = true;

  settings.formatter = {
    # Less invasive than the provided options
    markdownlint = {
      command = "${pkgs.bash}/bin/bash";
      options = [
        "-euc"
        ''
          # Needed to pick up config
          cd ${./.}
          ${lib.getExe' pkgs.nodePackages.markdownlint-cli2 "markdownlint-cli2"} --fix $@
        ''
        "--" # bash swallows the second argument when using -c
      ];
      includes = ["*.md"];
    };
  };
}
