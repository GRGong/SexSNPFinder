import sys
import gzip


def filter_vcf(femalelist, malelist, vcf):
    female = [line.strip() for line in open(femalelist)]
    male = [line.strip() for line in open(malelist)]
    head = ""
    with gzip.open(vcf, "rt", encoding="utf-8") as txt:
        for line in txt:
            if not line.startswith("#"):
                if not head:
                    header = header.strip().split()
                    femalePos = []
                    malePos = []
                    for index, value in enumerate(header[9:], start=9):
                        if value in female:
                            femalePos.append(index)
                        elif value in male:
                            malePos.append(index)
                    head = "done"
                    print(femalePos)
                    print(malePos)
                
                line = line.strip().split()
                p = line[6]
                maleP = 0
                femaleP = 0

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
    if len(sys.argv) != 4:
        print("Usage: python SexFinder.py <femalelist> <malelist> <vcf>")
        sys.exit(1)
    filter_vcf(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()




