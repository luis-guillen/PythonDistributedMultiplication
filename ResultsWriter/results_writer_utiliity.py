import os

class ResultsWriterUtility:
    @staticmethod
    def write_to_text(file_path, headers, data):
        """
        Writes results to a text file, appending them if the file already exists.

        Args:
            file_path (str): Path to the file where results will be written.
            headers (list[str]): List of headers describing the data.
            data (list[str]): List of data corresponding to the headers.
        """
        try:
            # Check if the file exists and is empty
            is_new_file = not os.path.exists(file_path) or os.path.getsize(file_path) == 0

            with open(file_path, 'a') as writer:
                if is_new_file:
                    writer.write("---- Results ----\n")

                writer.write("\nExecution Results:\n")
                for header, value in zip(headers, data):
                    writer.write(f"{header}: {value}\n")
                writer.write("-----------------\n")
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")