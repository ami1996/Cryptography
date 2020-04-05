import hashlib, binascii, get_prime, sys

def gcd(a,b):
    res =  a if b==0 else gcd(b, a%b)
    return res

def get_e(phi_N):
    for e in range(2,phi_N):
        if gcd(e,phi_N)== 1:
            return e

def get_d(e, phi_N):
    d = get_prime.extended(e, phi_N)[1]
    if d == -1:
        print("\nInverse of e not possible in modulo phi_n")
        sys.exit(0)
    if d < 0:
        d = phi_N + d
    return d

def get_primes():
    p, q = get_prime.generate_prime_number(), get_prime.generate_prime_number()
    while (p == q):
        p, q = get_prime.generate_prime_number(), get_prime.generate_prime_number()
    return (p, q)

def print_all(phi_N, p, q, N, d, e, temp_m, m,m_1,encrypted_text,decrypted_text):
    print("\nphi_N : ",phi_N,"\np: ", p,"\nq: ",q,"\nN: ",N)
    print("\nprivate key: ", d)
    print("\npublic key: ", e)
    print("\nMessage is: ",temp_m)
    print("\nascii form data: ",m)
    print("\nplan text integer is: ",m_1)
    print('\nencrypted text integer:  ',encrypted_text)
    print('\ndecrypted text integer:  ', decrypted_text)
    print('\nmessage: ', binascii.unhexlify(hex(decrypted_text)[2:]).decode())


def digital_rsa(file):
    p, q           = get_primes()
    N              = p * q
    phi_N          = (p-1) * (q-1)
    e              = get_e(phi_N)
    d              = get_d(e, phi_N)
    temp           = open(file, 'r') #input from file
    temp_m         = temp.read()
    m              = binascii.hexlify(temp_m.encode())
    m_1            = int(m,16)
    hash_msg       = hashlib.sha256(temp_m.encode()).hexdigest()
    hash_msg_int   = int(hash_msg, 16)
    enc_hash_int   = pow(hash_msg_int, e ,N)
    dec_hash_int   = pow(enc_hash_int, d, N)

    print("\nRSA digital signature")

    print("\nhash data: ", hash_msg)
    print("\ninteget hash data: ", hash_msg_int)
    print("\nencrypted hash digest: ", enc_hash_int)

    if dec_hash_int == hash_msg_int:
        print("\ndecrypt hash digest: ", dec_hash_int)

    #print_all(phi_N, p, q, N, d, e, temp_m, m,m_1)

def rsa(file):
    p, q           = get_primes()
    N              = p * q
    phi_N          = (p-1) * (q-1)
    e              = get_e(phi_N)
    d              = get_d(e, phi_N)
    temp           = open(file, 'r') #input from file
    temp_m         = temp.read()
    m              = binascii.hexlify(temp_m.encode())
    m_1            = int(m,16)
    encrypted_text = pow(m_1, e, N)
    decrypted_text = pow(encrypted_text, d, N)
    print("\nRSA Encryption Decryption")
    print_all(phi_N, p, q, N, d, e, temp_m, m,m_1,encrypted_text,decrypted_text)

if __name__ == "__main__":
    file  = "input.txt"
    rsa(file)
    digital_rsa(file)
