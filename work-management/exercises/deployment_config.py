deployment_config = {
    "application": "payment-service",
    "environment": "development",
    "region": "central-india",
    "replicas": 2,
}


def get_application_name():
    return f"Application: {deployment_config['application']}"


def get_deployment_config():
    return deployment_config


def get_deployment_summary():
    return "Deployment summary for payment-service"


def is_production_deployment():
    return deployment_config["environment"] == "production"


def get_deployment_region():
    return f"Deployment region: {deployment_config['region']}"


def get_deployment_notes_file():
    return "deployment_notes.txt"
