import os

__version__ = "0.8.7"
__build__ = os.environ.get('GITHUB_SHA', '')[:7] if os.environ.get('GITHUB_SHA') else None
