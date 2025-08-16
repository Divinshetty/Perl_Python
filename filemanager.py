class FileManager:
    """
    A class to manage text files with basic operations
    """
    def __init__(self, filename, owner, created_date, file_type, max_size):
        """Initialize with 5 attributes"""
        self.__filename = filename  # private attribute
        self.owner = owner          # public attribute
        self._created_date = created_date  # protected attribute
        self.file_type = file_type
        self._max_size = max_size
        self.__content = ""
   
    def read_file(self):
        """Read content from the file"""
        try:
            with open(self.__filename, 'r') as file:
                self.__content = file.read()
            print(f"File {self.__filename} read successfully")
            return self.__content
        except FileNotFoundError:
            print(f"Error: File {self.__filename} not found")
            return ""
   
    def write_file(self, text):
        """Write content to the file"""
        if len(text) > self._max_size:
            print(f"Error: Content exceeds maximum size of {self._max_size} characters")
            return False
       
        try:
            with open(self.__filename, 'w') as file:
                file.write(text)
            self.__content = text
            print(f"File {self.__filename} written successfully")
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False
   
    def get_file_info(self):
        """Display file information"""
        return {
            "filename": self.__filename,
            "owner": self.owner,
            "created_date": self._created_date,
            "file_type": self.file_type,
            "size": len(self.__content)
        }
   
    def append_to_file(self, text):
        """Append content to the file"""
        if len(self.__content) + len(text) > self._max_size:
            print(f"Error: Appending would exceed maximum size of {self._max_size} characters")
            return False
       
        try:
            with open(self.__filename, 'a') as file:
                file.write(text)
            self.__content += text
            print(f"Content appended to {self.__filename} successfully")
            return True
        except Exception as e:
            print(f"Error appending to file: {e}")
            return False
   
    def check_file_exists(self):
        """Check if the file exists"""
        import os
        exists = os.path.isfile(self.__filename)
        if exists:
            print(f"File {self.__filename} exists")
        else:
            print(f"File {self.__filename} does not exist")
        return exists


# Usage example
if __name__ == "__main__":
    # Create a text file manager instance
    text_file = FileManager("File1.txt", "User1", "2025-04-15", "text", 1000)
   
    # Check if file exists
    text_file.check_file_exists()
   
    # Write to file
    text_file.write_file("Hello,this is a python code.\nCreated using OOP concepts.")
   
    # Read from file
    content = text_file.read_file()
    print(f"Content: {content}")
   
    # Append to file
    text_file.append_to_file("\nThis has 5 attributes.")

    # Get file information
    info = text_file.get_file_info()
    print("\nFile Information:")
    for key, value in info.items():
        print(f"{key}: {value}")
if not text_file.check_file_exists(): 
    
# Create a text file manager instance
    text_file = FileManager("Default.txt", "User1", "2025-04-15", "text", 1000)
 
    # If the file doesn't exist
    print("File not found. Creating a new file...")
    text_file.write_file("This is a newly created file.")  # Create the file with default content

    # Continue with other operations
    text_file.append_to_file("\nThis line was appended later.")
    content = text_file.read_file()
    print("\nFile Content:\n", content)
    
     # Get file information
    info = text_file.get_file_info()
    print("\nFile Information:")
    for key, value in info.items():
        print(f"{key}: {value}")
     
