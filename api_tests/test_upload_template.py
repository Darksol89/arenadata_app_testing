"""Testing of uploading different templates"""
import pytest
import allure


@allure.title('Upload default template')
@pytest.mark.parametrize('template_file', ['google_template.yml'])
def test_default_upload_template(api_client, get_template_directory, template_file):
    responce = api_client.upload_template(template_file=template_file)

    assert responce.status_code == 201
    assert 'Template successfully uploaded' in responce.text


@allure.title('Upload template with custom template id')
@pytest.mark.parametrize('tmpl_id', ['test_google_01'], ids=['Custom_Template_id'])
@pytest.mark.parametrize('template_file', ['google_template.yml'], ids=['custom_templ_file'])
def test_upload_template_with_custom_params(api_client, get_template_directory, tmpl_id, template_file):
    responce = api_client.upload_template(template_file=template_file, tmpl_id=tmpl_id)

    assert responce.status_code == 201
    assert f'Template successfully uploaded. tmpl_id={tmpl_id}' in responce.text


@allure.title('Upload template with not supported format')
@pytest.mark.parametrize('template_file', ['main.html'])
def test_upload_not_supported_format(api_client, get_template_directory, template_file):
    responce = api_client.upload_template(template_file=template_file)

    assert responce.status_code != 201
    assert "Allowed file types are {\'yaml\', \'yml\'}" in responce.text


@allure.title('Upload not exist template file')
@pytest.mark.parametrize('template_file', ['test.yaml'])
@pytest.mark.xfail
def test_upload_not_exist_file(api_client, get_template_directory, template_file):
    try:
        responce = api_client.upload_template(template_file=template_file)
    except FileNotFoundError:
        raise
