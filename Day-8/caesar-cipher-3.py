alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

def caesar(text, shift, direction):
  cipher_text = ""
  for letter in text:
    position = alphabet.index(letter)
    if direction == "encode":
      new_position = position + shift
    if direction == "decode":
      new_position = position - shift
    cipher_text += alphabet[new_position]
  print(f"The {direction}d text is {cipher_text}")


caesar(text, shift, direction)
