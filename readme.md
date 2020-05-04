# JSON explorer

## Origin

Even well formatted large json files can be confusing.  This CLI will help you navivigate and understand JSON files you are working with.

## how to use

```shell
$ python jsn_exp.py --help
Usage: jsn_exp.py [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...

Options:
  --help  Show this message and exit.

Commands:
  look  Let's you examine and manipulate the JSON file.
  walk  Let's you explore and manipulate the JSON file.
  
```


```shell
$ python jsn_exp.py look --help
Usage: jsn_exp.py look [OPTIONS] FILE_NAME

  Let's you examine and manipulate the JSON file.

Options:
  -p, --pretty    Display formatted json.
  -o, --out TEXT  File to write out to.
  -e, --edit      Edit the json before saving.
  --help          Show this message and exit.
  ```

```

```shell
$ python jsn_exp.py walk --help
Usage: jsn_exp.py walk [OPTIONS] FILE_NAME

  Let's you explore and manipulate the JSON file.

Options:
  -k, --keys        Display Keys.
  -v, --value TEXT  Display Value by Key.
  --help            Show this message and exit.
```

### Really important sub-sub-title