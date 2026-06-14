#!/bin/bash
# deploy/docker_images/build_docker_images.sh

if [ -z "${DOCKER_CMD}" ];then
    echo "Error: missing DOCKER_CMD"
    exit 1
fi

echo "Building ${DOCKER_CMD} image for GenericSuite CodeGen..."

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

    echo "Building ${DOCKER_CMD} image: $image_name"
    pwd
    ${DOCKER_CMD} build -t "$image_name" -f "$dockerfile" "$src_path"

    if [ $? -eq 0 ]; then
        echo "${DOCKER_CMD} image built successfully: $image_name"
    else
        echo "Error building ${DOCKER_CMD} image: $image_name"
        exit 1
    fi
}

# Build the base image
build_image "fastapitemplate_python" "Dockerfile-Python" "."

# Build the MongoDB Atlas image
build_image "fastapitemplate_mongo_db_atlas" "Dockerfile-MongoDb-Atlas" "."
