def csWhereIsBob(names):
     '''
     input names - a list of strings
                        
     output is an integer which is the location of Bob 
     if Bob not present return -1
     '''
                                                
     if "Bob" not in names:
         return -1
                                                                    
     for i in range(len(names)):
         if names[i] == "Bob":
             return i

print(csWhereIsBob(["Jimmy", "Layla", "Bob"])) # 2
print(csWhereIsBob(["Bob", "Layla", "Kaitlyn", "Patricia"])) # 0
print(csWhereIsBob(["Jimmy", "Layla", "James"])) # -1
