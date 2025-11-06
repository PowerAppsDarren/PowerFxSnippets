#!/bin/bash

# VS Code Update Script for Kubuntu
# This script updates Visual Studio Code to the latest version

set -e

echo "🔍 Checking current VS Code version..."
if command -v code &> /dev/null; then
    CURRENT_VERSION=$(code --version | head -n1)
    echo "Current version: $CURRENT_VERSION"
else
    echo "VS Code not found in PATH"
fi

echo ""
echo "🔄 Updating VS Code..."
echo ""

# Check if VS Code was installed via apt/deb
if dpkg -l | grep -q "code"; then
    echo "VS Code installed via apt/deb package"
    echo "Updating package lists..."
    sudo apt update

    echo "Upgrading VS Code..."
    sudo apt upgrade code -y

elif flatpak list | grep -q "com.visualstudio.code"; then
    echo "VS Code installed via Flatpak"
    echo "Updating Flatpak packages..."
    flatpak update com.visualstudio.code -y

elif snap list 2>/dev/null | grep -q "code"; then
    echo "VS Code installed via Snap"
    echo "Updating Snap packages..."
    sudo snap refresh code

else
    echo "⚠️  Could not determine VS Code installation method"
    echo ""
    echo "Please choose installation method:"
    echo "1) apt/deb (recommended for Kubuntu)"
    echo "2) Flatpak"
    echo "3) Snap"
    read -p "Enter choice (1-3): " choice

    case $choice in
        1)
            echo "Updating via apt..."
            sudo apt update
            sudo apt upgrade code -y
            ;;
        2)
            echo "Updating via Flatpak..."
            flatpak update com.visualstudio.code -y
            ;;
        3)
            echo "Updating via Snap..."
            sudo snap refresh code
            ;;
        *)
            echo "Invalid choice. Exiting."
            exit 1
            ;;
    esac
fi

echo ""
echo "✅ Update complete!"
echo ""

if command -v code &> /dev/null; then
    NEW_VERSION=$(code --version | head -n1)
    echo "Updated version: $NEW_VERSION"
fi
