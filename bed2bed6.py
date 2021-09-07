import csv

path = "/Users/ngc7293/kisohai/BED/ERR001702.filt.map.l36.srt.bed"
path2 = "/Users/ngc7293/kisohai/BED/ERR001702.filt.map.l36.srt.bed6.bed"

with open(path2, "w") as bed_file2:
    writer = csv.writer(bed_file2, delimiter="\t")

    with open(path, "r") as bed_file:
        reader = csv.reader(bed_file, delimiter="\t")

        for line in reader:
            li = ["chr20"] + line[1:5]
            writer.writerow(li)
