def print_step(step_name):
    print()
    print(f"**** Step {step_name} ****")
    print()



def file_to_list(filepath):
    with open(filepath) as f:
        return f.read().splitlines()


