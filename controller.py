import view
import model_sorting

def my_start():
    while True:
        op = view.op()
        if op ==1: 
            view.add_worker()

        elif op==2: 
            view.print_table()

        elif op==3: 
            view.print_names()

        elif op==4: 
            model_sorting.sorting_names()
        
        elif op==5: 
            model_sorting.sorting_id()
        
        elif op== 6:
            break

