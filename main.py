def pasword(n, pas, drop):
  a=[]
  for i in pas:
    if ord(i) not in range(48,58) and n==0:
      a.append(chr(ord(i)+drop))
    elif ord(i) not in range(48,58) and n==1:
      a.append(chr(ord(i)-drop))
  return(''.join(a))
print("\nHi, This is a Caesar Cipher Encoder and Decoder\n")
c=0    
while(c!=1):
  try:
    n=int(input("\nEnter 0 for Encoder and 1 for Decoder:\t"))
  except:
    print("\nEnter 1 or 0")
  if n==0:
    c=1
    print("\nWelcome to Encoder")
    print("\n\tIt takes a password(string) and a shift(integer) as input,")
    print("\n\tand output the encoded ciphered text")
    print('\n\tTry entering a password below and shift value to see encoded text\n')
    pas=input("\nEnter password:\t")
    drop=int(input("\nEnter the shift:\t"))
    print("\nOutput\nEncoded text:\t",pasword(n,pas,drop))
  elif(n==1):
    c=1
    print("\n\tWelcome to Decoder")
    print("\n\tIt takes an encoded password(string) and a shift(integer) as input,")
    print("\n\tand output the decoded text")
    print('\n\tTry entering an encoded text below and shift value to see decoded text\n')
    pas=input("\nEnter password:\t")
    drop=int(input("\nEnter the shift:\t"))
    print("\nOutput\nDecoded text:\t",pasword(n,pas,drop))
