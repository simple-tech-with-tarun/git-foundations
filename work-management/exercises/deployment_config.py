deployment_config = {
    "application": "payment-service",
    "environment": "development",
    "region": "central-india",
    "replicas": 2,
}


def get_deployment_config():
    return deployment_config


def get_deployment_summary():
    return "Production deployment configuration"
