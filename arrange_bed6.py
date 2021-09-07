import csv

path = "/Users/ngc7293/kisohai/BED/ALL.chr20.NA12878.hg38.bed"
path2 = "/Users/ngc7293/kisohai/BED/ALL.chr20.NA12878.hg38.arr.bed"

with open(path2, "w") as bed_file2:
    writer = csv.writer(bed_file2, delimiter="\t")

    with open(path, "r") as bed_file:
        reader = csv.reader(bed_file, delimiter="\t")

        for line in reader:
            info = line[3]
            li = line + info.split("_")
            writer.writerow(li)