#list1 = [1,2,3,4,5]
#list2 = ['one', 'two', 'three', 'four', 'five']

#zipped = list(zip(list1,list2))

#print(zipped)

#unzipped = list(zip(*zipped))

#print(unzipped)

#for (l1, l2) in zip(list1, list2):
  #print(l1)
  #print(l2)

items = ['Apple', 'Banana', 'Orange']
counts = [30, 12, 7]
price = [5, 4, 6]

sentences = []
for (item, count, price) in zip(items, counts, price):
  item, count, price = str(item), str(count), str(price)
  sentence = 'I bought ' + count + ' ' + item + 's @' + price + ' ' + 'Rs. each.'
  sentences.append(sentence)

print(sentences)