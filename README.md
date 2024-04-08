# set-yourself-TREE
sorry for the pun...

## Tree from What?

I don't know, I just thought it was a funny name. But really, I had a situation lately that having ran `tree` previously saved the day. 

On my unRAID NAS server, I have lots of media that would be pretty easy to replace if the unthinkable happened. In cases such as this, having an accurate layout and list of contents of your folders can be vital to restoration, god forbid. Trust me, you might think you know what is on your hard drives but when it comes down to an itemized list, you will miss some things. 

```
.
├── AWS Exam
│   └── AWS-Certified-Cloud-Practitioner_Sample-Questions.pdf
├── Chemistry
├── Code
│   └── 7zrar.sh
├── DoesResolve.sh
├── Electronics Projects.txt
├── Git
│   ├── code
│   │   └── git_basics
│   │       ├── README.md
│   ├── dog
│   └── git_basics
│       ├── README.md
├── Hacking
│   ├── Chase Cunningham - Cyber Warfare-Packt Publishing (2020).epub
│   ├── InfoSec_for_Journalists_V1.21.pdf
│   ├── Investigations
│   ├── Shared Folder VM
│   ├── Wireshark_Tut1.pdf
│   └── aquatone
│       ├── CHANGELOG.md
│       ├── Gopkg.lock
│       ├── Gopkg.toml
│       ├── LICENSE.txt
│       ├── README.md
│       ├── agents
```

Thereby, a script that automagically dumps the file metadata of your drives in a sane, readable format can be invaluable in case you ever delete something on accident or screw up, and accidentally wipe the contents of the Cache drive which contained all the recent TV shows I had moved.

## Installation

I set this up as a docker image which basically just runs a simple Python script. You can configure the time length between runs (I do every 5 days) and obviously you will need to change the ENV FLAGS for your mount/folder locations. 

## TLDR

Script for unRAID or other NAS that runs "Tree" command to get a text list of your files. Call it a poor mans mirror. 


