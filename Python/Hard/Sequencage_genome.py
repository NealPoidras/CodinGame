##Working a 92%
import sys
class PermutationAndSequencingHandler:
    n=0
    elements = list()
    permutations = list()
    def __init__(self,n=0,elements = []):
        self.n = n
        self.elements = elements
    def permute():
        self.permute(0,str(n))
    
    def permute(index,array = list(str)):
        if(index==self.n) :
            self.permutations.append(array)
        else:
            element = str(self.elements[index])
            for i in range(self.n) :
                if(array[i] == None):
                    arr = array[n]
                    arr[i]=element
                    self.permute(index+1,arr)
            

    def finShourtestSequence():
        shortest = sys.maxsize
        for permutation in permutations :
            size = calcLenght(permutation)
            if(size<shortest):
                shortest=size
        return size

    def calcLenght(permutation = list(str)):
        builder = list(str)
        builder.append(permutation[0])
        for i in range(self.n):
            j = i-1
            first = permutation[j]
            second = permutation[i]
            bestLength = 0
            if second in first:
                bestLength=len(second)
            else:
                for i in range(min(len(first),len(second))):
                    firstSub = first[len(first)-i:len(first)]
                    secondSub = second[0:i]
                    if(firstSub == secondSub):
                        bestLength = i
            
            builder.append(second[bestLength:len(second)])

        return builder

n = input()
subseqs=list()
for i in range(n):
    subseq=input()
    subseqs.append(subseq)
subseqs.reverse()
handler = PermutationAndSequencingHandler()
shortest = handler.findShortestSequence()
print(str(shortest))