"""Testing of install different templates"""
import pytest
import allure
import yaml


@allure.title('Install uploaded template with all fields')
@pytest.mark.parametrize('template_file', ['template_all_field.yml'])
def test_install_template(api_client, get_template_directory, template_file):
    api_client.upload_template(template_file=template_file)
    template_name = template_file.split(sep='.')
    responce = api_client.install_template(template=template_name[0])

    assert responce.ok
    assert f'Template with tmpl_id={template_name[0]} successfully installed!' in responce.text


@allure.title('Install uploaded template with custom tmpl_id')
@pytest.mark.parametrize('template_file', ['template_all_field.yml'])
@pytest.mark.parametrize('tmpl_id', ['test_google_01'])
def test_install_template_with_custom_tmpl_id(api_client, get_template_directory, template_file, tmpl_id):
    api_client.upload_template(template_file=template_file, tmpl_id=tmpl_id)
    responce = api_client.install_template(template=tmpl_id)

    assert responce.ok
    assert f'Template with tmpl_id={tmpl_id} successfully installed!' in responce.text


@allure.title('Install not exist template')
@pytest.mark.parametrize('random_template_name', ['Test_template'])
def test_install_not_exist_template(api_client, get_template_directory, random_template_name):
    responce = api_client.install_template(template=random_template_name)

    assert not responce.ok
    assert f'No template with tmpl_id={random_template_name} found!' in responce.text


@allure.title('Install template without label')
@pytest.mark.parametrize('template_file', ['template_no_label.yaml'])
def test_install_template_without_label(api_client, get_template_directory, template_file):
    api_client.upload_template(template_file=template_file)
    template_name = template_file.split(sep='.')
    responce = api_client.install_template(template=template_name[0])

    assert responce.status_code != 200
    assert 'Links without labels are not allowed.' in responce.text


@allure.title('Install template without id')
@pytest.mark.parametrize('template_file', ['template_no_id.yaml'])
def test_install_template_without_id(api_client, get_template_directory, template_file):
    api_client.upload_template(template_file=template_file)
    template_name = template_file.split(sep='.')
    responce = api_client.install_template(template=template_name[0])

    assert responce.status_code != 200
    assert 'No \\"id\\" field' in responce.text


@allure.title('Install template without parent id')
@pytest.mark.parametrize('template_file', ['template_no_parent_id.yml'])
def test_install_template_without_parent_id(api_client, get_template_directory, template_file):
    api_client.upload_template(template_file=template_file)
    template_name = template_file.split(sep='.')
    # Reading YAML file as dictionary
    with open(template_file) as yml_file:
        yaml_dict = yaml.safe_load(yml_file)
    responce = api_client.install_template(template=template_name[0])

    assert responce.status_code != 200
    assert f'Dependency form {yaml_dict[0]} is not presented in template' in responce.text


@allure.title('Install uploaded template with multiple elements')
@pytest.mark.parametrize('template_file', ['template_two_elements.yml'])
def test_install_template_with_multiple_elements(api_client, get_template_directory, template_file):
    api_client.upload_template(template_file=template_file)
    template_name = template_file.split(sep='.')
    responce = api_client.install_template(template=template_name[0])

    assert responce.ok
    assert f'Template with tmpl_id={template_name[0]} successfully installed!' in responce.text


@allure.title('Install template with wrong structure')
@pytest.mark.parametrize('template_file', ['wrong_template.yml'])
def test_install_template_with_wrong_structure(api_client, get_template_directory, template_file):
    api_client.upload_template(template_file=template_file)
    template_name = template_file.split(sep='.')
    responce = api_client.install_template(template_name[0])

    assert responce.status_code != 201
    assert "Invalid template format!" in responce.text
