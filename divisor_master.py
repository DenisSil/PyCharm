# Первая функция

def prime(text):
  numb = copy.deepcopy(text.split())
  prime_numbers = []
  dividers = {}
  for i in range(len(numb)):
    number = int(numb[i])
    dividers[number] = 1
    for n in range(2,int(number) + 1):    
      x = number % n
      if x == 0:
        dividers[number] += 1
  else:
    number = list(dividers.keys())
    for i in number:
      if  dividers[i] == 2:
        prime_numbers.append(i)
    else:
      prime_numbers = [i for i in prime_numbers if i != 1]
      return prime_numbers
# print(prime('668 431 386 107 93 423 974 836 474 428 7 142 172 808 93 135 926 362 266 239 548 802 835'))
# Выход: [431, 107, 7, 239]

# Вторая фунция

def prime_dividers(text):
  not_prime_numbers = [1,4,6,9]
  numbers = copy.deepcopy(text.split())
  dividers = {}
  for i in range(len(numbers)):
    numb = int(numbers[i])
    dividers[numb] = []
    for s in range(1,int(numb) + 1):   
      x = numb % s
      if x == 0:
        dividers[numb].append(s)
  else:
    numb = dividers.keys()
    for i in numb:
      number_list = dividers[i]
      number_list = [l for l in number_list if l != not_prime_numbers]
      dividers[i] = number_list
      for n in range(len(number_list)):
        number = int(number_list[n])
        m = 0
        for s in range(1,number + 1):
          x = number % s
          if x == 0:
            m += 1
            if m > 2:
              number_list[n] = ''
    else:
      x = list(dividers.keys())
      for i in x:
        dividers[i] = [i for i in dividers[i] if i != '']
      else:

        for i in x:
          list_numb = dividers[i] 
          max_number = 0
          for n in list_numb:
            if max_number < int(n):
              max_number = n
          else:
            dividers[i] = max_number
        else:  
          return dividers
          
# print(prime_dividers('668 431 386 107 93 423 974 836 474 428 7 142 172 808 93 135 926 362 266 239 548 802 835')
# Выход: {668: 167, 431: 431, 386: 386, 107: 107, 93: 93, 423: 47, 974: 974, 836: 418, 474: 6, 428: 107, 7: 7, 142: 142, 172: 43, 808: 8, 135: 9, 926: 926, 362: 362, 266: 14, 239: 239, 548: 137, 802: 802, 835: 835} 
