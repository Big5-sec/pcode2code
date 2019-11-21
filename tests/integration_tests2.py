import unittest
import sys
import os
import pcode2code

class Processor():

    def check_output(self, input_, original):
        originallines = original.splitlines()
        splittedinput = input_.splitlines()
        lines=[]
        outputval = True
    
        # we parse each lines, and cut them by line blocks, to put them in "lines"
        for inputLine in splittedInput:
            inputLine = inputLine.strip()
            if inputLine.startswith('Line '):
                lines.append(inputLine.split(':')[1])
    
        if len(originallines) != len(lines):
            print '\t[!] Number of Lines differ'
            outputval = False
    
        i = 0
        defects = 0
        
        if len(originallines) > len(lines):
            for aline in lines:
                if aline != originallines[i].strip():
                    if debug:
                        print '\t[!] line ' + i + 'mismatch'
                        print '\t\toriginal line: ' + originallines[i].strip()
                    defects += 1
                i += 1
            
        if len(originallines) <= len(lines):
            for aline in originallines:
                if aline.strip() != lines[i]:
                    if debug:
                        print '\t[!] line ' + i + 'mismatch'
                        print '\t\toriginal line: ' + aline.strip()
                    defects += 1
                i += 1
    
        if defects > 0:
            print '\t[!] current mismatchs : ' + defects
            print '\t[!] score : ' + (defects*1.0)/i +'%'
            outputval = False
    
        return outputval
            
    def readfile(self, path):
        return open(path, 'r').read()
    
    def process_tests(self, path):
        subdirs = [x[0] for x in os.walk(path)]
        subdirs.remove('.')
        testsok = 0
        totaltests = 0
        for dir_ in subdirs:
            print '[+] processing ' + dir_
            outfile = pcode2code.process(self.readile(dir_ + '/' + dir_))
            #input_ = pcode2dmp.processinput(readfile(dir_ + '/input'))
            expectedfile = self.readfile(dir_ + '/expected')
            r = check_output(expectedfile, outputfile)
            if r:
                testsok +=1
            totaltests +=1
        print '[+] output: ' + testsok + '/' + totaltests +' tests succeeded'



class TestOutput(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestOutput, self).__init__(*args, **kwargs)
        self.processor = Processor()
    
    def testing(self):
        self.processor.process_tests('.')
        self.assertEqual(1,2)
        

        
if __name__ == '__main__':
    unittest.main()
        

    
