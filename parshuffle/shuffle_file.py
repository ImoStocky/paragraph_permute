import pathlib
import sys
import random


def shuffle(original):
    copy = original.copy()
    shuffled = []
    for x in range(len(copy)):
        idx = random.randint(0, len(copy) - 1)
        shuffled.append(copy[idx])
        copy.pop(idx)
    return shuffled


def reconstruct(file, lst, out_file=sys.stdout):
    for x in range(len(lst), 0, -1):
        pos, delta = lst[x-1]
        file.seek(pos)
        end = '\n\n'
        if x == 1:
            end = "\n"
        print(file.read(delta), end=end, file=out_file)
    return


def read_index(file):
    par_start = []
    paragraph = True

    tmp = 0
    pos = 0
    delta = 0
    par_lines_cnt = 0

    line = file.readline()
    while line:
        if paragraph:
            if line is "\n":
                # end of a paragraph
                paragraph = False

            else:
                # calculate delta, based of number of lines ending with "\n" subtract extra length
                # "\n" is two symbols "\r\l" - seek offset is therefore 2, but during read "\n" is counted as one
                par_lines_cnt += (1 if "\n" in line else 0)
                delta = tmp - pos + len(line) - par_lines_cnt

        else:
            if line is "\n":
                pass

            else:
                par_start.append((pos, delta))
                pos = tmp
                par_lines_cnt = (1 if "\n" in line else 0)
                paragraph = True

        #position after reading line
        tmp = file.tell()
        line = file.readline()

    par_start.append((pos, delta))
    return par_start


def shuffle_file(input_fname, output_fname):

    file_name = pathlib.Path(input_fname)
    with open(file_name, "r") as file:
        paragraphs = read_index(file)

        if output_fname is None:
            reconstruct(file, shuffle(paragraphs), sys.stdout)

        else:
            out_file_name = pathlib.Path(output_fname)
            if pathlib.Path(output_fname).name is '':
                out_file_name = file_name.with_name(file_name.stem+"_shuffled.txt")

            with open(out_file_name, "w") as f_out:
                reconstruct(file, shuffle(paragraphs), f_out)













