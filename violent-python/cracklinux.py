import crypt
from optparse import OptionParser
import sys

def get_unencrypted_pass(encrypted_pass, dict_filename):
    salt = encrypted_pass[0:2]
    dict_file = open(dict_filename)
    for word in dict_file.readlines():
        word = word.strip()
        crypt_word = crypt.crypt(word, salt)
        if (crypt_word == encrypted_pass):
            return word
        return False

def main():
    parser = OptionParser()
    parser.add_option("-d", "--dict", dest="dictionary_filename",
                  help="the dictionary file to use", metavar="FILE")
    parser.add_option("-p", "--pass", dest="pass_filename",
                  help="the encrypted passwords file to use", metavar="FILE")
    (options, args) = parser.parse_args()

    if len(args) < 2:
        parser.error('Not enough options stated')

    passwords = open(pass_filename)
    for line in passwords.readlines():
        if ':' in line:
            user = line.split(':')[0]
            encrypted_pass = line.split(':')[1]
            result = get_unencrypted_pass(encrypted_pass, dict_filename)
            if result:
                print('%s : %s' % (user, result))

if __name__ == '__main__':
    main()