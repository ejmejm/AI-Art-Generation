from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

# Source: https://stackoverflow.com/questions/1883980/find-the-nth-occurrence-of-substring-in-a-string
def find_nth(haystack, needle, n):
    parts = haystack.split(needle, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(haystack) - len(parts[-1]) - len(needle)

def clean_title(title):
    new_title = title.replace('\\', '')
    new_title = ' '.join(new_title.split())
    new_title = new_title.strip()
    return new_title

def gen_titles(n=1, genre=None):
    if not genre:
        genre = ''
    else:
        genre = genre.replace('"', '').strip() + ' '
    prompt = f'This {genre} artwork is called "'

    output = generator(
        prompt,
        max_length = 25 + len(genre.split()),
        num_return_sequences = n,
        num_beams = 10,
        temperature = 10.0,
        top_k = 100
    )

    output_texts = []
    for item in output:
        full_text = item['generated_text']
        start_idx = find_nth(full_text, '"', 0) + 1
        end_idx = find_nth(full_text, '"', 1)

        if end_idx == -1:
            target_text = full_text[start_idx:]
        else:
            target_text = full_text[start_idx:end_idx]

        cleaned_title = clean_title(target_text)
        # Replace any empty titles
        if cleaned_title == '':
            cleaned_title = gen_titles(n, genre)[0]

        output_texts.append(cleaned_title)

    return output_texts

if __name__ == '__main__':
    print(gen_titles(3))