# mvr
The "mv" coreutil but with regular expressions.

## Usage

```bash
mvr.py match_regex rename_regex files [files ...]
```

## Examples

#### Rename all .zip files to .cbz files recursively
```bash
$ mvr.py '(.*)\.zip$' '\1.cbz'
```

#### Use anything python's `re` module supports like character classes and backreferences
```bash
$ mvr.py 'img(\d+).png' 'image\1.png'
```

#### Will warn you if there's a collision in the new names
```shell
$ mvr.py '.txt$' 'constant_string'
Collision exists in new file names. Aborting...
```

### Move into different directories

```shell
$ mvr.py 'app/assets/images/([^\.]+)\.(.+)$' 'public/images/\1_new.\2'
```
