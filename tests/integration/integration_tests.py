import unittest
import sys
import os
import pcode2code

class Processor():

    def __init__(self):
        pass

    def check_output(self, original, input_):
        debug = True
        originallines = original.splitlines()
        splittedinput = input_.splitlines()
        lines=[]
        outputval = True
    
        # we parse each lines, and cut them by line blocks, to put them in "lines"
        for inputLine in splittedinput:
            inputLine = inputLine.strip()
            """
            if inputLine.startswith('Line '):
                lines.append(inputLine.split(':')[1])
            """
            lines.append(inputLine)
    
        if len(originallines) != len(lines):
            print '\t[!] Number of Lines differ\r\n'
            outputval = False
    
        i = 0
        defects = 0
        
        if len(originallines) > len(lines):
            for aline in lines:
                if aline != originallines[i].strip():
                    if debug:
                        print('\t[!] line ' + str(i) + ' mismatch')
                        print('\t[!] original line: ' + originallines[i].strip())
                        print('\t[!] current line: ' + aline)
                        print('')
                    defects += 1
                i += 1
            
        if len(originallines) <= len(lines):
            for aline in originallines:
                print aline
                if aline.strip() != lines[i]:
                    if debug:
                        print '\t[!] line ' + i + 'mismatch'
                        print '\t\toriginal line: ' + aline.strip()
                    defects += 1
                i += 1

        if defects > 0:
            print '\t[!] current mismatchs : ' + str(defects)
            print '\t[!] score : ' + str(100 - ((defects*1.0)/i)*100) +'%'
            outputval = False
    
        return outputval
            
    def readfile(self, path):
        return open(path, 'r').read()
    
    def process_tests(self, path):
        subdirs = [x[0] for x in os.walk(path)]
        subdirs.pop(0) # avoid base dir
        testsok = 0
        totaltests = 0
        for dir_ in subdirs:
            print '[+] processing ' + dir_
            outfile = pcode2code.process(self.readfile(dir_ + '/' + os.path.split(dir_)[1]))
            expectedfile = self.readfile(dir_ + '/expected')
            r = self.check_output(expectedfile, outfile)
            if r:
                testsok +=1
            totaltests +=1
        print('[+] output: ' + str(testsok) + '/' + str(totaltests) +' tests succeeded')



class TestOutput(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestOutput, self).__init__(*args, **kwargs)
        self.processor = Processor()
    
    def testing(self):
        dirname, filename = os.path.split(os.path.abspath(__file__))
        self.processor.process_tests(dirname)
        self.assertEqual(1,2)
        

        
if __name__ == '__main__':
    unittest.main()
        

    
