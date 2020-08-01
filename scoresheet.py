class ScoreSheet(object):
    def __init__(self):
        self.sheet = dict() # pid to list of scores
        self.currBids = dict() # pid to list of bids

    def bidToScore(self, bid):
        return bid*11+10
    
    def sumOfBids(self):
        return sum(self.currBids)

    def getBid(self, pid):
        return self.currBids[pid]
    
    def getScore(self, pid):
        return sum(self.sheet[pid])

    def addBid(self, pid, bid):
        self.currBids[pid] = bid