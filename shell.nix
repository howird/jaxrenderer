{pkgs ? import <nixpkgs> {}}: let
  lib = pkgs.lib;
in
  pkgs.mkShell {
    packages = with pkgs; [
      uv
    ];

    LD_LIBRARY_PATH = lib.optionalString pkgs.stdenv.isLinux (
      lib.makeLibraryPath (
        pkgs.pythonManylinuxPackages.manylinux1
        ++ (with pkgs; [
          dbus
          fontconfig
          freetype
          zstd

          glfw
          glm
          libGL
          libglvnd
          libX11
          libXcursor
          libXi
          libXinerama
          libxkbcommon
          libXrandr
          libXt
          wayland
          xrandr
        ])
      )
    );

    shellHook = ''
      unset PYTHONPATH
      uv sync --group test --frozen
      . .venv/bin/activate
    '';
  }
