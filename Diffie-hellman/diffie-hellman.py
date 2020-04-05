import get_prime
import random

def dh(prime_size, N):
    p = get_prime.generate_prime_number(prime_size)
    g = get_prime.findPrimitive(p)
    print("\ng: ",g,"\np: ",p)

    alice, bob = random.randint(2, N), random.randint(2, N)
    while(alice == bob):
        alice, bob = random.randint(2, N), random.randint(2, N)

    BOB   = pow(g, bob, p)
    ALICE = pow(g, alice, p)

    print("\nbob choose: ", bob,"\nalice choose: ",alice)
    print("\nBob computes: ", BOB)
    print("\nALICE computes: ", ALICE)

    print("\n<---Bob and Alice exchange key --->")

    Alice = pow(BOB, alice, p)
    Bob   = pow(ALICE, bob, p)

    print("\nBoth Alice and Bob have arrived at the same value: ",Alice," - ",Bob)

if __name__ == "__main__":
    dh(12,100)
