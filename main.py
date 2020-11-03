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

def reconstruct(file, lst):
    for pos, delta in lst:
        file.seek(pos)
        print(file.read(delta), end='\n---\n')
    return

if __name__ == '__main__':

    file_name = pathlib.Path(sys.argv[1])
    par_start = []
    paragraph = True

    tmp = 0
    pos = 0
    delta = 0
    with open(file_name, 'r') as f:
        line = f.readline()
        while line:
            if paragraph:
                # end of a paragraph
                if line is "\n":
                    #delta = tmp - pos
                    paragraph = False
                else:
                    delta = tmp - pos #extra symbols related to number of read lines
                    # else continue in same mode, reading
            else:
                if line is "\n":
                    # delta = tmp - pos
                    pass
                else:
                    par_start.append((pos, delta))
                    pos = tmp
                    paragraph = True

            #position after reading line
            tmp = f.tell()
            line = f.readline()

        paragraph = False
        par_start.append((pos, delta))

        print(par_start)
        reconstruct(f, shuffle(par_start))







