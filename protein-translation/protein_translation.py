def proteins(strand):
    strand_dict = {'AUG':'Methionine', 'UUU':'Phenylalanine', 'UUC':'Phenylalanine', 
    'UUA':'Leucine', 'UUG':'Leucine', 'UCU':'Serine', 'UCC':'Serine',
    'UCA':'Serine', 'UCG':'Serine', 'UAU':'Tyrosine', 'UAC':'Tyrosine', 
    'UGU':'Cysteine', 'UGC':'Cysteine', 'UGG':'Tryptophan', 'UAA':'STOP', 
    'UAG':'STOP', 'UGA':'STOP'}
    
    strand_list = list(map(''.join, zip(*[iter(strand)]*3)))
    return_list = []
    for i in strand_list:
        if strand_dict.get(i) == 'STOP':
            return return_list
        else:
            return_list.append(strand_dict.get(i))
    return return_list