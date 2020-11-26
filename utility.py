def parse_segment_space(line, index):
    while line[index].isspace():
        index += 1

    buffer = ""
    while index < len(line) and line[index].isspace() == False:
        buffer += line[index]
        index += 1
    return buffer.strip()

def parse_segment_coma(line, index):
    while line[index] == ',':
        index += 1

    buffer = ""
    while index < len(line) and line[index] != ',':
        buffer += line[index]
        index += 1
    return buffer.strip()