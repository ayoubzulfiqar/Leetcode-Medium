import time

class TimeLimitedCache:
    def __init__(self):
        # self.cache stores key-value pairs along with their expiration timestamps.
        # Format: {key: (value, expiration_timestamp_in_seconds)}
        # The expiration_timestamp_in_seconds is calculated using time.monotonic()
        # which provides a monotonic clock that is not affected by system clock changes.
        self.cache = {}

    def set(self, key: int, value: int, duration: int) -> bool:
        # Get the current time using the monotonic clock.
        current_time_seconds = time.monotonic()
        
        # Check if the key already exists in the cache and if its current entry is still un-expired.
        # The problem requires returning true if the same un-expired key already exists.
        key_was_unexpired = False
        if key in self.cache:
            _old_value, old_expiration_time_seconds = self.cache[key]
            # If the current time is less than the old expiration time, the key was un-expired.
            if current_time_seconds < old_expiration_time_seconds:
                key_was_unexpired = True
        
        # Calculate the new expiration timestamp.
        # 'duration' is in milliseconds, so convert it to seconds by dividing by 1000.0.
        new_expiration_time_seconds = current_time_seconds + (duration / 1000.0)
        
        # Store or update the key-value pair with its new value and new expiration timestamp.
        # This overwrites any existing entry for the key, regardless of its expiration status.
        self.cache[key] = (value, new_expiration_time_seconds)
        
        # Return whether the key was found and un-expired before this set operation.
        return key_was_unexpired

    def get(self, key: int) -> int:
        # Get the current time using the monotonic clock.
        current_time_seconds = time.monotonic()
        
        # Check if the key exists in the cache.
        if key in self.cache:
            value, expiration_time_seconds = self.cache[key]
            
            # Check if the key's entry is still un-expired.
            if current_time_seconds < expiration_time_seconds:
                # If un-expired, return the associated value.
                return value
            else:
                # If the key exists but is expired, remove it from the cache.
                # This helps keep the cache clean and efficient for future operations like count().
                del self.cache[key]
        
        # If the key does not exist or was found to be expired, return -1.
        return -1

    def count(self) -> int:
        # Get the current time using the monotonic clock.
        current_time_seconds = time.monotonic()
        
        unexpired_count = 0
        # Create a list to store keys that need to be deleted after iteration.
        # This prevents RuntimeError: dictionary changed size during iteration.
        keys_to_delete = [] 
        
        # Iterate through all items in the cache.
        for key, (value, expiration_time_seconds) in self.cache.items():
            # Check if the current entry for the key is un-expired.
            if current_time_seconds < expiration_time_seconds:
                unexpired_count += 1
            else:
                # If the key is expired, mark it for deletion.
                keys_to_delete.append(key)
        
        # Remove all marked expired keys from the cache.
        for key in keys_to_delete:
            del self.cache[key]
            
        # Return the total count of un-expired keys.
        return unexpired_count