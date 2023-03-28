def generate_acceptat(initial, final, lmax):

    # dictionar pt stari
    transitions={}
    with open('input.txt') as f:
        for linie in f:

            current, simbol, next=linie.strip().split()
            current=int(current)
            next=int(next)

            if current not in transitions: #adaugam starea in dictionar, daca nu o avem deja
                transitions[current]={}

            if simbol=="-":
                simbol = None  # - e lambda

            if simbol not in transitions[current]: #adaugam litera in dictionarul care are cheie starea curenta
                transitions[current][simbol]=[]

            transitions[current][simbol].append(next)

    acceptat=set()
    queue=[(initial, '', 0)]
    visited = set()

    while queue:

        current, cuvant, length = queue.pop(0)  # stare - cuvant - lungime

        # pentru cazul lambda ciclu
        if (current, cuvant, length) in visited:
            continue

        visited.add((current, cuvant, length))

        #cuvantul e acceptat 
        if current in final and length>0:
            acceptat.add(cuvant)

        if length<lmax:
            for simbol, nexts_list in transitions.get(current, {}).items(): # daca nu am simbol si nexts in transitions[current], atunci ={}
                for next in nexts_list:
                    if simbol is None:
                        queue.append((next, cuvant, length))
                    else:
                        queue.append((next, cuvant + simbol, length+1)) # daca nu e lambda, cresc lungimea cu 1, updatez cuvant+simbol 

    return acceptat

# input
initial=int(input("Starea initiala este: "))
final=[int(state) for state in input("Starile finale sunt: ").split()]
lmax=int(input("Lungimea maxima a cuvintelor acceptate este: "))

# cuvintele sortate
acceptat=generate_acceptat(initial, final, lmax)
print("CUVINTE ACCEPTATE:")
for cuvant in sorted(acceptat):
    print(cuvant)

print("NUMARUL DE CUVINTE ACCEPTATE DE AUTOMAT ESTE: ",len(acceptat))