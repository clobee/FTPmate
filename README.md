# FTPmate

FTPmate tests FTP enabled servers by uploading test executable files, and then (optionally) uploading files which allow for command execution or other actions directly on the target.

_This project was inspired by the famous davtest.pl_

-------
## About

This program attempts to exploit FTP enabled servers by:

- attempting to create a new directory
- attempting to put test files of various programming languages
- check if files executed or were uploaded properly
- optionally upload a backdoor/shell file for languages which execute

Additionally, this can be used to put an arbitrary file to remote systems.

-------
## Requirements

- Python3 

-------
## Test Files

Tests are used to determine if the server can execute a certain type of code. Each test may have a 
corresponding backdoor file, but backdoor files *must* have a corresponding test to determine if 
that file type can execute on the server. It is recommended a simple/basic operation for each language
is used--by default, the supplied tests use mathematical calculations, if possible.

Test files are located in the 'test/' directory. Files must be named according to
the type of program file they will become on the server. For example, a file named 'php.txt'
will be put to the server with a .php extension. 

Each file must have two lines, 'content' and 'execmatch'--the body put to the server and regex to 
match to see if it executed. For example, the php.txt contents are:
	content=<?php print 7.8 * 6.4;?>
	execmatch=49.92

Additionally, the token $$FILENAME$$ will be replaced (with the PUT file's name) in the content before
it sent to the server. Embedded newlines (\n) will be converted to actual newlines (to accommodate PERL).

-------
## Backdoor files

Backdoor files are located in the 'backdoors/' directory. They must have the match extension for the type 
they will be uploaded for. For example, a php backdoor must have a '.php' extension.

A backdoor file can contain any code you desire, and multiple backdoor files may be used for a file type. 
If multiple files exist for a type, each will be uploaded when appropriate.

A backdoor type (e.g., php) *must* have a corresponding type in the 'tests/' directory, otherwise it will 
never be tested/uploaded.

-------
## Examples

Example: Test file uploads at a specific location url:
```bash
ftpmate.py -ftpip 127.0.0.1 -ftpport 2121 -url http://localhost/hellodir
```

Example: Test file uploads at this location url and send backdoors for any that succeed:
```bash
ftpmate.py -ftpip 127.0.0.1 -ftpport 2121 -url http://localhost/hellodir -sendbd auto
```

Example: Upload a file using authentication, send the perl_cmd.pl backdoor and call it perl.pl on the server:
```bash
ftpmate.py -ftpip 127.0.0.1 -ftpport 2121 -url http://localhost/hellodir -auth user:pass -uploadfile backdoors/perl_cmd.pl -uploadloc perl.pl
```

-------
## TODO:
- Backdoors for more languages 
- Threads
- Cleanup 

