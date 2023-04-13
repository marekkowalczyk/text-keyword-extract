import yaml
import os

# Config info

config_folder="/Users/marekkowalczyk/repos/audio-transcribe/config/"
filename_keys="keys.yaml"

# TODO Put config info in a config file

file_path_keys = os.path.join(config_folder, filename_keys)

# Get API key

def get_api_key_value(api_key_name):
    with open(file_path_keys, 'r') as f:
        data = yaml.safe_load(f)
        for key in data:
            if key['api_key']['api_key_name'] == api_key_name:
                return key['api_key']['api_key_value']
