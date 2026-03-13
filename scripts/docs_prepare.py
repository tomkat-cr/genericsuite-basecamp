import os
import shutil
import sys
import argparse

# Flutter does not support .svg files... yet
allowed_extensions = [
    ".md",
    # ".pdf",
    ".json",
    ".yml",
    ".yaml",
    ".toml",
    ".sh",
    ".ico",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".bmp",
    ".wbmp",
    ".svg",
]

ignore_files = [
    "package.json",
    "package-lock.json",
    "pyproject.toml",
    "CHANGELOG.md",
    "manifest.json",
    "config-example.json",
    "dynamodb_cf_template.yaml",
    "run_mcp_server.sh",
    "claude_desktop_config.json",
    "vscode_mcp_config.json",
    "deployment.yml",
    "docker-compose.yml",
    "tsconfig.json",
    "base.json",
    "nextjs.json",
    "react-library.json",
    "pnpm-lock.yaml",
    "pnpm-workspace.yaml",
    "turbo.json",
    "build_if_required.sh",
    "clean_directory.sh",
    "init_env_files.sh",
    "link_common_assets.sh",
    "run-deploy.sh",
    "build_docker_images.sh",
    "server-entrypoint.sh",
    "claude_desktop_http_config.json",
    "claude_desktop_stdio_config.json",
    "vscode_mcp_http_config.json",
    "vscode_mcp_stdio_config.json",
    "copy_env_files.sh",
    "init_app_environment.sh",
    "docs_manifest.json",
]


def clean_path(path):
    if path.startswith("./"):
        path = path[2:]
    return path


def main():
    parser = argparse.ArgumentParser(
        description="Convert MkDocs to Flutter Assets")
    parser.add_argument("--docs_dir", required=True,
                        help="Path to the /docs directory")
    parser.add_argument("--output_dir", default="docs_for_ftp",
                        help="Path to output cleaned /docs directory")
    parser.add_argument("--mkdocs_path", default="mkdocs.yml",
                        help="Path to mkdocs.yml file")
    args = parser.parse_args()

    docs_dir = args.docs_dir
    dest_dir = args.output_dir
    mkdocs_path = args.mkdocs_path

    if not os.path.exists(mkdocs_path):
        print(f"Error: mkdocs.yml not found at {mkdocs_path}")
        sys.exit(1)

    # Clean output directory
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir)

    files_processed = []
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(tuple(allowed_extensions)) and \
                    os.path.basename(file) not in ignore_files and \
                    file not in files_processed:

                rel_path = os.path.relpath(os.path.join(root, file), docs_dir)
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, rel_path)

                print(f"Processing file: {rel_path}")

                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copy2(src_file, dest_file)

                files_processed.append(src_file)

    print(f"Conversion complete. {len(files_processed)} files processed.")


if __name__ == "__main__":
    main()
