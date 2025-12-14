#!/bin/bash
BACKUP_DIR="/var/backups/postgres"
LATEST=$(ls -t $BACKUP_DIR | head -n1)

if [ -z "$LATEST" ]; then
  echo "No backups found"
  exit 1
fi

echo "Latest backup: $LATEST"
