from models import FileSystem


def main():
    fs = FileSystem()

    print(fs.process_command('CREATE pugs'))
    print(fs.process_command('CREATE pugs/stella'))
    print(fs.process_command('DELETE pugs/stella'))
    print(fs.process_command('DELETE pugs/foo'))

    print(fs.process_command('LIST'))

    # Read and process the file one line at a time to simulate a user
    # running these commands at a terminal
    # with open('./command_input.txt', 'r') as commands:
    #     for command in commands:
    #         print(fs.process_command(command))


main()
