from app.config.config import config

DB_CONFIG = {
    "connections":
        {
            "default": config.POSTGRES_URL
        },
    "apps":
        {
            "models": {
                "models":
                    [
                        "app.models.users",
                        "aerich.models"     # aierich.models for aerich support
                    ],
                "default_connection": "default"
            }
        }
}
