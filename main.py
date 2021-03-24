import json
import argparse


def flatten(d, prev='', sep='.'):
    # CREATING A LIST TO RETURN
    objects = []
    # LOOP IN THE DICTIONARY ITEMS
    for k, v in d.items():
        # IF THERE IS A PREVIOUS KEY
        if prev:
            # THE NEW ONE WILL BE A COMBINATION
            ne = prev + sep + k
        else:
            # ELSE IT WILL BE THE SAME
            ne = k
        # IF THE VALUE EXISTS IN THE DICT
        if isinstance(v, dict):
            # EXTENDING THE LIST WITH RECURSION
            objects.extend(flatten(v, ne, sep))
        else:
            # OTHERWISE APPEND TO THE LIST OF TUPLES
            objects.append((ne, v))

    return objects


def run(args):

    # OPENING INPUT FILE
    with open(args.input) as f:
        db = json.load(f)

    f.close()

    # OPENING OUTPUT FILE
    with open(args.output, "w") as fo:
        json.dump(dict(flatten(db)), fo, indent=4)

    fo.close()


def main():
    parser = argparse.ArgumentParser(description="Flatten a json file")
    parser.add_argument("-in", help="json input file", dest="input", type=str, required=True)
    parser.add_argument("-out", help="json output file", dest="output", type=str, required=True)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()




