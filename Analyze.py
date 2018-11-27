import numpy as np

def createMatrix(filename, numLines):
    f = open(filename)
    header = next(f)
    header = header.split()
    data = []
    output = []
    for line in f:
        line = line.split()
        for each in line[1:]:
            each = int(each)
            data.append(each)
        output.append(int(line[0]))
    inputMat = np.array(data).reshape(numLines, len(header) - 1)
    outputMat = np.array(output).reshape(len(output), 1)
    x = np.linalg.lstsq(inputMat, outputMat, rcond = 0)
    return(x[0])
  
if __name__ == '__main__':
    x = createMatrix("FifaData", 48)
    print(x)
