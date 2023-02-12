import os

from hale_sec.core.config import Config

config = Config()

broker_url = f"redis://user:{config.redis_password}@{config.redis_host}:{config.redis_port}/0"
result_backend = broker_url
task_serializer = "pickle"
result_serializer = "pickle"
accept_content = ["pickle", "json"]
result_expires = 60
worker_hijack_root_logger = False
worker_redirect_stdouts = False
worker_log_color = None
task_routes = {

}

# TODO - I don't like this solution but had to do it to reduce dependancies per service
# It allows us to only import the tasks we need for a specific worker
if os.getenv("CELERY_IMPORTS", None):
    imports = tuple(os.getenv("CELERY_IMPORTS").split(","))
