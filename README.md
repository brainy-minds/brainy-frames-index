# brainy-frames-index
An online index of brainy packages.

## Releasing a package

A package description is called a frame.

To add a new release of the existing package one has to add a description file into this index folder tree. It is enough that package is available via http url as an **tar.gz** or as a github repository with a specific *tag/<tag>* or *branch* instead of the version.

If the package is new, just create a missing folder and add the package there.

Package description is a yaml file. The name of the package and the version are encoded into the filename. E.g. description for iBRAIN package version 3.0.1 will be located under `iBRAIN/iBRAIN_3.0.1.yaml` according to `<name>_<version>.yaml`.

## YAML scheme of package description

```yaml
# Keys like `name`, `version` are parsed from the file name.

# Namespace of the package is parsed from URL if possible.
# In case of the GITHUB workflow it corresponds to the project owner.
# In this case namespace can be parsed from the github https url below.
namespace: 'pelkmanslab'

url: 'https://github.com/pelkmanslab/iBRAIN/archive/3.0.1.tar.gz'

depens_on:
  - 
    name: 'CellProfilerPelkmans'
    version: '1.0.0'

```


## How index is build

Each folder is listed and each file is collected into one big `index.yaml`. This is called index (re)building.


## Updating local copy of the index file

This repository contains `index_hash`, which is a (sha)hash of `index.yaml`. It is incremented every time a new `index.yaml` is build.

When user runs command:

```
brainy frames update
```

The hash of `index.yaml` is downloaded from the github repository 

```
GET https://raw.githubusercontent.com/brainy-minds/brainy-frames-index/master/index_hash
```
and compared versus the hash of the local copy of the `index.yaml`.

## How to build index.

Run `build.py`. It will: 

- generate a new `index.yaml`
- compute (sha)hash of `index.yaml` and save it as `hash`

Commit and push new changes if you happy about result.


Every time the index maintainer runs `build.py` 


If the number changes from the local copy, then the whole 
repository is cloned into /tmp and new index is build.
