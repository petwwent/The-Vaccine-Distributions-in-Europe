{ pkgs ? import <nixpkgs> {} }:

let
  pythonPackages = with pkgs.python311Packages; [
    fastapi==0.104.1
    numpy==1.26.2
    uvicorn==0.15.0
    pandas==1.3.3
    plotly==5.3.1
  ];
# https://ryantm.github.io/nixpkgs/languages-frameworks/python/#how-to-consume-python-modules-using-pip-in-a-virtual-environment-like-i-am-used-to-on-other-operating-systems
in pkgs.mkShell rec {
  buildInputs = [
    # A Python interpreter including the 'venv' module is required to bootstrap
    # the environment.
    pkgs.python311
    pythonPackages
  ];
}
