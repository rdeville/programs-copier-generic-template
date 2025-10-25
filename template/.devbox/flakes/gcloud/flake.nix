{
  description = "Google Cloud SDK with GKE auth plugin";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {self, nixpkgs, flake-utils}:
    flake-utils.lib.eachDefaultSystem (system:
      let
        overlay = (final: prev: {
          google-cloud-sdk = prev.google-cloud-sdk.withExtraComponents [
            pkgs.google-cloud-sdk.components.gke-gcloud-auth-plugin
          ];
        });

        pkgs = import nixpkgs {
          inherit system overlay;
        };
      in {
        packages = {
          google-cloud-sdk = pkgs.google-cloud-sdk;
        };
      }
    );
}
