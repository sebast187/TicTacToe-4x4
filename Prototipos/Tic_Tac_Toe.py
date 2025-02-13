def main():
  tic = ['', '', '']
  tac = ['', '', '']
  toe = ['', '', '']
  ttt = []
  ttt.append(tic)
  ttt.append(tac)
  ttt.append(toe)
  contx = 0
  conto = 0
  contg = 0
  tttmore = '\n\'{}\'\t\'{}\'\t\'{}\'\n\n\'{}\'\t\'{}\'\t\'{}\'\n\n\'{}\'\t\'{}\'\t\'{}\'\n'
  tttmore = tttmore.format(ttt[0][0], ttt[0][1], ttt[0][2], ttt[1][0], ttt[1][1], ttt[1][2], ttt[2][0], ttt[2][1], ttt[2][2])
  print(tttmore)
  while True:
    ficha = input('Turno: ')
    if ficha == 'X' or ficha == 'x':
      lugar = int(input('Seleccione del 1-9 para poner su ficha: '))
      lugarc = lugar % 3
      lugarr = lugar
      if lugarc == 0:
        lugarc = 3
      lugarc = lugarc - 1
      if lugar >= 1 and lugar <= 3:
        lugarr = 0
      if lugar >= 4 and lugar <= 6:
        lugarr = 1
      if lugar >= 7 and lugar <= 9:
        lugarr = 2
      if ttt[lugarr][lugarc] == '':
        ttt[lugarr][lugarc] = 'X'
        tttmore = '\n\'{}\'\t\'{}\'\t\'{}\'\n\n\'{}\'\t\'{}\'\t\'{}\'\n\n\'{}\'\t\'{}\'\t\'{}\'\n'
        tttmore = tttmore.format(ttt[0][0], ttt[0][1], ttt[0][2], ttt[1][0], ttt[1][1], ttt[1][2], ttt[2][0], ttt[2][1], ttt[2][2])
        print(tttmore)
      else:
        print('\nEsta ficha ya esta ocupada\n')
    if ficha == 'O' or ficha == 'o':
      lugar = int(input('Seleccione del 1-9 para poner su ficha: '))
      lugarc = lugar % 3
      lugarr = lugar
      if lugarc == 0:
        lugarc = 3
      lugarc = lugarc - 1
      if lugar >= 1 and lugar <= 3:
        lugarr = 0
      if lugar >= 4 and lugar <= 6:
        lugarr = 1
      if lugar >= 7 and lugar <= 9:
        lugarr = 2
      if ttt[lugarr][lugarc] == '':
        ttt[lugarr][lugarc] = 'O'
        tttmore = '\n\'{}\'\t\'{}\'\t\'{}\'\n\n\'{}\'\t\'{}\'\t\'{}\'\n\n\'{}\'\t\'{}\'\t\'{}\'\n'
        tttmore = tttmore.format(ttt[0][0], ttt[0][1], ttt[0][2], ttt[1][0], ttt[1][1], ttt[1][2], ttt[2][0], ttt[2][1], ttt[2][2])
        print(tttmore)
      else:
        print('\nEsta ficha ya esta ocupada\n')
    for i in range(len(ttt)):
      for m in range(len(ttt[i])):
        if ttt[i][m] == 'X':
          contx += 1
        if ttt[i][m] == 'O':
          conto += 1
      if contx == 3:
        return print('\nLas X ganaron\n')
      contx = 0
      if conto == 3:
        return print('\nLas O ganaron\n')
      conto = 0
    for i in range(len(ttt)):
      for m in range(len(ttt[i])):
        if ttt[m][i] == 'X':
          contx += 1
        if ttt[m][i] == 'O':
          conto += 1
      if contx == 3:
        return print('\nLas X ganaron\n')
      contx = 0
      if conto == 3:
        return print('\nLas O ganaron\n')
      conto = 0
    if ttt[0][0] == ttt[1][1] == ttt[2][2]:
      if ttt[1][1] == 'X':
        return print('\nLas X ganaron\n')
      elif ttt[1][1] == 'O':
        return print('\nLas O ganaron\n')
    elif ttt[0][2] == ttt[1][1] == ttt[2][0]:
      if ttt[1][1] == 'X':
        return print('\nLas X ganaron\n')
      elif ttt[1][1] == 'O':
        return print('\nLas O ganaron\n')
    for s in range(len(ttt)):
      for a in range(len(ttt[s])):
        if ttt[s][a] != '':
          contg += 1
    if contg == 9:
      return print('\nGato\n')
    else:
      contg = 0

main()