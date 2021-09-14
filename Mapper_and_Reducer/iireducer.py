#!/usr/bin/python
import sys


def reduce(key, value_list, file_out):
    # Write to file (appends)
    print(str(key) + "\t" + ",".join(value_list))

    # Emit just in cause this reducer will be chained further
    file_out.write(key + "\t" + ",".join(value_list) + "\n")


if __name__ == "__main__":
    current_key = None
    previous_key = None
    value_list = []

    with open(file="../inverted-index.txt", mode="w") as file_out:
        for line in sys.stdin:
            # Split line into key-value pairs
            line_list = line.strip().split("\t")
            current_key = line_list[0]
            value = line_list[1]

            # If not at line 1 and not iterating the same category as previous
            if previous_key is not None and current_key != previous_key:
                reduce(previous_key, value_list, file_out)
                value_list.clear()

            value_list.append(value)
            previous_key = current_key

        # When we reach the end of the file, reduce final unique key.
        reduce(previous_key, value_list, file_out)
