import sys
import gzip
def filter_vcf(femalelist , malelist, vcf):
    female =  [line.strip() for line in open(sys.argv[1])]
    male =  [line.strip() for line in open(sys.argv[2])]
    with gzip.open(vcf , "rt",encoding = "utf-8" ) as txt:
        for line in txt:
            if not line.startswith("#"):
                line = line.strip().split()
                Chr = line[0]
                pos = line[1]
                p = line[6]
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
filter_vcf(sys.argv[1]  , sys.argv[2] , sys.argv[3])
