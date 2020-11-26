# define the constituency
class constituency():
    def __init__(self, name, num, candidatelist):
        self.name = name
        self.num = num
        self.candidatelist = candidatelist

    # test function, probably will merge into init?
    def return_elected(self):
        i = 0
        result = []
        _candidatelist = self.candidatelist.copy()
        _candidatelist.sort(reverse = True)
        # list slicing seems to return memory addresses so this is an alternative
        while(i < self.num):
            result.append(str(_candidatelist[i]))
            i = i + 1
        return result

    def return_percentages(self):
        result = []
        total = 0
        for _candidate in self.candidatelist:
            total = total + _candidate.votes
        for _candidate in self.candidatelist:
            # due to python being annoying with floating points i have to go from float -> str -> float. 
            # there has to be a better way (decimal?) but i can't be arsed to import it just to fix this
            result.append([_candidate.name, _candidate.party, float("{:.3f}".format((_candidate.votes / total) * 100))])
        return result

    def recalculate(self, votePercent):
        pass

    def __str__(self):
        return "Name: " + str(self.name) + "\nSeats to fill: " + str(self.num) + "\nCandidates: " + str(self.num)
        
# add return strings for things like whether candidate was elected
class candidate():
    def __init__(self, name, votes, party):
        self.name = name
        self.votes = votes
        self.party = party
    
    def __eq__(self, other):
        return self.votes == other.votes

    def __lt__(self, other):
        return self.votes < other.votes

    def __gt__(self, other):
        return self.votes > other.votes
    
    def __str__(self):
        return "Name: " + str(self.name) + " Votes: " + str(self.votes) + " Party: " + str(self.party)


def main():
    """
    3-letter codes for party names: (letters derived from are capitalized)
    LDP : jmn (JiMiN)
    CDP : rkn (RiKkeN)
    komeito : kmt (KoMeiTo)
    DPfP : kkm (KoKuMin)
    ishin no kai : isk (IShin no Kai)
    JCP : jcp (i couldn't come up with a better acronym)
    reiwa shinsengumi : rws (ReiWa Shinsengumi)
    SDP : smt (ShaMinTo)
    NHK : nkt (NKokuTo)
    euthanasia party (?) : ark (AnRakuKai)
    happiness realization party : hrp (such a travesty that i have to write an acronym for this bullshit party...)
    olive tree : orb (ORiBu)
    worker's party for the liberation of labor : wpl (i got lazy here. i'm not reading the entire name just to get an acronym)
    """
    # testing time
    candidate1 = candidate("takahashi_harumi", 828220, "jmn")
    candidate2 = candidate("katsube_kenji", 523737, "rkn")
    candidate3 = candidate("iwamoto_tsuyohito", 454285, "jmn")
    candidate4 = candidate("hatayama_kazuya", 265862, "jcp")
    candidate5 = candidate("haraya_nami", 227174, "kkm")
    candidate6 = candidate("yamamoto_takahira", 63308, "nkt")
    candidate7 = candidate("nakamura_osamu", 23785, "ark")
    candidate8 = candidate("toriyama_yoshinori", 13724, "hrp")
    candidate9 = candidate("iwase_seiji", 10108, "wpl")

    candidatelist = [candidate1, candidate2, candidate3, candidate4, candidate5, candidate6, candidate7, candidate8, candidate9]

    constituency1 = constituency("hokkaido", 3, candidatelist)

    print(constituency1.return_percentages())

main()