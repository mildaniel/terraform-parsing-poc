import subprocess


def convert(input_filename, output_filname):
    with open(output_filname, "w") as f:
        subprocess.run(["hcl2json", input_filename], stdout=f)
