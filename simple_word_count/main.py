# book url: https://www.amazon.com/dp/B01KH9YWSY
from mapper import Mapper
from reducer import Reducer

class JobRunner:
    def run(self, Mapper, Reducer, data):
        # map
        mapper = Mapper()
        tuples = mapper.map(data)

        # combine
        combined = {}
        for k, v in tuples:
            if k not in combined:
                combined[k] = []
            combined[k].append(v)

        # reduce
        reducer = Reducer()
        output = reducer.reduce(combined)

        # do something with output
        for line in output:
            print line

runner = JobRunner()
runner.run(Mapper, Reducer, open('input.txt'))
