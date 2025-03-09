import emoji

def emoji_to_text(text):
  """Converts emojis in a string to their text descriptions.

  Args:
    text: The input string containing emojis.

  Returns:
    The string with emojis replaced by their text descriptions.
  """
  return emoji.demojize(text)

# Example usage:
text_with_emojis = "Hello, world! 😊🌍🎉"
text_without_emojis = emoji_to_text(text_with_emojis)
print(text_without_emojis)  # Output: Hello, world! :smiling_face_with_smiling_eyes::globe_with_meridians::party_popper:

text2 = "I love 🍕 and 🐶"
print(emoji_to_text(text2)) # Output: I love :pizza: and :dog_face:

text3 = "This is a test with multiple emojis 😃👍❤️"
print(emoji_to_text(text3)) # Output: This is a test with multiple emojis :grinning_face_with_big_eyes::thumbs_up::red_heart:

def text_to_emoji(text):
    """Converts emoji text descriptions back to emojis.

    Args:
        text: The input string containing emoji text descriptions.

    Returns:
        The string with emoji text descriptions replaced by emojis.
    """
    return emoji.emojize(text)

text_with_description = "Hello, world! :smiling_face_with_smiling_eyes::globe_with_meridians::party_popper:"
text_with_emojis_again = text_to_emoji(text_with_description)
print(text_with_emojis_again) #Output: Hello, world! 😊🌍🎉

text4 = "I love :pizza: and :dog_face:"
print(text_to_emoji(text4)) #Output: I love 🍕 and 🐶