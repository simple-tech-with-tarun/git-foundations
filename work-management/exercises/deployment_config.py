deployment_config = {
    "application": "payment-service",
    "environment": "development",
    "region": "central-india",
    "replicas": 2,
}


def get_application_name():
    return deployment_config["application"]


def get_deployment_config():
    return deployment_config


def get_deployment_summary():
    return "Production deployment configuration"


def is_production_deployment():
    return deployment_config["environment"] == "production"


def get_deployment_region():
    return deployment_config["region"]
