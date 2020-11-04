import pathlib
import sys
import random


def shuffle(lst):
    shuffled = []
    for x in range(len(lst)):
        idx = random.randint(0, len(lst)-1)
        shuffled.append(lst[idx])
        lst.pop(idx)
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


if __name__ == '__main__':

    file_name = pathlib.Path(sys.argv[1])
    par_start = []
    paragraph = True

    tmp = 0
    pos = 0
    delta = 0
    par_lines_cnt = 0

    with open(file_name, "r") as f:
        line = f.readline()
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
            tmp = f.tell()
            line = f.readline()

        par_start.append((pos, delta))
        #with open(file_name.with_name(file_name.stem+"_shuffled.txt"), "w") as f_out:
        #    reconstruct(f, shuffle(par_start), f_out)
        reconstruct(f, shuffle(par_start))








