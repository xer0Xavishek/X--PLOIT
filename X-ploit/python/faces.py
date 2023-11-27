def main():
    s = input()
    T=convert(s)
    print(T)

def convert(s):
    s = s.replace(":)","🙂").replace(":(","🙁")
    return s

main()