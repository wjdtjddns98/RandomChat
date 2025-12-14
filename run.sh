#!/bin/bash

#migrate
echo "Applying database migrations..."
aerich upgrade
echo "Migrations applied successfully."

#uvicorn
echo "Starting uvicorn server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
echo "Server stopped."