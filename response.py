import unicodedata
from storage import save_counts


def get_response(user_input: str, author, swear_count, count_dictionary) -> str:

    p_message = unicodedata.normalize("NFKD", user_input).casefold()
    swear_words = ["insert", "swear words", "here"]

    for i in swear_words:
        swear_word_normalized = unicodedata.normalize("NFKD", i).casefold()
        if swear_word_normalized in p_message:
            swear_count[author.id] = swear_count.get(author.id, 0) + 1
            count_dictionary[i] = count_dictionary.get(i, 0) + 1
            save_counts(swear_count)
            response = (f'{author.mention} said {i}!'
                        f'\nThey have said "{i}" {count_dictionary.get(i, 0)} times '
                        f'and have now sworn a total of {swear_count.get(author.id, 0)} times!')
            return response

    if "!swearcount" in p_message:
        return f"{author.mention} has sworn a total of {swear_count.get(author.id, 0)} times."
