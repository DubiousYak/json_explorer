import click
import json
from pygments import highlight, lexers, formatters
import types

def get_json(file_name):
    with open(file_name, "r") as raw_json:
        ugly_json = raw_json.read()

    return json.loads(ugly_json)

# is there a way to do a better highlighting scheme?
def get_color_json_string(formatted_json):
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    return colorful_json

def walk_json(json_object, key_path):

    path_to_print = key_path.split('/',1)
    # click.echo(json_object)

    myMap = dict(json_object)
    if path_to_print[0] in myMap.keys():
        val = myMap[path_to_print[0]]
        # print(type(val))
        # make info match json spec: json.org/json-en.html
        if isinstance(val, list):
            click.echo('This is a array')
            for attr in val:
                click.echo(attr)
        elif isinstance(val, str):
            click.echo('"'+ val + '" is an string')
        elif isinstance(val, bool):
             click.echo('"'+ str(val) + '" is an bool')
        elif isinstance(val, (int, float)):
            click.echo('"'+ str(val) + '" is an number')
        elif val == None:
            click.echo('"'+ str(val) + '" is an null')
        else:
            click.echo('This is an object.')
            click.echo(get_color_json_string(json.dumps(val)),  nl=False)
            ## check if path to print is None
            if len(path_to_print) > 1:
                walk_json(val, path_to_print[1])
    else:
        click.echo(path_to_print[0] + " is not a valid key")

@click.group(chain=True)
def cli():
    pass

## json explorer
## other features
# get value by nested key dog.minataure might give mini poodle and other small dogs
# convert to YAML
# convert from YAML
# paginate long json files
# get json from web address?
# add poetry
# add set up tools

@cli.command("pretty")
@click.option('-r','--raw', 'is_raw', is_flag=True, help='Display raw json.')
@click.option('-o','--out', 'out_file', default=None, help='File to write out to.')
@click.option('-e','--edit', 'edit_json', is_flag=True, help='Edit the json before saving.')
@click.argument("file_name")    
def pretty(is_raw, file_name, out_file, edit_json):
    """Takes a JSON file and makes it so pretty."""
    # read file
    click.echo("file name: ", nl=False)
    click.echo(click.style(file_name, fg='red',bold=True))

    json_object = get_json(file_name)

    if is_raw == True:
        indent_json = None
    else:
        indent_json = 4

    formatted_json = json.dumps(json_object, indent=indent_json)

    if edit_json:
        formatted_json = click.edit(formatted_json)

    if out_file is not None and formatted_json is not None:
        with open(out_file, "w") as file_ptr:
            file_ptr.write(formatted_json)

    # secho imposes a style on the string, allowing colors
    if formatted_json is not None:
        click.echo(get_color_json_string(formatted_json))

## explore json
@cli.command("walk")
@click.option('-k','--keys', 'keys', is_flag=True, help='Display Keys.')
@click.option('-v','--value', 'key_to_get', default=None, help='Display Value by Key.')
@click.argument("file_name")
def walk(file_name, keys, key_to_get):

    json_object = get_json(file_name)

    myMap = dict(json_object)

    if keys:
        click.echo(list(myMap.keys()))
    if key_to_get:
        walk_json(json_object, key_to_get)


if __name__ == "__main__":
    cli()

