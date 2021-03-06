# oeg.infotech.tool

[![Python 2.7](https://img.shields.io/travis/vb64/oeg.infotech.tool.svg?label=Python%202.7&style=plastic)](https://travis-ci.org/vb64/oeg.infotech.tool)
[![Code Climate](https://img.shields.io/codeclimate/maintainability-percentage/vb64/oeg.infotech.tool.svg?label=Code%20Climate&style=plastic)](https://codeclimate.com/github/vb64/oeg.infotech.tool)
[![Coverage Status](https://coveralls.io/repos/github/vb64/oeg.infotech.tool/badge.svg?branch=master)](https://coveralls.io/github/vb64/oeg.infotech.tool?branch=master)

Win32 console utility for manipulating OrgEnergoGaz Infotech xml files

## Install

```
$ git clone git@github.com:vb64/oeg.infotech.tool.git
$ cd oeg.infotech.tool
$ make setup PYTHON_BIN=D:\python\2.7.15\python.exe
```

## Build infotech.exe

```
$ make exe
```

`infotech.exe` executable can be found in `dist` folder.

## Use

```
> infotech.exe csv_weld fixtures\xml\1736.xml >build\1736_weld.csv
> infotech.exe csv_defect fixtures\xml\1736.xml >build\1736_defect.csv
> infotech.exe csv_lineobj fixtures\xml\1736.xml >build\1736_lineobj.csv
> infotech.exe reverse fixtures\xml\1736.xml >build\1736_reverse.xml
> infotech.exe join fixtures\xml\1736.xml 1100 fixtures\xml\1737.xml >build\1736_join.xml
```
