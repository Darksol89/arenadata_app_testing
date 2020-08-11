import pytest
import allure


@allure.title('Delete uploaded template')
@pytest.mark.parametrize('template_file', ['google_template.yml'])
def test_delete_template(api_client, get_template_directory, template_file):
    api_client.upload_template(template_file=template_file)
    template_name = template_file.split(sep='.')
    responce = api_client.delete_template(template=template_name[0])
    responce_get = api_client.list_template()

    assert responce.ok
    assert f'Template with tmpl_id={template_name[0]} successfully deleted!' in responce.text
    assert template_name[0] not in responce_get.json()
