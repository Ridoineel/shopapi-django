from os import path
from .utils.functions import generateModuleImportInit



BASE_DIR = path.dirname((path.dirname(__file__)))
modules_path = {
    path.join(BASE_DIR, "accounts", "models"),
    path.join(BASE_DIR, "accounts", "serializers"),
    path.join(BASE_DIR, "accounts", "views"),
    path.join(BASE_DIR, "boutique", "models"),
    path.join(BASE_DIR, "boutique", "serializers"),
    path.join(BASE_DIR, "boutique", "views"),
    path.join(BASE_DIR, "payment", "models"),
    path.join(BASE_DIR, "payment", "serializers"),
    path.join(BASE_DIR, "payment", "views")
}

for d in modules_path:
    generateModuleImportInit(d)