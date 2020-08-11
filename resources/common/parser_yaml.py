"""Parser YAML files and getting some info"""
import yaml

def get_button_text(file_template, btn_param):
    with open(file_template) as tmpl_file:
        file_info = yaml.safe_load(tmpl_file)
    value = file_info[0].get(btn_param)

    return value

