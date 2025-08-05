#!/bin/sh
# scripts/link_common_assets.sh
# Link ExampleApp common files, directories and libraries
# 2025-07-04 | CR

copy_common_assets() {
    common_asset_source_name="$1"
    common_asset_target_name="$2"
    echo ""
    echo "Copying '$common_asset_source_name' to '$common_asset_target_name'"
    if ! cp -r "${BASE_DIR}/$common_asset_source_name" "${BASE_DIR}/$common_asset_target_name"
    then
        echo "ERROR: Could not copy '$common_asset_source_name' to '$common_asset_target_name'"
    fi
}

link_common_assets() {
    common_asset_source_name="$1"
    common_asset_target_name="$2"
    echo ""
    echo "Linking '$common_asset_source_name' to '$common_asset_target_name'"
    if ! ln -s "${BASE_DIR}/$common_asset_source_name/" "${BASE_DIR}/$common_asset_target_name/"
    then
        echo "ERROR: Could not link '$common_asset_source_name' to '$common_asset_target_name'"
    fi
}

unlink_common_assets() {
    common_asset_source_name="$1"
    common_asset_target_name="$2"

    echo ""
    echo "Unlinking '$common_asset_source_name' from '$common_asset_target_name'"

    if ! unlink "${BASE_DIR}/$common_asset_target_name/$common_asset_source_name"
    then
        echo "ERROR: Could not unlink '${BASE_DIR}/$common_asset_target_name/$common_asset_source_name'"
    fi
}

remove_common_assets() {
    common_asset_source_name="$1"
    echo ""
    echo "Removing '$common_asset_source_name'"
    if ! rm -rf "${BASE_DIR}/$common_asset_source_name"
    then
        echo "ERROR: Could not remove '${BASE_DIR}/$common_asset_source_name'"
    fi
}

BASE_DIR="`pwd`"
cd "`dirname "$0"`" ;
SCRIPTS_DIR="`pwd`" ;
cd "${BASE_DIR}"

ACTION="$1"

COPY_OR_SYMLINK="$2"
if [ "$COPY_OR_SYMLINK" = "" ]; then
    COPY_OR_SYMLINK="copy"
    # COPY_OR_SYMLINK="symlink"
fi

echo ""
echo "link_common_assets.sh"
echo "BASE_DIR: $BASE_DIR"
echo "SCRIPTS_DIR: $SCRIPTS_DIR"
echo "ACTION: $ACTION"
echo "COPY_OR_SYMLINK: $COPY_OR_SYMLINK"
echo ""

if [ "$ACTION" = "link" ]; then
    echo ""
    echo "link_common_assets.sh | Linking common assets..."
    copy_common_assets "apps/config_dbdef" "apps/ui/src/configs"
    if [ "$COPY_OR_SYMLINK" = "symlink" ]; then
        link_common_assets "apps/config_dbdef" "apps/api-chalice/lib"
        link_common_assets "apps/config_dbdef" "apps/api-fastapi/lib"
        link_common_assets "apps/config_dbdef" "apps/api-flask/lib"
        link_common_assets "apps/config_dbdef" "apps/mcp-server/lib"
        link_common_assets "apps/api-chalice/lib/config" "apps/api-fastapi/lib"
        link_common_assets "apps/api-chalice/lib/config" "apps/api-flask/lib"
        link_common_assets "apps/api-chalice/lib/config" "apps/mcp-server/lib"
        link_common_assets "apps/api-chalice/lib/models" "apps/api-fastapi/lib"
        link_common_assets "apps/api-chalice/lib/models" "apps/api-flask/lib"
        link_common_assets "apps/api-chalice/lib/models" "apps/mcp-server/lib"
        link_common_assets "apps/api-chalice/scripts" "apps/api-fastapi"
        link_common_assets "apps/api-chalice/scripts" "apps/api-flask"
        link_common_assets "apps/api-chalice/scripts" "apps/mcp-server"
    else
        copy_common_assets "apps/config_dbdef" "apps/api-chalice/lib/"
        copy_common_assets "apps/config_dbdef" "apps/api-fastapi/lib/"
        copy_common_assets "apps/config_dbdef" "apps/api-flask/lib/"
        copy_common_assets "apps/config_dbdef" "apps/mcp-server/lib/"
        copy_common_assets "apps/api-chalice/lib/config" "apps/api-fastapi/lib/"
        copy_common_assets "apps/api-chalice/lib/config" "apps/api-flask/lib/"
        copy_common_assets "apps/api-chalice/lib/config" "apps/mcp-server/lib/"
        copy_common_assets "apps/api-chalice/lib/models" "apps/api-fastapi/lib/"
        copy_common_assets "apps/api-chalice/lib/models" "apps/api-flask/lib/"
        copy_common_assets "apps/api-chalice/lib/models" "apps/mcp-server/lib/"
        copy_common_assets "apps/api-chalice/scripts" "apps/api-fastapi/"
        copy_common_assets "apps/api-chalice/scripts" "apps/api-flask/"
        copy_common_assets "apps/api-chalice/scripts" "apps/mcp-server/"
    fi
    exit 0
fi

if [ "$ACTION" = "unlink" ]; then
    echo ""
    echo "link_common_assets.sh | Unlinking common assets..."
    remove_common_assets "apps/ui/src/configs"
    if [ "$COPY_OR_SYMLINK" = "symlink" ]; then
        unlink_common_assets "config_dbdef" "apps/api-chalice/lib"
        unlink_common_assets "config_dbdef" "apps/api-fastapi/lib"
        unlink_common_assets "config_dbdef" "apps/api-flask/lib"
        unlink_common_assets "config_dbdef" "apps/mcp-server/lib"
        unlink_common_assets "config" "apps/api-fastapi/lib"
        unlink_common_assets "config" "apps/api-flask/lib"
        unlink_common_assets "config" "apps/mcp-server/lib"
        unlink_common_assets "models" "apps/api-fastapi/lib"
        unlink_common_assets "models" "apps/api-flask/lib"
        unlink_common_assets "models" "apps/mcp-server/lib"
        unlink_common_assets "scripts" "apps/api-fastapi"
        unlink_common_assets "scripts" "apps/api-flask"
        unlink_common_assets "scripts" "apps/mcp-server"
    else
        remove_common_assets "apps/api-chalice/lib/config_dbdef"
        remove_common_assets "apps/api-fastapi/lib/config_dbdef"
        remove_common_assets "apps/api-flask/lib/config_dbdef"
        remove_common_assets "apps/mcp-server/lib/config_dbdef"
        remove_common_assets "apps/api-fastapi/lib/config"
        remove_common_assets "apps/api-flask/lib/config"
        remove_common_assets "apps/mcp-server/lib/config"
        remove_common_assets "apps/api-fastapi/lib/models"
        remove_common_assets "apps/api-flask/lib/models"
        remove_common_assets "apps/mcp-server/lib/models"
        remove_common_assets "apps/api-fastapi/scripts"
        remove_common_assets "apps/api-flask/scripts"
        remove_common_assets "apps/mcp-server/scripts"
    fi
    exit 0
fi

echo ""
echo "ERROR: Unknown action: '$ACTION'"
echo ""
exit 1

