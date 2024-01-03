import os
from dotenv import load_dotenv
import pylint_django

# Load environment variables from .env
load_dotenv()

# Set PYTHONPATH
os.environ['PYTHONPATH'] = os.getenv('PYTHONPATH', '')
print("PYTHONPATH: ",os.getenv('PYTHONPATH', '') );


def initialize():
    pylint_django.settings.django_settings() # type: ignore
