input_path = "/Users/ngc7293/kisohai/bases_pileup.txt"
output_path = "/Users/ngc7293/kisohai/pickup_bases.txt"

with open(output_path, "w") as output_file:

    with open(input_path, "r") as input_file:
        line = input_file.readline().rstrip("\r\n")

        reads_list = []
        variant_type = None
        cnt = -2

        while line:

            if line == "0|0":
                reads_list.append(line + "\n")
                line = input_file.readline().rstrip("\r\n")
                variant_type = "Nothing"
                continue

            if line == ("1|0" or "0|1" or "1|1" or "2|0" or "0|2"):
                reads_list.append(line + "\n")
                line = input_file.readline().rstrip("\r\n")
                variant_type = "variant"
                continue

            elif line == "#":
                if len(reads_list) == 12:
                    if cnt < 50 or variant_type == "variant":
                        cnt += 1
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
