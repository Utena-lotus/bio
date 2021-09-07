id = ["ERR001702.1411297", "ERR001702.5801919", "ERR001702.5703036", "ERR001702.1928118", "ERR001702.2342962"]

with open(path2, "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for line in reader:
        if any(x in line for x in id):
            print(line)
            bases = line[9]
            start_pos = int(line[3])
            end_pos = start_pos + 35
            left_pos = variant_pos - 18
            right_pos = variant_pos + 18
            if start_pos <= left_pos:
                num_pos = left_pos - start_pos
                num_brank = right_pos -end_pos
                app_bases = bases[num_pos:] + ("-" * num_brank)
                print(app_bases)
            else:
                num_pos = end_pos - right_pos
                num_brank = start_pos -left_pos
                app_bases = ("-" * num_brank) + bases[:-num_pos]
                print(app_bases)
