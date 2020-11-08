def main():
    # Read and process the file one line at a time to simulate a user
    # running these commands at a terminal
    with open('./command_input.txt', 'r') as commands:
        for command in commands:
            process_command(command)

def process_command(command_str: str) -> str:
    command = tuple([x.strip() for x in command_str.split(' ')])
    
    if command[0] == 'LIST':
        return ''
    if command[0] == 'CREATE':
        pass
    if command[0] == 'MOVE':
        pass
    if command[0] == 'DELETE':
        pass

main()