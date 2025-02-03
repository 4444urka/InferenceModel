import os
import yaml

class Config:
    def __init__(self, env: str):
        self.env = env

def load_config_by_path(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError("config file not found: " + path)

    with open(path, "r") as f:
        data = yaml.safe_load(f)

    env = data.get("env", "local")

    return Config(env)