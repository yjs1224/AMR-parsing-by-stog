import argparse
import os

def main(infn,outdir):
    # Load the file
    print('Reading ', infn)
    sents = []
    with open(infn) as f:
        for line in f.readlines():
            line = line.strip()
            if not line or len(line)==0: continue
            sents.append(line)


    # Create a dummy amr file
    os.makedirs(outdir, exist_ok=True)
    for outfn in ["test.txt",]:
        outfn = os.path.join(outdir,outfn)
        print('Writing ', outfn)
        with open(outfn, 'w') as f:
            for i, sent in enumerate(sents):
                f.write('# ::id sents_id.%d\n' % i)
                f.write('# ::snt %s\n' % sent)
                f.write('(d / dummy)\n')
                f.write('\n')
    for outfn in ["dev.txt", "train.txt"]:
        outfn = os.path.join(outdir,outfn)
        print('Writing Nothing to ', outfn)
        with open(outfn, 'w') as f:
            for i, sent in enumerate(sents):
                f.write('# ::id sents_id.%d\n' % i)
                f.write('# ::snt %s\n' % sent)
                f.write('(d / dummy)\n')
                f.write('\n')
                if i >=0:
                    break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="args")
    parser.add_argument("--in_file", type=str)
    parser.add_argument("--out_dir", type=str)
    args = parser.parse_args()
    main(args.in_file, args.out_dir)

