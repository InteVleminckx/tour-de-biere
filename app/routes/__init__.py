import importlib
import pkgutil
from flask import Blueprint

def discover_blueprints():
    blueprints = []

    # Import all modules in the current package
    package_name = __name__
    package = importlib.import_module(package_name)

    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"{package_name}.{module_name}")

        # Find variables that are Blueprint instances
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, Blueprint):
                blueprints.append(attr)

    return blueprints
