#!/usr/bin/env python3

#
# config.py
# Load configuration from file or environment variables
#

from dynaconf import Dynaconf
from os.path import join, abspath, exists


config_files = ["config.yaml", ".secrets.yaml"]
config_files = [abspath(join(__file__, "../../config/", f)) for f in config_files]

for f in config_files:
    assert exists(f)

settings = Dynaconf(
    environments=True, envvar_prefix="OTTO", settings_files=config_files
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load this files in the order.
