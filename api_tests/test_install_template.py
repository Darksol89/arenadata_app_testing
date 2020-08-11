"""Testing of install different templates"""
import pytest
import allure


@allure.title('Install uploaded template')
@pytest.mark.parametrize('template_file', ['google_template.yml'])
def test_install_template(api_client, get_template_directory, template_file):
    api_client.upload_template(template_file=template_file)
    template_name = template_file.split(sep='.')
    responce = api_client.install_template(template=template_name[0])

    assert responce.ok
    assert f'Template with tmpl_id={template_name[0]} successfully installed!' in responce.text


@allure.title('Install not exist template')
@pytest.mark.parametrize('random_template_name', ['Test_template'])
def test_install_not_exist_template(api_client, get_template_directory, random_template_name):
    responce = api_client.install_template(template=random_template_name)

    assert not responce.ok
    assert f'No template with tmpl_id={random_template_name} found!' in responce.text
