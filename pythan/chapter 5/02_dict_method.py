marks = {
"Harry" :100,
"Prince" :23,
"Mithlesh": 34,
0: "Herry"
}
#print(marks.items())
#print(marks.keys())
#print(marks.values())

#marks. update({"harry": 99,"rohan": 67})
#print(marks)

#print(marks.get("Harry2"))#print None

#print(marks["Harry2"])# Return  an error

items = marks.popitem()
print(items)

