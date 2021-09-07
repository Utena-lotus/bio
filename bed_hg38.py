import csv

path = "/Users/ngc7293/kisohai/BED/ALL.chr20.NA12878.bed6.hg38.bed"
path2 = "/Users/ngc7293/kisohai/BED/ALL.chr20.NA12878.bed"
new_file_path = "/Users/ngc7293/kisohai/BED/ALL.chr20.NA12878.hg38.bed"

with open(new_file_path, "w") as new_bed_file:
    writer = csv.writer(new_bed_file, delimiter="\t")

    with open(path, "r") as bed_file:
        reader = csv.reader(bed_file, delimiter="\t")
        for line in reader:
            li = line[0:5]
            id = line[3]

            with open(path2, "r") as bed_file2:
                reader2 = csv.reader(bed_file2, delimiter="\t")
                for line2 in reader2:
                    if id in line2[3]:
                        new_line = li + line2[5:]
                        writer.writerow(new_line)
