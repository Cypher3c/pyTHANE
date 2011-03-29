'''
Created on March 28, 2011

@author: Cypher
License: GPLv3

Using better abstraction
'''

import asset
import pickle

print "pyTHANE v0.0., pythonized THANE"
print ""
print "by Cypher, licensed under GPLv3"

foo = asset.AssetList()
foo.loadXML("test.xml")

for elem in foo.alist:
    print "----------"
    print elem.aname
    if elem.isvirtual:
        print "---System is Virtual---"
        print elem.faction
        print elem.facvalue
        print elem.facrange
    else: 
        print elem.posX
        print elem.posY
        print elem.spaceGFX
        print elem.extGFX
        if elem.faction:
            print elem.faction
            print elem.facvalue
            print elem.facrange
    if elem.misload:
        print "element did not load properly"
        
#pickle stuff

    
    
    
