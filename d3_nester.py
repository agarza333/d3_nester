
class Nester(object):

    def __init__(self, *args):
        self.keys = args
        self.length = len(args)

    def useNativeNest(self, jsonFile):

        def chaining(chain, count):
            if count == self.length:
                return chain.entries(jsonFile)

            newChain = chain.key(self.keys[count])
            return chaining(newChain, count + 1)

        nativeNest = chaining(Nest(), 0)
        return nativeNest

    def d3ReadyNest(self, nested):
        nestedArray = []

        def Nest(currentNest, children, numNestForFirst):
            rowCount = 0
            for row in currentNest:
                rowCount += 1
                if not isinstance(row.values[0], nesting.Entry):
                    if len(currentNest) - rowCount and self.length == 1:
                        nestedArray.append({})
                        currentDict = nestedArray[-1]
                        currentDict['key'] = row.key
                        currentDict['children'] = row.values[0]
                    else:
                        children.append({})
                        currentDict = children[-1]
                        currentDict['key'] = row.key
                        currentDict['children'] = row.values[0]
                else:
                    if len(currentNest) - \
                            rowCount >= 0 and numNestForFirst == self.length:
                        nestedArray.append({})
                        currentDict = nestedArray[-1]
                        currentDict['key'] = row.key
                        currentDict['children'] = []
                        Nest(
                            row.values,
                            currentDict['children'],
                            numNestForFirst - 1)
                    else:
                        children.append({})
                        currentDict = children[-1]
                        currentDict['key'] = row.key
                        currentDict['children'] = []
                        Nest(
                            row.values,
                            currentDict['children'],
                            numNestForFirst)

        Nest(nested, [], self.length)
        return {"key": "root", "children": nestedArray}
