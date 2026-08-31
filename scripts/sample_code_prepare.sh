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
        # exit 1
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

get_pypi_git_url() {
    local repo_name=$1
    local branch_name=$2
    echo "git+https://github.com/tomkat-cr/$repo_name@$branch_name"
}

get_npm_git_url() {
    local repo_name=$1
    local branch_name=$2
    echo "tomkat-cr/$repo_name#$branch_name"
}

if [ "$BRANCH" == "" ]; then
    export GS_FE_CORE="genericsuite"
    export GS_FE_AI="genericsuite-ai"
    export GS_FE_SCRIPTS="genericsuite-fe-scripts"
    export GS_BE_CORE="genericsuite"
    export GS_BE_AI="genericsuite-ai"
    export GS_BE_SCRIPTS="genericsuite-be-scripts"
else
    export GS_FE_CORE=$(get_npm_git_url genericsuite-fe $BRANCH)
    export GS_FE_AI=$(get_npm_git_url genericsuite-fe-ai $BRANCH)
    export GS_FE_SCRIPTS=$(get_npm_git_url genericsuite-fe-scripts $BRANCH)
    export GS_BE_CORE=$(get_pypi_git_url genericsuite-be $BRANCH)
    export GS_BE_AI=$(get_pypi_git_url genericsuite-be-ai $BRANCH)
    export GS_BE_SCRIPTS=$(get_npm_git_url genericsuite-be-scripts $BRANCH)
fi

uninstal_python_packages "mkdocs_root/code/exampleapp/apps/api-flask" "genericsuite genericsuite-ai"
uninstal_npm_packages "mkdocs_root/code/exampleapp/apps/api-flask" "genericsuite-be-scripts"
install_python_packages "mkdocs_root/code/exampleapp/apps/api-flask" "$GS_BE_CORE $GS_BE_AI"
install_npm_packages "mkdocs_root/code/exampleapp/apps/api-flask" "-D $GS_BE_SCRIPTS"

uninstal_python_packages "mkdocs_root/code/exampleapp/apps/api-chalice" "genericsuite genericsuite-ai"
uninstal_npm_packages "mkdocs_root/code/exampleapp/apps/api-chalice" "genericsuite-be-scripts"
install_python_packages "mkdocs_root/code/exampleapp/apps/api-chalice" "$GS_BE_CORE $GS_BE_AI"
install_npm_packages "mkdocs_root/code/exampleapp/apps/api-chalice" "-D $GS_BE_SCRIPTS"

uninstal_python_packages "mkdocs_root/code/exampleapp/apps/api-fastapi" "genericsuite genericsuite-ai"
uninstal_npm_packages "mkdocs_root/code/exampleapp/apps/api-fastapi" "genericsuite-be-scripts"
install_python_packages "mkdocs_root/code/exampleapp/apps/api-fastapi" "$GS_BE_CORE $GS_BE_AI"
install_npm_packages "mkdocs_root/code/exampleapp/apps/api-fastapi" "-D $GS_BE_SCRIPTS"

uninstal_npm_packages "mkdocs_root/code/exampleapp/apps/ui" "genericsuite genericsuite-ai genericsuite-fe-scripts"
install_npm_packages "mkdocs_root/code/exampleapp/apps/ui" "$GS_FE_CORE $GS_FE_AI"
install_npm_packages "mkdocs_root/code/exampleapp/apps/ui" "-D $GS_FE_SCRIPTS"

uninstal_python_packages "mkdocs_root/code/fastapitemplate/server" "genericsuite genericsuite-ai"
uninstal_npm_packages "mkdocs_root/code/fastapitemplate/server" "genericsuite-be-scripts"
install_python_packages "mkdocs_root/code/fastapitemplate/server" "$GS_BE_CORE $GS_BE_AI"
install_npm_packages "mkdocs_root/code/fastapitemplate/server" "-D $GS_BE_SCRIPTS"

uninstal_npm_packages "mkdocs_root/code/fastapitemplate/ui" "genericsuite genericsuite-ai genericsuite-fe-scripts"
install_npm_packages "mkdocs_root/code/fastapitemplate/ui" "$GS_FE_CORE $GS_FE_AI"
install_npm_packages "mkdocs_root/code/fastapitemplate/ui" "-D $GS_FE_SCRIPTS"
