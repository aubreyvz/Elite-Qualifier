import time
import difflib

# load dictionary words from file
def load_words():
  da_words = []
  start_time = time.time()
  
  with open('da words.txt', 'r') as f:
    for line in f:
      da_words.append(line.rstrip())
  end_time = time.time()

  elapsed_time = end_time - start_time
  # log words loaded and elapsed time
  print('Loaded ' + str(len(da_words)) + ' words in ' + f'{elapsed_time:.2f}' + ' seconds.')

  return da_words

#autocorrect function

def autocorrect(text, da_words):
  for w in text.casefold().split():
    if w not in da_words:
      suggestion = difflib.get_close_matches(w, da_words)
      print(f'Did you mean {" , ".join(str(x) for x in suggestion)} instead of {w}?')
      
    elif w in da_words:
        print('Looks good!')

    
  return text

def main():
    da_words = load_words()
    print('Type a word or sentence or type \"quit\" to stop')
    while True:
        text = input(':> ')
        if ('quit' == text):
          break
        autocorrect(text, da_words)

if __name__ == "__main__":
    main()
    autocorrect(text, da_words)