import random
import molecules
import numpy.random as npr


class Process(object):
    """
    Parent for all cellular processes.
    """
    def __init__(self, id, name): #Konstruktor
        self.id = id
        self.name = name


        self.enzyme_ids = [] 
        self.substrate_ids = []

    def set_states(self, substrate_ids, enzyme_ids): # mRNA, Ribosom
        self.enzyme_ids = enzyme_ids # auch leere Liste
        self.substrate_ids = substrate_ids

    def update(self, model): #hier ist ein sinnloser Kommentar
        """
        Has to be implemented by child class.
        """
        pass # = mach nichts
        #Defaultfunktion
        #weil andere Klassen auch die FUnk miterben


class Translation(Process):
    """
    Translation is instantiated in the Cell to produce proteins.

    Defines Translation process. It iterates over all ribosomes and decides what
    they should do. They either bind to mRNA or elongate/terminate a protein if
    they are already bound.

    """
    code = dict([('UCA', 'S'), ('UCG', 'S'), ('UCC', 'S'), ('UCU', 'S'),
                 ('UUU', 'F'), ('UUC', 'F'), ('UUA', 'L'), ('UUG', 'L'),
                 ('UAU', 'Y'), ('UAC', 'Y'), ('UAA', '*'), ('UAG', '*'),
                 ('UGU', 'C'), ('UGC', 'C'), ('UGA', '*'), ('UGG', 'W'),
                 ('CUA', 'L'), ('CUG', 'L'), ('CUC', 'L'), ('CUU', 'L'),
                 ('CCA', 'P'), ('CCG', 'P'), ('CCC', 'P'), ('CCU', 'P'),
                 ('CAU', 'H'), ('CAC', 'H'), ('CAA', 'Q'), ('CAG', 'Q'),
                 ('CGA', 'R'), ('CGG', 'R'), ('CGC', 'R'), ('CGU', 'R'),
                 ('AUU', 'I'), ('AUC', 'I'), ('AUA', 'I'), ('AUG', 'M'),
                 ('ACA', 'T'), ('ACG', 'T'), ('ACC', 'T'), ('ACU', 'T'),
                 ('AAU', 'N'), ('AAC', 'N'), ('AAA', 'K'), ('AAG', 'K'),
                 ('AGU', 'S'), ('AGC', 'S'), ('AGA', 'R'), ('AGG', 'R'),
                 ('GUA', 'V'), ('GUG', 'V'), ('GUC', 'V'), ('GUU', 'V'),
                 ('GCA', 'A'), ('GCG', 'A'), ('GCC', 'A'), ('GCU', 'A'),
                 ('GAU', 'D'), ('GAC', 'D'), ('GAA', 'E'), ('GAG', 'E'),
                 ('GGA', 'G'), ('GGG', 'G'), ('GGC', 'G'), ('GGU', 'G')])

    def __init__(self, id, name):
        super(Translation, self).__init__(id, name) # ohne super keine Attribute, aber Funktionen 

        # declare attributes
        self.__ribsomes = []

    def update(self, model): # von model, saemtliche modelobjekte
        """
        Update all mrnas and translate proteins.
        """
        self.__ribosomes = model.states[self.enzyme_ids[0]] # gibt Ribosomobjekt von enzyme aus model 
        for mrna_id in self.substrate_ids:
            prot = None
            mrna = model.states[mrna_id]
<<<<<<< HEAD

            prot = self.elongate(mrna)
=======
            if not mrna.binding[0]: # wenns 0 ist, Abfrage richtig, geht rein
                self.initiate(mrna)
            else:
                prot = self.elongate(mrna)
>>>>>>> 78e177808159f55a1f0c4c2dec7b239af38fcfac
            if isinstance(prot, molecules.Protein): # Typabfrage
                if prot.id in model.states:
                    model.states[prot.id].append(prot)
                else:
                    model.states[prot.id] = [prot]

<<<<<<< HEAD

            if not mrna.binding[0]: # wenns 0 ist, Abfrage richtig, geht rein
                self.initiate(mrna)
            #else:
            
=======
>>>>>>> 78e177808159f55a1f0c4c2dec7b239af38fcfac
    def initiate(self, mrna):
        """
        Try to bind to a given MRNA. Binding probability corresponds to the ribosome count.

        @type mrna: MRNA
        """

        if not mrna.binding[0]:  #  no mrna bound yet and target mrna still free at pos 0
            # bind a nascent protein to the 0 codon
            if npr.poisson(self.__ribosomes.count) > 1: # at least one binding event happens in time step
                # if a ribosome binds the position a new Protein is created and stored on the
                # position as if it were bound to the ribosome
                mrna.binding[0] = molecules.Protein("Protein_{0}".format(mrna.id),
                                                     "Protein_{0}".format(mrna.id),
                                                     self.code[mrna[0:3]])
                self.__ribosomes.count -= 1

    def elongate(self, mrna):
        """
        Elongate the new protein by the correct amino acid. Check if an
        MRNA is bound and if ribosome can move to next codon.
        Terminate if the ribosome reaches a STOP codon.

        @type return: Protein or False
        """

<<<<<<< HEAD
        perm_list = npr.permutation(range(len(mrna.binding)))
        for i in perm_list:
            bound_at_i = mrna.binding[i]

            if isinstance(bound_at_i, molecules.Protein):
                codon = mrna[i*3:i*3+3]
                aa = self.code[codon]
                if aa == "*":  # terminate at stop codon
                    return self.terminate(mrna, i)

                if not mrna.binding[i + 1]:  # if the next rna position is free
                    mrna.binding[i] + aa
                    mrna.binding[i + 1] = mrna.binding[i]
                    mrna.binding[i] = 0
        return 0


        # TODO: this needs to update in a random order
       

=======
        # TODO: this needs to update in a random order

        for i, ribosome in enumerate(mrna.binding):
            try:
                if 'AUG' in mrna:

                    j = mrna.index('AUG')
                    while (j < j + 16):
                        if isinstance(ribosome, molecules.Protein):
                            codon = mrna[3*i:3*i+3]
                            aa = self.code[codon]
                            if not aa == "M":
                                j += 1
                                continue 
                            else: 
                                if aa == "*":  # terminate at stop codon
                                    return self.terminate(mrna, i)
                        j += 1

            except:
                print "Wrong length of mRNA."    

                if not mrna.binding[i + 1]:  # if the next rna position is free
                    mrna.binding[i] + aa # setze auf diese Stelle aa
                    mrna.binding[i + 1] = mrna.binding[i] # die naechste Stelle wird die betrachtete
                    mrna.binding[i] = 0 # und die betrachtete Stelle ist 0
        return 0

>>>>>>> 78e177808159f55a1f0c4c2dec7b239af38fcfac
    def terminate(self, mrna, i):
        """
        Splits the ribosome/MRNA complex and returns a protein.

        @type mrna: MRNA
        """
<<<<<<< HEAD
=======

>>>>>>> 78e177808159f55a1f0c4c2dec7b239af38fcfac
        protein = mrna.binding[i]  # bound mRNA
        mrna.binding[i] = 0 #ungebunden
        self.__ribosomes.count += 1
        print protein.sequence
<<<<<<< HEAD
        print self.energy(protein.sequence)
        return protein
    
    def energy(self, value):
        atp = len(value)
        gtp = 4*len(value)
        print '{0} ATP und {1} GTP wurden verbraucht.'.format(atp,gtp)
        return (atp, gtp)

    
=======
        return protein
>>>>>>> 78e177808159f55a1f0c4c2dec7b239af38fcfac
