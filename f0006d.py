helyezés = int(input('Hányadik helyezést értél el? '))
if helyezés == 1:
  kiírandó = 'Arany érmes vagy.'
elif helyezés == 2:
  kiírandó = 'Ezüst érme vagy.'
elif helyezés == 3:
  kiírandó = 'Bronz érmes vagy.'
print(kiírandó)