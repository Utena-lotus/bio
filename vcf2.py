import csv

path = "/Users/ngc7293/kisohai/VCF/ALL.chr20.NA12878.vcf"
path2 = "/Users/ngc7293/kisohai/VCF/ALL.chr20.NA12878.slct.vcf"

with open(path2, "w") as vcf_file2:
    writer = csv.writer(vcf_file2, delimiter="\t")

    with open(path, "r") as vcf_file:
        reader = csv.reader(vcf_file, delimiter="\t")
        for line in reader:
            if not "0|0" in line[9]:
                writer.writerow(line)
