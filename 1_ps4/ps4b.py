# Problem Set 4B
# Name: Ayush Nayak
# Collaborators: None
# Time Spent: 0:15
# Late Days Used: 0

import random

class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has one attribute:
            the message text
        '''
        self.text = input_text

    def __repr__(self):
        '''
        Returns a human readable representation of the object

        Returns: (string) A representation of the object
        '''
        #DO NOT CHANGE
        return f'''Message('{self.get_text()}')'''

    def get_text(self):
        '''
        Used to access the message text outside of the class

        Returns: (string) the message text
        '''
        return self.text

    def shift_char(self, char, shift):
        '''
        Used to shift a character as described in the pset handout

        char (string): the single character to shift.
                    ASCII value in the range: 32<=ord(char)<=126
        shift (int): the amount to shift char ASCII value up by

        Returns: (string) the shifted character with ASCII value in the range [32, 126]
        '''
        return chr((ord(char) + shift - 32) % 95 + 32)

    def apply_pad(self, pad):
        '''
        Used to calculate the ciphertext produced by applying a one time pad to the message text.
        For each character in the text at index i shift that character by
            the amount specified by pad[i]

        pad (list of ints): a list of integers used to encrypt the message text
                        len(pad) == len(the message text)

        Returns: (string) The ciphertext produced using the one time pad
        '''
        ciphertext = ''
        for i in range(len(self.text)):
            ciphertext += self.shift_char(self.text[i], pad[i])
        return ciphertext

class PlaintextMessage(Message):
    def __init__(self, input_text, pad=None):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        pad (list of ints OR None): the pad to encrypt the input_text or None if left empty
            if pad!= None then len(pad) == len(self.input_text)
            save as a COPY

        A PlaintextMessage object inherits from Message. It has three attributes:
            the message text
            the pad (list of integers, determined by pad
                or generated randomly using self.generate_pad() if pad == None)
            the ciphertext (string, input_text encrypted using the pad)
        '''
        super().__init__(input_text)
        if pad == None:
            self.pad = self.generate_pad()
        else:
            self.pad = pad[:]

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''PlaintextMessage('{self.get_text()}', {self.get_pad()})'''

    def generate_pad(self):
        '''
        Generates a one time pad which can be used to encrypt the message text.

        The pad should be generated as follows:
            Make a new list
            For each character in the message, choose a random number n in the range [0, 110)
            Add n to this new list    

        Returns: (list of integers) the new one time pad
                    len(pad) == len(message text)
        '''
        pad = []
        for i in range(len(self.text)):
            pad.append(random.randint(0, 109))
        return pad

    def get_pad(self):
        '''
        Used to safely access your one time pad outside of the class

        Returns: (list of integers) a COPY of your pad
        '''
        return self.pad[:]

    def get_ciphertext(self):
        '''
        Used to access the ciphertext produced by applying the pad to the message text

        Returns: (string) the ciphertext
        '''
        return self.apply_pad(self.pad)

    def change_pad(self, new_pad):
        '''
        Changes the pad used to encrypt the message text and updates any other
        attributes that are determined by the pad.

        new_pad (list of ints): the new one time pad that should be associated with this message.
            len(new_pad) == len(the message text)
            save as a COPY

        Returns: nothing
        '''
        self.pad = new_pad[:]

class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the ciphertext of the message

        an EncryptedMessage object inherits from Message. It has one attribute:
            the message text (ciphertext)
        '''
        super().__init__(input_text)


    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''EncryptedMessage('{self.get_text()}')'''

    def decrypt_message(self, pad):
        '''
        Decrypts the message text that was encrypted with pad as described in the writeup

        pad (list of ints): the new one time pad used to encrypt the message.
            len(pad) == len(the message text)

        Returns: a PlaintextMessage intialized using the decrypted message and the pad
        '''
        plaintext = ''
        for i in range(len(self.text)):
            plaintext += self.shift_char(self.text[i], -pad[i])
        return PlaintextMessage(plaintext, pad)
    
