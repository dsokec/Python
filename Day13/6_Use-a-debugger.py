# Use a Debugger
# https://pythontutor.com/visualize.html#mode=edit

# ask StackOverflow for help https://stackoverflow.com/questions/tagged/python
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])