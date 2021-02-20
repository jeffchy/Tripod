from .example_configs import example_env_config, example_config_config
import json

def check_experiment_settings(config):
    error = ''

    try:
        config = dict(config)
    except:
        error = "Not a valid dict."
    else:
        invalid_keys = []
        for key in config.keys():
            if key not in example_env_config:
                invalid_keys.append(key)
        if len(invalid_keys) > 0:
            error += "Invalid keys: {}. \n".format(','.join(invalid_keys))

        not_appear_keys = []
        for key in example_env_config.keys():
            if key not in config:
                not_appear_keys.append(key)
        if len(not_appear_keys) > 0:
            error += "Not appear keys: {}. \n".format(','.join(not_appear_keys))

        if len(not_appear_keys) > 0 or len(invalid_keys) > 0:
            error += "Should have keys: {}. \n".format(example_env_config.keys())

    return error


def check_config_settings(config):
    error = ''

    try:
        config = config.replace("'", '"')
        config = json.loads(config)
    except:
        error = "Not a valid dict. "

    return error