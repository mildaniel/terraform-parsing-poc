from typing import Dict


class TerraformConfig:
    tf_json: Dict
    locals: Dict
    variables: Dict
    resources: Dict
    resolved_functions: Dict

    def __init__(self, tf_json) -> None:
        self.tf_json = tf_json
        self.resolved_functions = {}

    def load(self):
        self.locals = self._read_locals()
        self.resources = self._read_resources()

    def _read_locals(self):
        return self.tf_json.get("locals", [])[0]

    def _read_resources(self):
        return self.tf_json.get("resource", {})
