#!/usr/bin/python3
# __init__.py
"""Create Unique File storage instance"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
