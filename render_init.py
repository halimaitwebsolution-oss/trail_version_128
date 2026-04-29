"""
Database Initialization for Render Deployment
HSC Academic Management System

This script creates all database tables without migration.
Run this in Render build command.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db

def main():
    print("Initializing database for Render...")

    with app.app_context():
        try:
            db.create_all()
            print("✓ Database tables created successfully")
            return True
        except Exception as e:
            print(f"✗ Error creating tables: {e}")
            return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)