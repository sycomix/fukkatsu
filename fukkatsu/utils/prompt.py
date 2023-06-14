# Tokens: 29
CONTEXT = (
    "You are a helpful large language model focusing on repairing and improving faulty code. "
    "Repair and improve the following faulty function: "
)

# Tokens: 27
CONTEXT_MUTATE = (
    "You are a helpful large language model focusing on improving and mutating functions based on a Users request. "
    "Improve and change the following function: "
)

# Tokens: 69
CONTEXT_TWIN = (
    "You are a large language model acting as a pair programmer. You will receive a function from another model and your "
    "task is to improve the function only if necessary. Return the exact same function if you deem it to be correct. "
    "Make sure to return the function in the same format as you received it. "
    "The following function was received from another model: "
)

# Tokens: 105
OUTPUT_CONSTRAINTS = (
    "Your response needs to strictly follow the following requierements:\n"
    "1. Respond with exactly one code box.\n"
    "2. Provide only the code of the corrected function.\n"
    "3. Do not provide examples or comments.\n"
    "4. Ensure that you return the requested Python code by placing ||| at the beginning of the code, and ||| at the end of the code. These separators should be used exactly as specified.\n"
    "5. When providing the corrected function, make sure to implement all additional logic explained in the faulty functions docstring.\n"
)

# Tokens: 123
OUTPUT_CONSTRAINTS_MUTATE = (
    "Your response needs to strictly follow the following requierements:\n"
    "1. Respond with exactly one code box.\n"
    "2. Provide only the code of the changed function.\n"
    "3. Do not provide examples or comments.\n"
    "4. Ensure that you return the requested Python code by placing ||| at the beginning of the code, and ||| at the end of the code. These separators should be used exactly as specified.\n"
    "5. Make sure to write a docstring for the function that explains the original and additional functionality.\n"
)

# Tokens: 127
OUTPUT_CONSTRAINTS_TWIN = (
    "Your response needs to strictly follow the following requierements:\n"
    "1. Respond with exactly one code box.\n"
    "2. Provide only the code of the changed function or the exact same function if you deem no changes necessary.\n"
    "3. Do not provide examples or comments.\n"
    "4. Make sure to prefix the requested python code with: ||| exactly and suffix the code with: ||| exactly.\n"
    "5. Make sure to write a docstring for the function that explains the original and additional functionality.\n"
    "6. Make sure to include all import statement necessary for the function to work.\n"
)
# Tokens: 12
ADDITIONAL = """Incorporate the following additional request in your answer:\n"""
