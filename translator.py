#using dictionary and having a string which consists of symbols each of which can be translated into dec system, you can get list with translated symbols
class Translator:
    def __init__(self, d, s):
        self.dictionary = d
        self.string = s
#if there are not any matches in a dictionary and string, this method returns 'None'
    def get_collection(self):
        my_list = list()
        value = ''
        inside = False
        for i in self.string:
            if inside == True:
                if i != ']':
                    value += i
                    continue
                else:
                    value += i
                    if not value in self.dictionary:
                        return None
                    my_list.append(self.dictionary[value])
                    inside = False
                    continue
            if i == '[':
                value = '['
                inside = True
                continue
            else:
                value = i
            if not value in self.dictionary:
                return None
            my_list.append(self.dictionary[value])
        if inside == True:
            return None
        return my_list
#this method uses dec collection which becomes a dec integer. After that the dec integer turns into to_ integer
    def translate_from_to(self, from_, to_, dec_collection):
        in_base10 = 0
        reans = ""
        koef = from_ ** (len(dec_collection)-1)
        for i in range(0, len(dec_collection)):
            in_base10 += dec_collection[i] * koef
            koef = koef // from_
        in_base10 = int(in_base10)
        while in_base10 >= to_:
            reans += str(in_base10 - to_ * (in_base10 // to_))
            in_base10 = in_base10 // to_
        reans += str(in_base10)
        ans = ""
        for i in range(0, len(reans)):
            ans += reans[len(reans) - i - 1]
        return ans
            
        
            
            
            
                
        
        

