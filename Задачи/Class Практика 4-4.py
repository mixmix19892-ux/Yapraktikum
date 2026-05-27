class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt = True):
        result = []
        if not is_encrypt:
            shift = -shift

        for letter in text:
            letter = letter.lower()
            if letter not in self.alphabet:
                result.append(letter)
                continue
            
            index = self.alphabet.index(letter)
            summ = index + shift
            length = len(self.alphabet)

            if summ >= length:
                summ = summ - length
                result.append(self.alphabet[summ])
            else:
                result.append(self.alphabet[summ])
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))

print(cipher_master.process_text(
    text='Уфмьпт фиёав ё ьмшфтёдсстр ёмзи. Одкицхг, сдх фдххофяпм!',
    shift=4,
    is_encrypt=True
))