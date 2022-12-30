import json
import os
from typing import List
from config import TerraformConfig
from parser.resolvers import ConditionalResolver, ConstantResolver
from resolvers import FunctionLayerResolver, LocalsResolver
from pathlib import Path

class ConfigBuilder:
    layer_resolvers: List[FunctionLayerResolver]
    config: TerraformConfig
    
    def __init__(self, json_file) -> None:
        tf_dict = self._read_json(json_file)
        self.config = TerraformConfig(tf_json=tf_dict)
        self.config.load()
        self.layer_resolvers = [
            LocalsResolver,
            ConstantResolver,
            ConditionalResolver,
        ]

    def build(self) -> TerraformConfig:
        self._resolve_function_layers()
        return self.config
     
    def _resolve_function_layers(self):
        lambda_functions = self.config.resources.get("aws_lambda_function", {})
        for name, value in lambda_functions.items():
            for resolver in self.layer_resolvers:
                resolver.resolve(value, self.config)
            self.config.resolved_functions[name] = value
    
    def _read_json(self, json_file):
        with open(Path(os.getcwd(), json_file)) as f:
            return json.load(f)
