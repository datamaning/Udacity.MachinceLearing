"""Count words."""
import main
class Reversinator(object):
    def __init__(self, obj):
        self.obj = obj
    def __lt__(self, other):
        return other.obj < self.obj
def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    map={}
  
    l=s.split(" ")
    for i in l:
        i = i.strip()
        if i!="":
            if map.has_key(i)==False:
                map.setdefault(i,1)
            else:
                count=map.get(i)+1
                map[i]=count
###########################################
#		sort map									#
#		sort map									#
###########################################
   # map=sorted(map.iteritems(),key=lambda asd:asd[1],reverse=True)
    map=sorted(map.iteritems(),key=lambda x: (x[1], Reversinator(x[0])),reverse=True)
    list_map=list(map);
    top_n=list_map[0:n]
    # TODOmap={}
###########################################
#		sort map									#
#		sort map									#
###########################################
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
