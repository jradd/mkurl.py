# mkurl
Simple script to create markdown url's from a directory
listing. 

#### Usage:
`python mkurl.py <dir_to_list> [output file]`  

```python
$ python mkurl.py /srv/data/wiki Test.md
Appending to file ==> /srv/data/wiki/Test.md
[[test]]
[[regex-cheat]]
[[fullstack]]
[[_Footer]]
[[Home]]
[[preview]]
[[notes]]
[[python]]
[[todo]]
[[regex]]
[[TOC]]
Processed: 11 files.

$ ls /srv/data/wiki
notes        notes_unsorted  containers.sh  fullstack.md  perf.txt    regex-cheat.md  Test.md
notes_final  uploads         Dockerfile     Home.md       preview.md  regex.md        TOC.md
notes_old    work            _Footer.md     notes.md      python.md   test.md         todo.md
```



