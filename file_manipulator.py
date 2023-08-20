import sys

methods = ["reverse", "copy", "duplicate-contents", "replace-string"]

def reverse(inputPath, outputPath):
    with open(inputPath, "r") as f:
        contents = f.read()
    with open(outputPath, "x") as nf:
        reverseContents = contents[::-1]
        nf.write(reverseContents)

def copy(inputPath, outputPath):
    with open(inputPath, "r") as f:
        contents = f.read()
    with open(outputPath, "x") as nf:
        nf.write(contents)

def duplicateContents(inputPath, times):
    with open(inputPath, "r") as f:
        contents = f.read()
    with open(inputPath, "a") as f:
        for i in range(int(times)):
            f.write("\n" + contents)

def replaceString(inputPath, originWord, newWord):
    with open(inputPath, "r") as f:
        contents = f.read()
    with open(inputPath, "w") as f:
        newContents = contents.replace(originWord, newWord)
        f.write(newContents)


if len(sys.argv) < 2 or sys.argv[1] not in methods:
    print("no such method. please check")
    sys.exit(1)

if sys.argv[1] == "reverse":
    reverse(sys.argv[2], sys.argv[3])
if sys.argv[1] == "copy":
    copy(sys.argv[2], sys.argv[3])
if sys.argv[1] == "duplicate-contents":
    duplicateContents(sys.argv[2], sys.argv[3])
if sys.argv[1] == "replace-string":
    replaceString(sys.argv[2], sys.argv[3], sys.argv[4])

