deployment_override = {
    "environment": "staging",
    "replicas": 1,
}


def get_override_environment():
    return deployment_override["environment"]
