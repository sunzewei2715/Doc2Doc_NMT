import os 
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--hypotheses_dir', '-hd', required=True,
                     help='The hypotheses paths')

parser.add_argument('--reference', '-r', required=False, default='./testsets/doc/en.tok',
                     help='The reference path (tokened)')

parser.add_argument('--candidates', '-c', required=False, default='./testsets/doc/en.candidates',
                     help='The word candidates file path')

args = parser.parse_args()

nums = [50,46,52]
frontwindow = 20
backwindow = 20

with open(args.reference, 'r') as f:
    refs = f.readlines()
with open(args.candidates, 'r') as f:
    cand_lines = f.readlines()

hyps_dir = args.hypotheses_dir
if os.path.isfile(hyps_dir):
    hyp_paths = [hyps_dir]
elif os.path.isdir(hyps_dir):
    hyp_paths = [os.path.join(hyps_dir, x) for x in sorted(os.listdir(hyps_dir))]
else:
    raise("Wrong Hypotheses Path!")

def check(i, cand, span):
    if len(cand.split(' '))>1:
        if cand in ' '.join(span):
            return True
    else:
        if cand in span:
            return True
    return False

for hyp_path in hyp_paths:
    print('---------{}--------'.format(hyp_path))
    with open(hyp_path, 'r') as f:
        hyps = f.readlines()

    n_t, n_c, n_p = 0, 0, 0
    all_t, all_c, all_p = 0, 0, 0 
    pall = 0
    for i in range(len(hyps)):
        hyp_wordlist = hyps[i].split()
        ref_wordlist = refs[i].split()
        length_ratio = len(hyp_wordlist) / len(ref_wordlist)
        labels = cand_lines[i].strip().split('\t')

        for label in labels:
            pos = int(label.strip().split(':')[0])
            pos = int(pos * length_ratio)
            cands = label.split(':')[1].split(',')
            for cand in cands:
                span = hyp_wordlist[max(pos-frontwindow,0):min(pos+backwindow,len(hyp_wordlist))]
                if check(i, cand, span):
                    if i < nums[0]:
                        n_t += 1
                    elif i < nums[0] + nums[1]:
                        n_c += 1
                    else:
                        n_p += 1
                    break

        if i < nums[0]:
            all_t += len(labels)
        elif i < nums[0] + nums[1]:
            all_c += len(labels)
        else:
            all_p += len(labels)

    print("TC:\t", round(100*n_t/all_t, 1), "(hit={0}, all={1})".format(n_t, all_t))
    print("CP:\t", round(100*n_c/all_c, 1), "(hit={0},  all={1})".format(n_c, all_c))
    print("PT:\t", round(100*n_p/all_p, 1), "(hit={0},  all={1})".format(n_p, all_p))
    print("TCP:\t", round(100*(n_t/all_t*n_c/all_c*n_p/all_p)**(1/3), 1))
    print()
