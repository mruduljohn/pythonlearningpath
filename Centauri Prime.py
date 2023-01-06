def isvowel(a):
    if a in ('a','e','i','o','u','A','E','I','O','U'):
        return True

def getRuler(x):
    last_letter = x[-1]
    if isvowel(last_letter):
        return "Alice"
    if ( last_letter == "y" or last_letter == "Y" ):
        return "Nobody"
    return "Bob"

if __name__ == '__main__':
    T =input()
    for i in range(int(T)):
      kingdom = input()
      print("Case #{}: {} is ruled by {}".format(i+1, kingdom, getRuler(kingdom)))
