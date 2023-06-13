#!/bin/sh
APPS="users educators departments faculties rating educator_rating"
EXCLUDE_MODELS="AbstractUser,Group,Permission"
python manage.py graph_models $APPS --exclude-models=$EXCLUDE_MODELS  -o schema.dot --dot