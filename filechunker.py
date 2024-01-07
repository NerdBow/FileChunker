import os

class FileChunker:
    def __init__(self, chunk_size=1024 * 1024):  # 1 MB as placeholder
        self.chunk_size = chunk_size

    def chunk_file(self, input_file, output_directory):
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        with open(input_file, 'rb') as file:
            chunk_number = 1
            while True:
                chunk_data = file.read(self.chunk_size)
                if not chunk_data:
                    break  

                output_file = os.path.join(output_directory, f'chunk_{chunk_number}.bin')
                with open(output_file, 'wb') as output:
                    output.write(chunk_data)

                chunk_number += 1

if __name__ == "__main__":
    # Example usage:
    input_file_path = 'path/to/input/file.txt'
    output_directory_path = 'path/to/output/directory'

    chunker = FileChunker()
    chunker.chunk_file(input_file_path, output_directory_path)
