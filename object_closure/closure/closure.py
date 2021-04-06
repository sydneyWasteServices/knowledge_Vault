
class Closure:
    def __init__(self):
        self._closure_state = 0
        
# =============================================
    def indie_method(self, inputState = 0):

        self._closure_state = self.make_counter(inputState) 
        numb = self._closure_state()
        print(numb)
    
    def make_counter(self, para):
        
        count = para

# This method is to store the state
        def inner():

            nonlocal count
            count += 1
            return count

        return inner


# =============================================

    def closure(
        self, 
        init_state,
        enclosed_state = []):
        
        if init_state is None:
            return enclosed_state
        else: 
            enclosed_state.append(init_state)   
            return self.closure(init_state, enclosed_state)

#     routes_id_loc_dict => it would store the previous state, if not pass a new object
#      _get_cells_loc("name", Cell, object)


#     def _get_cells_loc(
#             self,
#             ws_name : str,
#             target_cell: object,
#             routes_id_loc_dict={}):

# if target_cell.value is None:

#     return routes_id_loc_dict

# else:

    # routes_id_loc_dict[route_number] = target_cell

    # new_target_cell = target_cell.offset(column_offset=1)

    # return self._get_cells_loc(ws_name, new_target_cell, routes_id_loc_dict)