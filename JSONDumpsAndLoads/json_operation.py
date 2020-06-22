import json

# dumps takes an object and produces a string:

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# load would take a file-like object, read the data from that object, and use that string to create an object:

with open('event.json') as fh:
    a = json.load(fh)
    print(a)


# Note that dump and load convert between files and objects, while dumps and loads convert between strings and objects.
# You can think of the s-less functions as wrappers around the s functions:

def dump(obj, fh):
    fh.write(json.dumps(obj))


def load(fh):
    return json.loads(fh.read())
