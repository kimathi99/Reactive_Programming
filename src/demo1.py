# first  demo  
from reactivex import create

def push_user_input_strings(observer, scheduler):
    while True:
        user_input = input("Enter a string (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        observer.on_next(user_input)

    observer.on_completed()

source = create(push_user_input_strings)

source.subscribe(
    on_next=lambda i: print("Received {0}".format(i)),
    on_error=lambda e: print("Error Occurred: {0}".format(e)),
    on_completed=lambda: print("Done!"),
)
