#!/home/z7zyi2hwe9l8/.local/bin/python3.8
from wsgiref.handlers import CGIHandler
import os
sys.path.insert(0, '/home/z7zyi2hwe9l8/public_html/website/')
from __init__ import app

if __name__ == "__main__":
    CGIHandler().run(app)