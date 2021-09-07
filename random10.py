import random
import csv

path = "/Users/ngc7293/kisohai/BED/ALL.chr20.NA12878.ERR001702.filt.map.l36.srt.hg38.arr.c10.wb.bed"
path2 = "/Users/ngc7293/kisohai/BED/ALL.chr20.NA12878.ERR001702.filt.map.l36.srt.hg38.arr.c10.wb.ran10.bed"
random_index = 9

with open(path2, "w") as f2:
    writer = csv.writer(f2, delimiter="\t")

    with open(path, "r") as f:
        reader = csv.reader(f, delimiter="\t")

        # 今相対的に見て何行目かを数えるカウンター
        counter = 0

        # メインデータの読み込み
        for line in reader:
            if counter <= 0:
                # 何行目までをランダムサンプルの対象とするか情報取得
                n = int(line[random_index])

                # 今のところからn行までのうち、何行目を取得するのか決める
                target = list(range(n))
                sample = random.sample(target, 10)

                # カウンターをセット
                counter = n

                # もしsample対象と選ばれていたら抽出
            if n - counter in sample:
                # csvに書き出しなど行う
                writer.writerow(line)

            # カウントダウン
            # counterが0以下になったら、
            # random対象区間が切り替わったということなので、
            # 再度サンプリング対象の選定を行う
            counter -= 1
