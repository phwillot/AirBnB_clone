#!/usr/bin/python3
"""This is the Init module"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
