import random, string

nombre = 100000

def gen():
    rdm = string.ascii_lowercase + string.digits
    return ''.join(random.choice(rdm) for _ in range(4))

pseudos = [gen() for _ in range(nombre)]

with open("pseudos.txt", "w") as f:
    for pseudo in pseudos:
        f.write(f"{pseudo}\n")
