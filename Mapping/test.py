import multiprocessing

# Define a function that increments a shared variable
def increment_shared_variable(shared_variable):
    for _ in range(1000000):
        shared_variable.value += 1

# Define the shared variable
shared_variable = multiprocessing.Value('i', 0)

# Create two processes and pass the shared variable as an argument
process1 = multiprocessing.Process(target=increment_shared_variable, args=(shared_variable,))
process2 = multiprocessing.Process(target=increment_shared_variable, args=(shared_variable,))

# Start the processes
process1.start()
process2.start()

# Wait for the processes to finish
process1.join()
process2.join()

print("Final value of shared_variable:", shared_variable.value)
