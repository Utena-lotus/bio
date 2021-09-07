import csv
import gzip

person_id = "NA12812"

path = "/Users/ngc7293/kisohai/VCF/ALL.chr20.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz"
path2 = "/Users/ngc7293/kisohai/VCF/ALL.chr20.NA12812.vcf"

with open(path2, "w") as vcf_file2:
    writer = csv.writer(vcf_file2, delimiter="\t")

    with gzip.open(path, "rt", "utf_8") as vcf_file:
        reader = csv.reader(vcf_file, delimiter="\t")

        # person_idがある行でperson_idが何列目か求める
        for line in reader:
            if '#' in line[0]:
                if person_id in line:
                    index = line.index(person_id)
                    li = line[0:9]
                    li.append(line[index])
                    writer.writerow(li)
            # person_idの列のみ取り出す
            else:
                li = line[0:9]
                li.append(line[index])
                writer.writerow(li)
