#!/bin/bash
# clean_directory.sh
# Clean up all `node_modules`, `dist`, `build`, `.env*`, `.turbo`, `logs` directories under `docs/Sample-Code/exampleapp` (or ./site) and sub-directories.
# 2025-07-05 | CR

remove_item() {
    local item_path="$1"
    if [ -d "${item_path}" ]; then
        echo "Removing directory: ${item_path}"
        rm -rf "${item_path}"
    elif [ -f "${item_path}" ]; then
        echo "Removing file: ${item_path}"
        rm -rf "${item_path}"
    fi
}

show_dir() {
    echo "Directory: $1"
    ls -la "$1"
}

show_file() {
    echo "File: $1"
    cat "$1"
}
    
show_help() {
    echo "Usage: clean_directory.sh <directory_path_to_clean> <remove_envs> <debug>"
    echo ""
    echo "Example:"
    echo "clean_directory.sh ./docs/Sample-Code/exampleapp true true"
    echo ""
    exit 1
}

clean_directory() {
    local directory_path_to_clean="$1"
    local remove_envs="$2"
    local debug="$3"
    if [ "${debug}" = "true" ]; then
        echo ""
        echo "clean_directory()"
        echo "directory_path_to_clean: ${directory_path_to_clean}"
        echo "remove_envs: ${remove_envs}"
        echo "debug: ${debug}"
        echo ""
        echo "Directories to remove:"
        find "${directory_path_to_clean}" -type d \( -name "node_modules" -o -name "dist" -o -name "build" -o -name ".turbo" -o -name "logs" -o -name "__pycache__" -o -name "venv" -o -name ".DS_Store" \) -exec bash -c 'show_dir "$0"' {} \;
        echo ""
        echo "Files to remove:"
        find "${directory_path_to_clean}" -type f \( -name ".DS_Store" \) -exec bash -c 'show_file "$0"' {} \;
        if [ "${remove_envs}" = "true" ]; then
            echo ""
            echo ".env files to remove:"
            find "${directory_path_to_clean}" -type f \( -name ".env" -o -name "*.bak" -o -name "*.log" \) -exec bash -c 'show_file "$0"' {} \;
        fi
        echo ""
        echo "Press [Enter] key to confirm the directories/files to remove [FTP-010]"
        read
    fi
    echo ""
    echo "Removing directories..."
    find "${directory_path_to_clean}" -type d \( -name "node_modules" -o -name "dist" -o -name "build" -o -name ".turbo" -o -name "logs" -o -name "__pycache__" -o -name "venv" -o -name ".DS_Store" \) -exec bash -c 'remove_item "$0"' {} \;
    echo ""
    echo "Removing files..."
    find "${directory_path_to_clean}" -type f \( -name ".DS_Store" \) -exec bash -c 'remove_item "$0"' {} \;
    if [ "${remove_envs}" = "true" ]; then
        echo ""
        echo "Removing .env files..."
        find "${directory_path_to_clean}" -type f \( -name ".env" -o -name "*.bak" -o -name "*.log" \) -exec bash -c 'remove_item "$0"' {} \;
    fi
    if [ "${debug}" = "true" ]; then
        echo ""
        echo "clean_directory() completed"
        echo "Press [Enter] key to review directories/files were removed completely, or 'c' to continue [FTP-020]"
        read user_response
        if [ "${user_response}" != "c" ]; then
            echo ""
            echo "POST: ls -lar \"${directory_path_to_clean}\" | less"
            echo ""
            ls -laR "${directory_path_to_clean}" | less
            echo ""
            echo "Press [Enter] key to confirm directories/files were removed completely [FTP-030]"
            read
        fi
    fi
}

if [ "$1" = "" ] || [ "$2" = "" ]; then
    show_help
fi

debug="$3"
if [ "$debug" = "" ]; then
    debug="true"
fi

# Export functions to be used in find --exec commands
export -f show_dir
export -f show_file
export -f remove_item

clean_directory "$1" "$2" "$debug"
