#!/bin/bash

# --------------------------------------------------
# Odoo Docker Database Backup & Restore Script
# --------------------------------------------------
# Usage:
#   ./db_backup_restore.sh backup   -> creates backup
#   ./db_backup_restore.sh restore  -> restores latest backup
# --------------------------------------------------

# Configuration
COMPOSE_FILE=".devcontainer/docker-compose.yml"
DB_CONTAINER="db"
DB_NAME="postgres"
DB_USER="odoo"
BACKUP_DIR="$HOME/odoo_backups"

# Create backup directory if not exists
mkdir -p "$BACKUP_DIR"

# Timestamp for backup filenames
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/odoo_postgres_backup_$TIMESTAMP.sql.gz"

# Command based on argument
case "$1" in
  backup)
    echo "Backing up database '$DB_NAME' from container '$DB_CONTAINER'..."
    docker compose -f "$COMPOSE_FILE" exec -T "$DB_CONTAINER" pg_dump -U "$DB_USER" "$DB_NAME" | gzip > "$BACKUP_FILE"
    echo "Backup completed: $BACKUP_FILE"
    ;;

  restore)
    # Get the latest backup file
    LATEST_BACKUP=$(ls -t $BACKUP_DIR/odoo_postgres_backup_*.sql.gz | head -n1)
    if [[ -z "$LATEST_BACKUP" ]]; then
      echo "No backup found in $BACKUP_DIR"
      exit 1
    fi
    echo "Restoring database '$DB_NAME' from $LATEST_BACKUP..."
    gunzip -c "$LATEST_BACKUP" | docker compose -f "$COMPOSE_FILE" exec -T "$DB_CONTAINER" psql -U "$DB_USER" "$DB_NAME"
    echo "Restore completed."
    ;;

  *)
    echo "Usage: $0 {backup|restore}"
    exit 1
    ;;
esac
