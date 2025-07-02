class Solution:
    def is_valid_utf8(self, data: list[int]) -> bool:
        num_bytes_to_follow = 0

        # Masks and patterns for UTF-8 byte types
        # 1-byte character: 0xxxxxxx
        MASK_1_BYTE_START = 0b10000000
        PATTERN_1_BYTE_START = 0b00000000

        # 2-bytes character: 110xxxxx
        MASK_2_BYTE_START = 0b11100000
        PATTERN_2_BYTE_START = 0b11000000

        # 3-bytes character: 1110xxxx
        MASK_3_BYTE_START = 0b11110000
        PATTERN_3_BYTE_START = 0b11100000

        # 4-bytes character: 11110xxx
        MASK_4_BYTE_START = 0b11111000
        PATTERN_4_BYTE_START = 0b11110000

        # Continuation byte: 10xxxxxx
        MASK_CONTINUATION = 0b11000000
        PATTERN_CONTINUATION = 0b10000000

        for byte in data:
            if num_bytes_to_follow == 0:
                # This byte is expected to be the start of a new UTF-8 character
                if (byte & MASK_1_BYTE_START) == PATTERN_1_BYTE_START:
                    # It's a 1-byte character (0xxxxxxx)
                    num_bytes_to_follow = 0  # No continuation bytes expected
                elif (byte & MASK_2_BYTE_START) == PATTERN_2_BYTE_START:
                    # It's a 2-bytes character (110xxxxx)
                    num_bytes_to_follow = 1  # Expect 1 continuation byte
                elif (byte & MASK_3_BYTE_START) == PATTERN_3_BYTE_START:
                    # It's a 3-bytes character (1110xxxx)
                    num_bytes_to_follow = 2  # Expect 2 continuation bytes
                elif (byte & MASK_4_BYTE_START) == PATTERN_4_BYTE_START:
                    # It's a 4-bytes character (11110xxx)
                    num_bytes_to_follow = 3  # Expect 3 continuation bytes
                else:
                    # Invalid start byte pattern (e.g., 10xxxxxx, 11111xxx, etc.)
                    return False
            else:
                # This byte is expected to be a continuation byte
                if (byte & MASK_CONTINUATION) == PATTERN_CONTINUATION:
                    # It's a valid continuation byte (10xxxxxx)
                    num_bytes_to_follow -= 1
                else:
                    # It's not a valid continuation byte
                    return False
        
        # After iterating through all bytes, if num_bytes_to_follow is 0,
        # it means all multi-byte characters were complete and valid.
        return num_bytes_to_follow == 0

```