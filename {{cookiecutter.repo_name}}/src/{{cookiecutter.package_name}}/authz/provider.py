from bami_chassis.security.authz.casbin_provider import CasbinProvider
from importlib import resources


def service_enforcer_provider():
    pkg = "{{cookiecutter.package_name}}.resources.authz"
    with resources.as_file(resources.files(pkg) / "policy.csv") as p:
        return CasbinProvider(policy_path=str(p))
