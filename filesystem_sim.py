from models import FileSystem


def main():
    fs = FileSystem()

    # Read and process the file one line at a time to simulate a user
    # running these commands at a terminal
    with open('./command_input.txt', 'r') as commands:
        for command in commands:
            print(fs.process_command(command).strip('\n'))


main()
