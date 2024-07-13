import os

def get_outer_folder_names(root_dir):
  """Gets a list of immediate subdirectory names within a given root directory.

  Args:
    root_dir: The root directory to search in.

  Returns:
    A list of immediate subdirectory names.
  """

  return [name for name in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, name))]


# Example usage:
root_directory = "/Users/akshay.khanna/projects/EbookGeneratorAI/output/books/"
all_folders = get_outer_folder_names(root_directory)
print(all_folders)