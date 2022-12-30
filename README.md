# terraform-parsing-poc

This repository demonstrates a small example of how to use hcl2json to parse a Terraform project and extract data like locals and constanst that are not resolved by `terraform plan` today.

### Running this project
1. Clone the repository
2. Update the `INPUT` constant `parser/__main__.py` with a path to a sample Terraform file
3. Run `python parser`

It will print the resolved Lambda Functions to the console.

Sample output demonstrating locals resolution for a Lambda Function

```
{'function1': [{'depends_on': ['${null_resource.sam_metadata_aws_lambda_function1}'], 'function_name': '${var.namespace}-function1-${random_uuid.s3_bucket.result}', 'handler': 'app.lambda_handler', 'layers': ['aws_lambda_layer_version.layer1.arn'], 'role': '${aws_iam_role.iam_for_lambda.arn}', 'runtime': 'python3.8', 's3_bucket': '${aws_s3_bucket.lambda_code_bucket.bucket}', 's3_key': '${aws_s3_object.lambda_function_code.key}', 'timeout': 300}]}
```


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

