def makeStackTraceReadable():
    with open('input.txt', 'r') as f:
        stack_trace = f.read().strip()

    lines = stack_trace.split('|')

    with open('output.txt', 'w') as f:
        for line in lines:
            if line.strip().startswith('at'):
                f.write('   ' + line.strip() + '\n')
            else:
                f.write(line.strip() + '\n')


if __name__ == "__main__":
    makeStackTraceReadable()
