from closure.closure import Closure
from incur_closure.incur_closure import Incur_closure

arr = [1,2,3]   

m = Closure()

[m.indie_method(num) for num in arr]


# def make_counter(para):
    
#     count = para

# # This method is to store the state
#     def inner():

#         nonlocal count
#         count += 1
#         return count

#     return inner


# # def closure(
# #     self, 
# #     init_state,
# #     enclosed_state = []):
    
# #     if init_state is None:
# #         return enclosed_state
# #     else: 
# #         enclosed_state.append(init_state)   

#         # This method is to store the state
#         # similar to this stored the state => self.closure(enclosed_state)
# #         return self.closure(init_state, enclosed_state)


# counter = make_counter(10)

# c = counter()
# print(c)

# c = counter()
# print(c)

# c = counter()
# print(c)