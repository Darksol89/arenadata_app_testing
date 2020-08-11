"""Special methods for Test application api working"""
import requests
import allure


class Api:
    def __init__(self, base_url):
        """Initializing base url"""
        self.base_url = base_url

    @allure.step('upload template')
    def upload_template(self, template_file, tmpl_id=None):
        """Upload template with PUT request"""
        return requests.put(f'{self.base_url}/api/v1/templates',
                            data={'tmpl_id': f'{tmpl_id}'},
                            files={'file': open(f'{template_file}')})

    @allure.step('install template')
    def install_template(self, template):
        """Install previously loaded template file with POST request"""
        return requests.post(f'{self.base_url}/api/v1/templates/{template}/install')

    @allure.step('delete template')
    def delete_template(self, template):
        """Delete previously loaded template file with DELETE request"""
        return requests.delete(f'{self.base_url}/api/v1/templates/{template}')

    @allure.step('list of templates')
    def list_template(self):
        """List all currently uploaded templates with GET request"""
        return requests.get(f'{self.base_url}/api/v1/templates')

    @allure.step('get info from resource')
    def get_information_from_resource(self):
        """Get information from tesitng resource"""
        return requests.get(f'{self.base_url}')