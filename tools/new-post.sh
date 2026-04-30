#!/usr/bin/env bash
#
# Create a new post with pre-filled front matter.
#
# Usage: bash tools/new-post.sh "Post Title"

set -eu

POSTS_DIR="_posts"

help() {
  echo "Create a new post with pre-filled front matter."
  echo
  echo "Usage:"
  echo
  echo "   bash $0 <title>"
  echo
  echo "Arguments:"
  echo "     <title>    The title of the post (in quotes if it contains spaces)."
  echo
  echo "Options:"
  echo "     -h, --help    Print this help information."
}

if [[ $# -eq 0 ]]; then
  echo "Error: No title provided."
  help
  exit 1
fi

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
  help
  exit 0
fi

# Generate a URL-friendly slug from the title.
slugify() {
  echo "$1" \
    | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/[^a-z0-9]+/-/g; s/^-//; s/-$//'
}

title="$1"
date="$(date +%Y-%m-%d)"
slug="$(slugify "$title")"
filename="${POSTS_DIR}/${date}-${slug}.md"

if [[ -f "$filename" ]]; then
  echo "Error: A post already exists for today with a similar title."
  echo "  File: $filename"
  exit 1
fi

# Ensure the _posts directory exists.
mkdir -p "$POSTS_DIR"

# Create the post with front matter.
cat > "$filename" <<EOF
---
title: "${title}"
date: ${date}
categories: []
tags: []
---
EOF

# Open in editor if set, otherwise print the path.
if [[ -n "${EDITOR:-}" ]]; then
  ${EDITOR} "$filename"
else
  echo "Post created: $filename"
fi
