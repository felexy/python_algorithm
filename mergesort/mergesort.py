def mergeSort(numbers):
  """Given a list of number sort and return the array."""
  l = len(numbers)
  if l <= 1:
    return numbers
  
  firstHalf = mergeSort(numbers[:l/2])
  secondHalf = mergeSort(numbers[l/2:])
  numbers = []

  while len(firstHalf) > 0 and len(secondHalf) > 0:
    if firstHalf[0] < secondHalf[0]:
      numbers.append( firstHalf.pop(0) )

    else:
      numbers.append(secondHalf.pop(0))

  return numbers + firstHalf + secondHalf
