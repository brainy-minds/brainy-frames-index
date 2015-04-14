#!/usr/bin/env python
'''
Index generation script:

- generate a new `index.yaml`
- compute md5hash of `index.yaml` and save it as `hash`

requires:

pip install -r requires.txt

'''
import os
import yaml
import hashlib
from glob import glob


def hashfile(afile, hasher, blocksize=65536):
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.hexdigest()


def build_index(index_yaml='index.yaml'):
    # List all YAML files.
    packages = list()
    for yaml_file in glob('*/*.yaml'):
        package_description = yaml.load(open(yaml_file).read())
        name, version = os.path.basename(yaml_file).split('_', 1)
        package_description['name'] = name
        package_description['version'] = name
        assert 'url' in package_description
        packages.append(package_description)
    # Write index.
    index = {'packages': packages}
    with open(index_yaml, 'w+') as stream:
        stream.write(yaml.dump(index, default_flow_style=False))


def update_index_hashsum(index_yaml='index.yaml'):
    index_hash = hashfile(open(index_yaml, 'rb'), hashlib.sha256())
    with open('hash', 'w') as hashsum:
        hashsum.write(str(index_hash))


if __name__ == '__main__':
    # Point working directory to the index repository.
    os.chdir(os.path.dirname(__file__))

    build_index()
    update_index_hashsum()
