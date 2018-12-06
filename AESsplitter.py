HOST = '142.93.221.154'
PORT = 1234
welcomeplain = pad('Welcome!!')

p = remote(HOST, PORT)
solve_proof(p)

# get welcome
welcome = p.recvline(keepends=False)
print 'Welcome:', welcome
welcome_dec = base64.b64decode(welcome)
welcomeblocks = blockify(welcome_dec, 16)
