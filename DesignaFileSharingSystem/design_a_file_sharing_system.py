class FileSharingSystem:
    def __init__(self):
        self.users = set()
        self.files = {}  # file_name -> {'owner': user_id, 'content': str}
        self.access = {} # file_name -> set(user_ids_with_access)

    def _user_exists(self, user_id: str) -> bool:
        """Helper to check if a user exists."""
        return user_id in self.users

    def register_user(self, user_id: str) -> bool:
        """
        Registers a new user in the system.
        Returns True if the user was successfully registered (new user), False otherwise (user already exists).
        """
        if user_id in self.users:
            return False
        self.users.add(user_id)
        return True

    def upload(self, user_id: str, file_name: str, content: str) -> bool:
        """
        Allows a user to upload a file.
        - If the file_name already exists and the uploader is the owner, the file content is updated.
        - If the file_name already exists and the uploader is not the owner, the upload fails.
        - If the file_name is new, it's uploaded and the uploader becomes the owner with access.
        Returns True on successful upload/update, False otherwise (e.g., user does not exist,
        or attempting to overwrite another user's file).
        """
        if not self._user_exists(user_id):
            return False

        if file_name in self.files:
            if self.files[file_name]['owner'] == user_id:
                # Owner is re-uploading, update content
                self.files[file_name]['content'] = content
                return True
            else:
                # Another user trying to upload an existing file name owned by someone else
                return False
        else:
            # New file upload
            self.files[file_name] = {'owner': user_id, 'content': content}
            self.access[file_name] = {user_id}  # Owner automatically has access
            return True

    def download(self, user_id: str, file_name: str) -> str | None:
        """
        Allows a user to download a file.
        Returns the file content as a string if the user has access, None otherwise
        (e.g., user does not exist, file does not exist, or user does not have access).
        """
        if not self._user_exists(user_id):
            return None

        if file_name not in self.files:
            return None

        if user_id in self.access.get(file_name, set()):
            return self.files[file_name]['content']
        else:
            return None

    def share(self, owner_user_id: str, file_name: str, target_user_id: str) -> bool:
        """
        Allows the owner of a file to share it with another user.
        Returns True on successful sharing, False otherwise (e.g., owner_user_id is not the actual owner,
        file does not exist, or one of the users does not exist).
        """
        if not self._user_exists(owner_user_id) or not self._user_exists(target_user_id):
            return False

        if file_name not in self.files:
            return False

        if self.files[file_name]['owner'] != owner_user_id:
            return False  # Only the file owner can share it

        # Add target_user_id to the access list for this file
        self.access.setdefault(file_name, set()).add(target_user_id)
        return True

    def list_files(self, user_id: str) -> list[str]:
        """
        Lists all files accessible by a given user.
        Returns a sorted list of file names. Returns an empty list if the user does not exist
        or no files are accessible.
        """
        if not self._user_exists(user_id):
            return []

        accessible_files = []
        for file_name, users_with_access in self.access.items():
            if user_id in users_with_access:
                accessible_files.append(file_name)
        return sorted(accessible_files)