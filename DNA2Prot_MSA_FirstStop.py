from Bio.Seq import Seq
from Bio import SeqIO
import sys

file_in=sys.argv[1]
file_out=sys.argv[2]

with open(file_out, 'w') as f_out:
    prot = []
    for seq_record in SeqIO.parse(open(file_in, mode='r'), 'fasta'):
        seq_record.seq = (Seq(seq_record.seq)).upper()
        start = Seq(seq_record.seq).find('ATG')
        seq_record.seq = Seq(seq_record.seq[start:len(seq_record.seq)])
        seq_record.seq = Seq((seq_record.seq).translate(to_stop=True))
        r = SeqIO.write(seq_record, f_out, "fasta")
        prot.append(r)

