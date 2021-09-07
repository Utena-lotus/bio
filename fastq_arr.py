path = "/Users/ngc7293/kisohai/FASTA/Homo_sapiens.GRCh38.dna.chromosome.20.fa"
path2 = "/Users/ngc7293/kisohai/FASTA/Homo_sapiens.GRCh38.dna.chromosome.20.arr.fa"


with open(path2, "w") as bed_file2:

    with open(path, "r") as bed_file:
        next(bed_file)

        reader = bed_file.read()

        bases = reader.replace("\n", "")
        bases = bases.replace("\r", "")

        bed_file2.write(bases)
