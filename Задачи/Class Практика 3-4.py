class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def __do(self, letter, shift):
        letter = letter.lower()
        if letter not in self.alphabet:
            return letter
        
        index = self.alphabet.index(letter)
        summ = index + shift
        length = len(self.alphabet)

        if summ >= length:
            summ = summ - length
            return self.alphabet[summ]

        return self.alphabet[summ]

    def cipher(self, original_text: str, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        result = []
        for letter in original_text:
            result.append(self.__do(letter, shift))
        return ''.join(result)


    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        result = []
        
        for letter in cipher_text:
            result.append(self.__do(letter, -shift))
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))

print(cipher_master.decipher(
    cipher_text='Уфмьпт фиёав ё ьмшфтёдсстр ёмзи. Одкицхг, сдх фдххофяпм!',
    shift=4
))