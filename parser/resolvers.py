from abc import ABC

from config import TerraformConfig
from typing import Dict


class FunctionLayerResolver(ABC):
    def resolve(lambda_function: Dict, config: TerraformConfig) -> None:
        raise NotImplementedError()


class LocalsResolver(FunctionLayerResolver):
    def resolve(lambda_function: Dict, config: TerraformConfig) -> None:
        layers = lambda_function[0].get("layers", [])
        for index, layer in enumerate(layers):
            if _check_dynamic_value(layer):
                layer = _strip_dynamic_value(layer)
                if layer.startswith("local."):
                    layer = config.locals.get(layer.split(".")[-1])
                    if _check_dynamic_value(layer):
                        layer = _strip_dynamic_value(layer)
                    layers[index] = layer
        

class ConstantResolver(FunctionLayerResolver):
    def resolve(lambda_function: Dict, config: TerraformConfig) -> None:
        ""


class ConditionalResolver(FunctionLayerResolver):
    def resolve(lambda_function: Dict, config: TerraformConfig) -> None:
        ""


def _check_dynamic_value(value: str) -> bool:
    return value.startswith("${") and value.endswith("}")


def _strip_dynamic_value(value: str) -> str:
    return value[2:-1]
