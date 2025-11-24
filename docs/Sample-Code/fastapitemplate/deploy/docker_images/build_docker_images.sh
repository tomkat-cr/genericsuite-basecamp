#!/bin/bash
# deploy/docker_images/build_docker_images.sh

echo "Building Docker image for GenericSuite CodeGen..."

# Synchronize dependencies from pyproject.toml files to Dockerfile
echo "Synchronizing dependencies from pyproject.toml files..."
if ! bash ../../node_modules/genericsuite-be-scripts/scripts/dependency-sync/sync_dependencies.sh --defaults --verbose; then
    echo ""
    echo "Dependency synchronization failed, continuing with existing Dockerfile"
    echo ""
    echo "You may want to execute the sync manually, run:"
    echo "   bash ../../node_modules/genericsuite-be-scripts/scripts/dependency-sync/sync_dependencies.sh --defaults --verbose"
    echo ""
    echo "Press any key to continue or Ctrl+C to exit..."
    read
fi

build_image() {
    local image_name=$1
    local dockerfile=$2
    local src_path=$3

    echo "Building Docker image: $image_name"
    pwd
    docker build -t "$image_name" -f "$dockerfile" "$src_path"

    if [ $? -eq 0 ]; then
        echo "Docker image built successfully: $image_name"
    else
        echo "Error building Docker image: $image_name"
        exit 1
    fi
}

# Build the base image
build_image "fastapitemplate_python" "Dockerfile-Python" "."

# Build the MongoDB Atlas image
build_image "fastapitemplate_mongo_db_atlas" "Dockerfile-MongoDb-Atlas" "."
