import sys
import gzip


def filter_vcf(femalelist, malelist, vcf):
    female = [line.strip() for line in open(femalelist)]
    male = [line.strip() for line in open(malelist)]
    with gzip.open(vcf, "rt", encoding="utf-8") as txt:
        for line in txt:
            if not line.startswith("#"):
                header = header.strip().split()
                femalePos = []
                malePos = []
                for index, value in enumerate(header[9:], start=9):
                    if value in female:
                        femalePos.append(index)
                    elif value in male:
                        malePos.append(index)
                line = line.strip().split()
                p = line[6]
                maleP = 0
                femaleP = 0
                if p == "PASS":
                    for i in malePos:
                        sample = line[i].split(':')
                        tp = sample[0]
                        # dp = int(sample[2])
                        if (tp == "0/1") or (tp == "0|1"):
                            maleP += 1
                    for i in femalePos:
                        sample = line[i].split(':')
                        tp = sample[0]
                        # dp = int(sample[2])
                        if (tp == "0/0") or (tp == "0|0"):
                            femaleP += 1

                    if (maleP >= len(malePos)*0.8) and (femaleP >= len(femalePos)*0.8):
                        print("\t".join(line))
            else:
                header = line


def main():
    filter_vcf(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()


