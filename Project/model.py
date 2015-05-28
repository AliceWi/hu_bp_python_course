import processes as proc
import molecules as mol

sample_seq = unicode("AUGGUACCGGGAUUUCGCGGGAUUGUACAAAAAUACGUUUUGUACAUGUUGUGCUGUUACCACUGCAAAUACACUUGGUUUCAAACACUUCCAUAG")

class Model(object):
    """
    Initializes the states and processes for the model and lets the processes update their corresponding states.
    """
    def __init__(self):
        self.states = {}
        self.processes = {}

        # initiate states
        self.ribosomes = {'Ribosomes': mol.Ribosome('Ribosomes', 'Ribosomes', 1)}
        mrna_list = ["AUGGUACGUUUCUAG", "AUGGUACGUUUUUAG", "AUGUUUCGUUUCUAG", sample_seq]
        print "Es wurden {0} mRNA Molekuele erkannt.".format(len(mrna_list))
        self.mrnas = {'MRNA_{0}'.format(i): mol.MRNA(i, 'MRNA_{0}'.format(i), mrna_list[i]) for i in xrange(len(mrna_list))}

        self.states.update(self.ribosomes)
        self.states.update(self.mrnas)

        # initiate processes
        translation = proc.Translation(1, "Translation")
        translation.set_states(self.mrnas.keys(), self.ribosomes.keys())
        self.processes = {"Translation":translation}

    def step(self):
        """
        Do one update step for each process.
        """

        for p in self.processes:
            self.processes[p].update(self)

    def simulate(self, steps, log=True):
        """
        Simulate the model for some time.
        """
        for s in xrange(steps):
            self.step()
    
if __name__ == "__main__":
    c = Model()
    c.simulate(100, log=True)