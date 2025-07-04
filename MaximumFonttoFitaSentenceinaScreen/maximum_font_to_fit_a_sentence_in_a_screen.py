def _can_fit_sentence(font_properties, text, screen_width, screen_height):
    """
    Helper function to determine if a given text can fit within the screen
    dimensions using a specific font.

    Args:
        font_properties (tuple): A tuple (font_size, char_width, font_height_val)
                                 representing the characteristics of the font.
        text (str): The sentence to fit.
        screen_width (int): The maximum width of the screen.
        screen_height (int): The maximum height of the screen.

    Returns:
        bool: True if the text can fit, False otherwise.
    """
    font_size, char_width, font_height_val = font_properties

    # An empty string always fits, regardless of screen or font dimensions.
    if not text:
        return True

    # If the screen has no width and characters have a positive width,
    # the text cannot fit horizontally.
    if screen_width <= 0 and char_width > 0:
        return False
    
    # If the screen has no height and the font has a positive height,
    # the text cannot fit vertically.
    if screen_height <= 0 and font_height_val > 0:
        return False

    lines_needed = 0
    if char_width == 0:
        # If character width is zero, all characters effectively take no horizontal space.
        # However, for non-empty text, it still occupies at least one line vertically.
        lines_needed = 1
    else:
        # Calculate the total width the text would occupy if laid out on a single line.
        total_text_width = len(text) * char_width
        
        # Calculate the number of lines required using ceiling division.
        # (A + B - 1) // B is a common integer division trick for ceil(A/B).
        lines_needed = (total_text_width + screen_width - 1) // screen_width

    # Calculate the total height required by the text.
    total_height_needed = lines_needed * font_height_val

    # Check if the total height needed fits within the screen height.
    return total_height_needed <= screen_height


def maximumFont(text, width, height, fonts):
    """
    Finds the maximum font size from a given list of fonts that allows a
    sentence to fit within specified screen dimensions.

    Args:
        text (str): The sentence to fit.
        width (int): The maximum width of the screen.
        height (int): The maximum height of the screen.
        fonts (list of tuple): A list of font properties, where each tuple is
                               (font_size, font_width_per_char, font_height).

    Returns:
        int: The maximum font_size that fits, or -1 if no font fits.
    """
    # Sort the fonts list by font_size in ascending order.
    # This is essential for the binary search algorithm to work correctly,
    # as we rely on the property that if a font fits, all smaller fonts also fit.
    fonts.sort(key=lambda x: x[0])

    ans_font_size = -1  # Initialize the answer with -1 (no font fits)

    # Perform binary search on the indices of the sorted fonts list.
    low = 0
    high = len(fonts) - 1

    while low <= high:
        mid = (low + high) // 2
        current_font_properties = fonts[mid]

        # Check if the text can fit using the current font.
        if _can_fit_sentence(current_font_properties, text, width, height):
            # If it fits, this font size is a potential candidate for the maximum.
            # We store its font_size and try to find an even larger font that also fits
            # by searching in the upper half.
            ans_font_size = current_font_properties[0]
            low = mid + 1
        else:
            # If it does not fit, this font size is too large.
            # We need to try a smaller font size by searching in the lower half.
            high = mid - 1
            
    return ans_font_size