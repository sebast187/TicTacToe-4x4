import random

def main():
    c = input('Enter the number of players that will play: ')
    if c == '1':
      tic = ['', '', '', '', '']
      tac = ['', '', '', '', '']
      toe = ['', '', '', '', '']
      tic2 = ['', '', '', '', '']
      tac2 = ['', '', '', '', '']
      ttt = []
      ttt.append(tic)
      ttt.append(tac)
      ttt.append(toe)
      ttt.append(tic2)
      ttt.append(tac2)
      contx = 0
      conto = 0
      contg = 0
      r = 0
      tttmore = '\n\t1\t2\t3\t4\t5\n\n0 +\t\'{0}\'\t\'{1}\'\t\'{2}\'\t\'{3}\'\t\'{4}\'\n\n5 +\t\'{5}\'\t\'{6}\'\t\'{7}\'\t\'{8}\'\t\'{9}\'\n\n10 +\t\'{10}\'\t\'{11}\'\t\'{12}\'\t\'{13}\'\t\'{14}\'\n\n15 +\t\'{15}\'\t\'{16}\'\t\'{17}\'\t\'{18}\'\t\'{19}\'\n\n20 +\t\'{20}\'\t\'{21}\'\t\'{22}\'\t\'{23}\'\t\'{24}\'\n'
      tttmore = tttmore.format(ttt[0][0], ttt[0][1], ttt[0][2], ttt[0][3], ttt[0][4], ttt[1][0], ttt[1][1], ttt[1][2], ttt[1][3], ttt[1][4], ttt[2][0], ttt[2][1], ttt[2][2], ttt[2][3], ttt[2][4], ttt[3][0], ttt[3][1], ttt[3][2], ttt[3][3], ttt[3][4], ttt[4][0], ttt[4][1], ttt[4][2], ttt[4][3], ttt[4][4])
      print(tttmore)
      while True:
        if r % 2 == 0:
          while True:
            lugar = int(input('\nFicha \'X\'\nSeleccione del 1-25 para poner su ficha: '))
            lugarc = lugar % 5
            lugarr = lugar
            if lugarc == 0:
              lugarc = 5
            lugarc = lugarc - 1
            if lugar >= 1 and lugar <= 5:
              lugarr = 0
            if lugar >= 6 and lugar <= 10:
              lugarr = 1
            if lugar >= 11 and lugar <= 15:
              lugarr = 2
            if lugar >= 16 and lugar <= 20:
              lugarr = 3
            if lugar >= 21 and lugar <= 25:
              lugarr = 4
            if ttt[lugarr][lugarc] == '':
              ttt[lugarr][lugarc] = 'X'
              tttmore = '\n\t1\t2\t3\t4\t5\n\n0 +\t\'{0}\'\t\'{1}\'\t\'{2}\'\t\'{3}\'\t\'{4}\'\n\n5 +\t\'{5}\'\t\'{6}\'\t\'{7}\'\t\'{8}\'\t\'{9}\'\n\n10 +\t\'{10}\'\t\'{11}\'\t\'{12}\'\t\'{13}\'\t\'{14}\'\n\n15 +\t\'{15}\'\t\'{16}\'\t\'{17}\'\t\'{18}\'\t\'{19}\'\n\n20 +\t\'{20}\'\t\'{21}\'\t\'{22}\'\t\'{23}\'\t\'{24}\'\n'
              tttmore = tttmore.format(ttt[0][0], ttt[0][1], ttt[0][2], ttt[0][3], ttt[0][4], ttt[1][0], ttt[1][1], ttt[1][2], ttt[1][3], ttt[1][4], ttt[2][0], ttt[2][1], ttt[2][2], ttt[2][3], ttt[2][4], ttt[3][0], ttt[3][1], ttt[3][2], ttt[3][3], ttt[3][4], ttt[4][0], ttt[4][1], ttt[4][2], ttt[4][3], ttt[4][4])
              print(tttmore)
              break
            else:
              print('\nEsta ficha ya esta ocupada\n')
        else:
          while True:
            ran = random.randint(1, 25)
            lugar = ran
            lugarc = lugar % 5
            lugarr = lugar
            if lugarc == 0:
              lugarc = 5
            lugarc = lugarc - 1
            if lugar >= 1 and lugar <= 5:
              lugarr = 0
            if lugar >= 6 and lugar <= 10:
              lugarr = 1
            if lugar >= 11 and lugar <= 15:
              lugarr = 2
            if lugar >= 16 and lugar <= 20:
              lugarr = 3
            if lugar >= 21 and lugar <= 25:
              lugarr = 4
            if ttt[lugarr][lugarc] == '':
              ttt[lugarr][lugarc] = 'O'
              tttmore = '\n\t1\t2\t3\t4\t5\n\n0 +\t\'{0}\'\t\'{1}\'\t\'{2}\'\t\'{3}\'\t\'{4}\'\n\n5 +\t\'{5}\'\t\'{6}\'\t\'{7}\'\t\'{8}\'\t\'{9}\'\n\n10 +\t\'{10}\'\t\'{11}\'\t\'{12}\'\t\'{13}\'\t\'{14}\'\n\n15 +\t\'{15}\'\t\'{16}\'\t\'{17}\'\t\'{18}\'\t\'{19}\'\n\n20 +\t\'{20}\'\t\'{21}\'\t\'{22}\'\t\'{23}\'\t\'{24}\'\n'
              tttmore = tttmore.format(ttt[0][0], ttt[0][1], ttt[0][2], ttt[0][3], ttt[0][4], ttt[1][0], ttt[1][1], ttt[1][2], ttt[1][3], ttt[1][4], ttt[2][0], ttt[2][1], ttt[2][2], ttt[2][3], ttt[2][4], ttt[3][0], ttt[3][1], ttt[3][2], ttt[3][3], ttt[3][4], ttt[4][0], ttt[4][1], ttt[4][2], ttt[4][3], ttt[4][4])
              print('\nFicha \'O\'')
              print(tttmore)
              break
        for i in range(len(ttt)):
          for m in range(len(ttt[i])):
            if ttt[i][m] == 'X':
              contx += 1
            else:
              if contx == 4:
                return print('\nLas X ganaron\n')
              contx = 0
              if conto == 4:
                return print('\nLas O ganaron\n')
              conto = 0
            if ttt[i][m] == 'O':
              conto += 1
            else:
              if contx == 4:
                return print('\nLas X ganaron\n')
              contx = 0
              if conto == 4:
                return print('\nLas O ganaron\n')
              conto = 0
        for i in range(len(ttt)):
          for m in range(len(ttt[i])):
            if ttt[m][i] == 'X':
              contx += 1
            else:
              if contx == 4:
                return print('\nLas X ganaron\n')
              contx = 0
              if conto == 4:
                return print('\nLas O ganaron\n')
              conto = 0
            if ttt[m][i] == 'O':
              conto += 1
            else:
              if contx == 4:
                return print('\nLas X ganaron\n')
              contx = 0
              if conto == 4:
                return print('\nLas O ganaron\n')
              conto = 0
        if ttt[0][0] == ttt[1][1] and ttt[2][2] == ttt[3][3]:
          if ttt[2][2] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[2][2] == 'O':
            return print('\nLas O ganaron\n')
        elif ttt[0][4] == ttt[1][3] and ttt[2][2] == ttt[3][1]:
          if ttt[2][2] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[2][2] == 'O':
            return print('\nLas O ganaron\n')
        if ttt[1][1] == ttt[2][2] and ttt[3][3] == ttt[4][4]:
          if ttt[2][2] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[2][2] == 'O':
            return print('\nLas O ganaron\n')
        elif ttt[1][3] == ttt[2][2] and ttt[3][1] == ttt[4][0]:
          if ttt[2][2] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[2][2] == 'O':
            return print('\nLas O ganaron\n')
        if ttt[1][0] == ttt[2][1] and ttt[3][2] == ttt[4][3]:
          if ttt[2][1] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[2][1] == 'O':
            return print('\nLas O ganaron\n')
        elif ttt[0][1] == ttt[1][2] and ttt[2][3] == ttt[3][4]:
          if ttt[1][2] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[1][2] == 'O':
            return print('\nLas O ganaron\n')
        if ttt[0][3] == ttt[1][2] and ttt[2][1] == ttt[3][0]:
          if ttt[1][2] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[1][2] == 'O':
            return print('\nLas O ganaron\n')
        elif ttt[1][4] == ttt[2][3] and ttt[3][2] == ttt[4][1]:
          if ttt[2][3] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[2][3] == 'O':
            return print('\nLas O ganaron\n')
        for s in range(len(ttt)):
          for a in range(len(ttt[s])):
            if ttt[s][a] != '':
              contg += 1
        if contg == 25:
          return print('\nGato\n')
        else:
          contg = 0
        r += 1
    elif c == '2':
      tic = ['', '', '', '', '']
      tac = ['', '', '', '', '']
      toe = ['', '', '', '', '']
      tic2 = ['', '', '', '', '']
      tac2 = ['', '', '', '', '']
      ttt = []
      ttt.append(tic)
      ttt.append(tac)
      ttt.append(toe)
      ttt.append(tic2)
      ttt.append(tac2)
      contx = 0
      conto = 0
      contg = 0
      r = 0
      tttmore = '\n\t1\t2\t3\t4\t5\n\n0 +\t\'{0}\'\t\'{1}\'\t\'{2}\'\t\'{3}\'\t\'{4}\'\n\n5 +\t\'{5}\'\t\'{6}\'\t\'{7}\'\t\'{8}\'\t\'{9}\'\n\n10 +\t\'{10}\'\t\'{11}\'\t\'{12}\'\t\'{13}\'\t\'{14}\'\n\n15 +\t\'{15}\'\t\'{16}\'\t\'{17}\'\t\'{18}\'\t\'{19}\'\n\n20 +\t\'{20}\'\t\'{21}\'\t\'{22}\'\t\'{23}\'\t\'{24}\'\n'
      tttmore = tttmore.format(ttt[0][0], ttt[0][1], ttt[0][2], ttt[0][3], ttt[0][4], ttt[1][0], ttt[1][1], ttt[1][2], ttt[1][3], ttt[1][4], ttt[2][0], ttt[2][1], ttt[2][2], ttt[2][3], ttt[2][4], ttt[3][0], ttt[3][1], ttt[3][2], ttt[3][3], ttt[3][4], ttt[4][0], ttt[4][1], ttt[4][2], ttt[4][3], ttt[4][4])
      print(tttmore)
      while True:
        if r % 2 == 0:
          while True:
            lugar = int(input('\nFicha \'X\'\nSeleccione del 1-25 para poner su ficha: '))
            lugarc = lugar % 5
            lugarr = lugar
            if lugarc == 0:
              lugarc = 5
            lugarc = lugarc - 1
            if lugar >= 1 and lugar <= 5:
              lugarr = 0
            if lugar >= 6 and lugar <= 10:
              lugarr = 1
            if lugar >= 11 and lugar <= 15:
              lugarr = 2
            if lugar >= 16 and lugar <= 20:
              lugarr = 3
            if lugar >= 21 and lugar <= 25:
              lugarr = 4
            if ttt[lugarr][lugarc] == '':
              ttt[lugarr][lugarc] = 'X'
              tttmore = '\n\t1\t2\t3\t4\t5\n\n0 +\t\'{0}\'\t\'{1}\'\t\'{2}\'\t\'{3}\'\t\'{4}\'\n\n5 +\t\'{5}\'\t\'{6}\'\t\'{7}\'\t\'{8}\'\t\'{9}\'\n\n10 +\t\'{10}\'\t\'{11}\'\t\'{12}\'\t\'{13}\'\t\'{14}\'\n\n15 +\t\'{15}\'\t\'{16}\'\t\'{17}\'\t\'{18}\'\t\'{19}\'\n\n20 +\t\'{20}\'\t\'{21}\'\t\'{22}\'\t\'{23}\'\t\'{24}\'\n'
              tttmore = tttmore.format(ttt[0][0], ttt[0][1], ttt[0][2], ttt[0][3], ttt[0][4], ttt[1][0], ttt[1][1], ttt[1][2], ttt[1][3], ttt[1][4], ttt[2][0], ttt[2][1], ttt[2][2], ttt[2][3], ttt[2][4], ttt[3][0], ttt[3][1], ttt[3][2], ttt[3][3], ttt[3][4], ttt[4][0], ttt[4][1], ttt[4][2], ttt[4][3], ttt[4][4])
              print(tttmore)
              break
            else:
              print('\nEsta ficha ya esta ocupada\n')
        else:
          while True:
            lugar = int(input('Ficha \'O\'\nSeleccione del 1-25 para poner su ficha: '))
            lugarc = lugar % 5
            lugarr = lugar
            if lugarc == 0:
              lugarc = 5
            lugarc = lugarc - 1
            if lugar >= 1 and lugar <= 5:
              lugarr = 0
            if lugar >= 6 and lugar <= 10:
              lugarr = 1
            if lugar >= 11 and lugar <= 15:
              lugarr = 2
            if lugar >= 16 and lugar <= 20:
              lugarr = 3
            if lugar >= 21 and lugar <= 25:
              lugarr = 4
            if ttt[lugarr][lugarc] == '':
              ttt[lugarr][lugarc] = 'O'
              tttmore = '\n\t1\t2\t3\t4\t5\n\n0 +\t\'{0}\'\t\'{1}\'\t\'{2}\'\t\'{3}\'\t\'{4}\'\n\n5 +\t\'{5}\'\t\'{6}\'\t\'{7}\'\t\'{8}\'\t\'{9}\'\n\n10 +\t\'{10}\'\t\'{11}\'\t\'{12}\'\t\'{13}\'\t\'{14}\'\n\n15 +\t\'{15}\'\t\'{16}\'\t\'{17}\'\t\'{18}\'\t\'{19}\'\n\n20 +\t\'{20}\'\t\'{21}\'\t\'{22}\'\t\'{23}\'\t\'{24}\'\n'
              tttmore = tttmore.format(ttt[0][0], ttt[0][1], ttt[0][2], ttt[0][3], ttt[0][4], ttt[1][0], ttt[1][1], ttt[1][2], ttt[1][3], ttt[1][4], ttt[2][0], ttt[2][1], ttt[2][2], ttt[2][3], ttt[2][4], ttt[3][0], ttt[3][1], ttt[3][2], ttt[3][3], ttt[3][4], ttt[4][0], ttt[4][1], ttt[4][2], ttt[4][3], ttt[4][4])
              print(tttmore)
              break
            else:
              print('\nEsta ficha ya esta ocupada\n')
        for i in range(len(ttt)):
          for m in range(len(ttt[i])):
            if ttt[i][m] == 'X':
              contx += 1
            else:
              if contx == 4:
                return print('\nLas X ganaron\n')
              contx = 0
              if conto == 4:
                return print('\nLas O ganaron\n')
              conto = 0
            if ttt[i][m] == 'O':
              conto += 1
            else:
              if contx == 4:
                return print('\nLas X ganaron\n')
              contx = 0
              if conto == 4:
                return print('\nLas O ganaron\n')
              conto = 0
        for i in range(len(ttt)):
          for m in range(len(ttt[i])):
            if ttt[m][i] == 'X':
              contx += 1
            else:
              if contx == 4:
                return print('\nLas X ganaron\n')
              contx = 0
              if conto == 4:
                return print('\nLas O ganaron\n')
              conto = 0
            if ttt[m][i] == 'O':
              conto += 1
            else:
              if contx == 4:
                return print('\nLas X ganaron\n')
              contx = 0
              if conto == 4:
                return print('\nLas O ganaron\n')
              conto = 0
        if ttt[0][0] == ttt[1][1] and ttt[2][2] == ttt[3][3]:
          if ttt[2][2] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[2][2] == 'O':
            return print('\nLas O ganaron\n')
        elif ttt[0][4] == ttt[1][3] and ttt[2][2] == ttt[3][1]:
          if ttt[2][2] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[2][2] == 'O':
            return print('\nLas O ganaron\n')
        if ttt[1][1] == ttt[2][2] and ttt[3][3] == ttt[4][4]:
          if ttt[2][2] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[2][2] == 'O':
            return print('\nLas O ganaron\n')
        elif ttt[1][3] == ttt[2][2] and ttt[3][1] == ttt[4][0]:
          if ttt[2][2] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[2][2] == 'O':
            return print('\nLas O ganaron\n')
        if ttt[1][0] == ttt[2][1] and ttt[3][2] == ttt[4][3]:
          if ttt[2][1] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[2][1] == 'O':
            return print('\nLas O ganaron\n')
        elif ttt[0][1] == ttt[1][2] and ttt[2][3] == ttt[3][4]:
          if ttt[1][2] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[1][2] == 'O':
            return print('\nLas O ganaron\n')
        if ttt[0][3] == ttt[1][2] and ttt[2][1] == ttt[3][0]:
          if ttt[1][2] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[1][2] == 'O':
            return print('\nLas O ganaron\n')
        elif ttt[1][4] == ttt[2][3] and ttt[3][2] == ttt[4][1]:
          if ttt[2][3] == 'X':
            return print('\nLas X ganaron\n')
          elif ttt[2][3] == 'O':
            return print('\nLas O ganaron\n')
        for s in range(len(ttt)):
          for a in range(len(ttt[s])):
            if ttt[s][a] != '':
              contg += 1
        if contg == 25:
          return print('\nGato\n')
        else:
          contg = 0
        r += 1
    else:
        return print('\n|----- Error -----|\n')

main()


