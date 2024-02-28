from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.yaml", "/project/config/config.yaml"],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.


firebase_config = {
    "apiKey": settings.get("API_KEY"),
    "authDomain": settings.get("AUTH_DOMAIN"),
    "projectId": settings.get("PROJECT_ID"),
    "storageBucket": settings.get("STORAGE_BUCKET"),
    "messagingSenderId": settings.get("MESSAGING_SENDER_ID"),
    "appId": settings.get("APP_ID"),
    "measurementId": settings.get("measurementId"),
}
