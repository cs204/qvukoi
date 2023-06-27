def main():
    s = input()
    s2 = convert(s)
    print(s2)

def convert(s):
    s = s.replace(":)", "\U0001F642")
    s = s.replace(":(", "\U0001F641")
    return s

main()