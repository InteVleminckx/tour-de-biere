import importlib
import pkgutil
from flask import Blueprint


def discover_blueprints(package_name="app.routes"):
    blueprints = []

    def walk_modules(package):
        for finder, name, is_pkg in pkgutil.iter_modules(package.__path__, package.__name__ + "."):
            module = importlib.import_module(name)

            # Collect blueprints in the current module
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, Blueprint) and attr not in blueprints:
                    blueprints.append(attr)

            if is_pkg:
                walk_modules(module)

    root_package = importlib.import_module(package_name)
    walk_modules(root_package)

    return blueprints