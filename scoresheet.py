def bidToScore(bid):
    return bid*11+10

class ScoreSheet(object):
    def __init__(self):
        self.sheet = dict() # pid to list of scores
        self.currBids = dict() # pid to list of bids
    
    def getSumOfBids(self):
        return sum(list(self.currBids.values()))
    
    def getTotalScore(self, pid):
        return sum(self.sheet[pid])
    
    def getRoundScore(self, pid, round): # round is zero indexed
        return self.sheet[pid][round]

    def setBid(self, pid, bid):
        self.currBids[pid] = bid
    
    def getBid(self, pid):
        return self.currBids[pid]

    def convertPlayerBidToScore(self, pid, didWin):
        if didWin:
            self.addScore(pid, self.bidToScore(self.getBid(pid)))
        else:
            self.addScore(pid, 0)
        self.currBids.pop(pid)