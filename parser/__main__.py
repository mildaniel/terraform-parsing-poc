from config_builder import ConfigBuilder
from hcl2json import convert

TEST_IN = ""
TEST_OUT = "sample.json"


def main():
    convert(TEST_IN, TEST_OUT)
    graph = ConfigBuilder(TEST_OUT).build()
    print(graph.resolved_functions)


if __name__ == "__main__":
    main()
