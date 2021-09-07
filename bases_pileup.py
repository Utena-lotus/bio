import csv
import distance
from time import sleep

def uniformize(variant_pos, start_pos):
    reads = []
    for ran_start_pos in range(start_pos-5, start_pos+6):

        end_pos = ran_start_pos + 35
        left_pos = variant_pos - 18
        right_pos = variant_pos + 18

        # 左側がはみ出す場合
        if start_pos <= left_pos:
            num_pos = left_pos - ran_start_pos
            num_blank = right_pos - end_pos
            # 右側の足りない部分を-で埋める
            arr_bases = bases[num_pos:] + ("-" * num_blank)
            if len(arr_bases) == 37:
                reads.append(arr_bases)
        # 右側がはみ出す場合
        else:
            num_pos = end_pos - right_pos
            num_blank = ran_start_pos - left_pos
            # 左側の足りない部分を-で埋める
            arr_bases = ("-" * num_blank) + bases[:-num_pos]
            if len(arr_bases) == 37:
                reads.append(arr_bases)
    return reads

bed_path = "/Users/ngc7293/kisohai/BED/ALL.chr20.NA12878.ERR001702.filt.map.l36.srt.hg38.arr.c10.wb.ran10.bed"
sam_path = "/Users/ngc7293/kisohai/SAM/ERR001702.filt.sam"
fa_path = "/Users/ngc7293/kisohai/FASTA/Homo_sapiens.GRCh38.dna.chromosome.20.arr.fa"
output_path = "/Users/ngc7293/kisohai/bases_pileup"

with open(output_path, "w") as output_file:

    with open(fa_path, "r") as fa_file:
        ref_bases = fa_file.read()

        with open(bed_path, "r") as bed_file:
            bed_reader = csv.reader(bed_file, delimiter="\t")
            # 今相対的に見て何行目かを数えるカウンター
            counter = 10
            id = []
            level = 0

            # メインデータの読み込み
            for line in bed_reader:
                if counter > 0:
                    # 変異のある場所の数字を取得
                    variant_pos = int(line[2])
                    kind_of_variant = line[8]
                    # リファレンスの左端と右端を指定
                    ref_left_pos = variant_pos - 18 - 1
                    ref_right_pos = variant_pos + 18
                    # 変異が入る塩基
                    variant = ref_bases[variant_pos - 1]
                    # idを取得
                    id.append(line[13])
                    # カウントダウン
                    # counterが0になったらここまでのidでpileupを作る
                    counter -= 1

                else:
                    # print(kind_of_variant)
                    output_file.write(kind_of_variant + "\n")
                    ref_reads = ref_bases[ref_left_pos:ref_right_pos]
                    # print(ref_reads)
                    output_file.write(ref_reads + "\n")
                    with open(sam_path, "r") as sam_file:
                        sam_reader = csv.reader(sam_file, delimiter="\t")
                        # メインデータの読み込み
                        for li in sam_reader:
                            # idの中のどれか１つでも一致するものがあるか
                            if any(x in li[0] for x in id):
                                # print(li)
                                # 定義
                                bases = li[9]
                                start_pos = int(li[3])
                                # reads = []
                                hamming_distance = []

                                reads = uniformize(variant_pos, start_pos)

                                for i in range(len(reads)):
                                    hamming_distance.append(distance.hamming(ref_reads, reads[i]))

                                if hamming_distance:
                                    # print(reads[hamming_distance.index(min(hamming_distance))])
                                    output_file.write(reads[hamming_distance.index(min(hamming_distance))] + "\n")

                                reads = []
                                hamming_distance = []

                        # 10行づつでダミー行を作る
                        # print("#")
                        output_file.write("#" + "\n")
                        level += 1
                        print('\r' + str(level), end='')
                        # 重たい処理
                        sleep(1)
                        # カウンターとidをセットし直す
                        counter = 10
                        id = []