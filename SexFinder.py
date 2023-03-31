import sys
import gzip
def filter_vcf(vcf):
    with gzip.open(vcf , "rt",encoding = "utf-8" ) as txt:
        for line in txt:
            if not line.startswith("#"):
                line = line.strip().split()
                Chr = line[0]
                pos = line[1]
                p = line[6]
                female = [12, 16, 18, 19, 23, 25, 26, 30, 31, 32, 34, 35, 37, 38, 39, 40, 42, 46, 47, 48]
                male = [9, 10, 11, 13, 14, 15, 17, 20, 21, 22, 24, 27, 28, 29, 33, 36, 41, 43, 44, 45]
                maleP = 0
                femaleP = 0
                if p == "PASS":
                    for i in male:
                        sample = line[i].split(':')
                        tp = sample[0]
                        dp = int(sample[2])
                        if   ((dp >= 5) and ( (tp =="0/1") or (tp == "0|1") )):
                            maleP += 1
                    for i in female:
                        sample = line[i].split(':')
                        tp = sample[0]
                        dp = int(sample[2])
                        if  ((dp >= 5) and ( (tp =="0/0") or (tp == "0|0") )):
                            femaleP += 1

                    if (maleP >=18 ) and (femaleP >= 18 ):
                        print("\t".join(line))
filter_vcf(sys.argv[1] )
