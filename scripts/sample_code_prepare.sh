#!/bin/bash
# File: scripts/sample_code_prepare.sh
# Prepare sample code (exampleapp and fastapitemplate) to use the latest packages
# 2026-03-13 | CR

uninstal_python_packages() {
    local python_packages_dir=$1
    local packages=$2
    local cmd="uv remove $packages"
    echo "Uninstalling python packages '$packages' in $python_packages_dir"
    cd $python_packages_dir
    if ! $cmd; then
        echo "❌ $cmd failed..."
        exit 1
    fi
    cd -
}

install_python_packages() {
    local python_packages_dir=$1
    local packages=$2
    local cmd="uv add $packages"
    echo "Installing python packages '$packages' in $python_packages_dir"
    cd $python_packages_dir
    if ! $cmd; then
        echo "❌ $cmd failed..."
        exit 1
    fi
    cd -
}

uninstal_npm_packages() {
    local npm_packages_dir=$1
    local packages=$2
    local cmd="npm uninstall $packages"
    echo "Uninstalling npm packages '$packages' in $npm_packages_dir"
    cd $npm_packages_dir
    if ! $cmd; then
        echo "❌ $cmd failed..."
        exit 1
    fi
    cd -
}

install_npm_packages() {
    local npm_packages_dir=$1
    local packages=$2
    local cmd="npm install $packages"
    echo "Installing npm packages '$packages' in $npm_packages_dir"
    cd $npm_packages_dir
    if ! $cmd; then
        echo "❌ $cmd failed..."
        exit 1
    fi
    cd -
}

uninstal_python_packages "docs/code/exampleapp/apps/api-flask" "genericsuite genericsuite-ai"
uninstal_npm_packages "docs/code/exampleapp/apps/api-flask" "genericsuite-be-scripts"
install_python_packages "docs/code/exampleapp/apps/api-flask" "genericsuite genericsuite-ai"
install_npm_packages "docs/code/exampleapp/apps/api-flask" "genericsuite-be-scripts"

uninstal_python_packages "docs/code/exampleapp/apps/api-chalice" "genericsuite genericsuite-ai"
uninstal_npm_packages "docs/code/exampleapp/apps/api-chalice" "genericsuite-be-scripts"
install_python_packages "docs/code/exampleapp/apps/api-chalice" "genericsuite genericsuite-ai"
install_npm_packages "docs/code/exampleapp/apps/api-chalice" "genericsuite-be-scripts"

uninstal_python_packages "docs/code/exampleapp/apps/api-fastapi" "genericsuite genericsuite-ai"
uninstal_npm_packages "docs/code/exampleapp/apps/api-fastapi" "genericsuite-be-scripts"
install_python_packages "docs/code/exampleapp/apps/api-fastapi" "genericsuite genericsuite-ai"
install_npm_packages "docs/code/exampleapp/apps/api-fastapi" "genericsuite-be-scripts"

uninstal_npm_packages "docs/code/exampleapp/apps/ui" "genericsuite genericsuite-ai"
install_npm_packages "docs/code/exampleapp/apps/ui" "genericsuite genericsuite-ai"

uninstal_python_packages "docs/code/fastapitemplate/server" "genericsuite genericsuite-ai"
uninstal_npm_packages "docs/code/fastapitemplate/server" "genericsuite-be-scripts"
install_python_packages "docs/code/fastapitemplate/server" "genericsuite genericsuite-ai"
install_npm_packages "docs/code/fastapitemplate/server" "genericsuite-be-scripts"

uninstal_npm_packages "docs/code/fastapitemplate/ui" "genericsuite genericsuite-ai"
install_npm_packages "docs/code/fastapitemplate/ui" "genericsuite genericsuite-ai"
