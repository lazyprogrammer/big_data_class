# book url: https://www.amazon.com/dp/B01KH9YWSY
class Reducer:
    def reduce(self, d):
        returnval = []
        for k, v in d.iteritems():
            returnval.append("%s\t%s" % (k, sum(v)))
        return returnval
