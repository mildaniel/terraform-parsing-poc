# terraform-parsing-poc

This repository demonstrates a small example of how to use hcl2json to parse a Terraform project and extract data like locals and constanst that are not resolved by `terraform plan` today.

### Running this project
1. Clone the repository
2. Update the `INPUT` constant `parser/__main__.py` with a path to a sample Terraform file
3. Run `python parser`

It will print the resolved Lambda Functions to the console.

### File breakdown

#### sample.json

A sample converted output from HCL to JSON

#### parser/__main__.py

Entrypoint that calls the ConfiguBuilder and prints the resolved functions

#### parser/config.py

Terraform configuration object definiton.

#### parser/config_builder.py

Creates the TerraformConfig, resolves it then returns the resolved version

#### parser/resolvers.py

Resolver definition and concrete resolvers. These resolvers take a lambda function and config, and then update the function as necessary. Used by the ConfigBuilder to create the Config instance.

#### parser/converter.py

Uses a subprocess to call hcl2json and convert the Terraform file to JSON

