import csv

path = "/Users/ngc7293/kisohai/SAM/ERR001702.filt.sam"
path2 = "/Users/ngc7293/kisohai/SAM/ERR001702.filt.arr.sam"

with open(path2, "w") as bed_file2:
    writer = csv.writer(bed_file2, delimiter="\t")

    with open(path, "r") as bed_file:
        reader = csv.reader(bed_file, delimiter="\t")

        for line in reader:
            if "20" in line[2]:
                writer.writerow(line)