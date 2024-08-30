import yaml
import os


class YamlHandler:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_yaml(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"文件 {self.filepath} 不存在")

        with open(self.filepath, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)

    def write_yaml(self, data):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

        with open(self.filepath, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, allow_unicode=True, default_flow_style=False)

    def clear_yaml(self):
        self.write_yaml({})
