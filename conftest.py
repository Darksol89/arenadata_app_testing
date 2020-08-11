import pytest
import requests
import os
from utils.api import Api


def pytest_addoption(parser):
    """Parser for command0line parameters"""
    parser.addoption('--url',
                     action='store',
                     default='http://localhost:5000',
                     help='Target link for request')
    parser.addoption('--template_dir',
                     action='store',
                     default='D:\\PyCharm_projects\\Arenadata_task\\templates',
                     help='Directory with templates for tests')


@pytest.fixture()
def api_client(request):
    """Get url for tests"""
    base_url = request.config.getoption('--url')
    return Api(base_url)


@pytest.fixture()
def get_template_directory(request):
    """Get working directory with templates"""
    template_directory = request.config.getoption('--template_dir')
    os.chdir(template_directory)
    return template_directory



