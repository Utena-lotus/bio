input_path = "/Users/ngc7293/kisohai/bases_pileup.txt"
output_path = "/Users/ngc7293/kisohai/pickup_bases100.txt"

with open(output_path, "w") as output_file:

    with open(input_path, "r") as input_file:
        line = input_file.readline().rstrip("\r\n")

        reads_list = []

        while line:

            if line == "#":
                if len(reads_list) == 12:
                    reads_list.append(line + "\n")
                    reads_str = "".join(reads_list)
                    output_file.write(reads_str)

                reads_list = []
                line = input_file.readline().rstrip("\r\n")
                continue

            else:
                reads_list.append(line + '\n')
                line = input_file.readline().rstrip("\r\n")
                continue
