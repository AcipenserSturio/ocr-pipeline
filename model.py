import torch

if torch.cuda.is_available():
    device = torch.device('cuda')
else:
  device = torch.device('cpu')

from transformers import AutoModelForSeq2SeqLM, T5TokenizerFast
MODEL_NAME = 'UrukHan/t5-russian-spell'
MAX_INPUT = 256
tokenizer = T5TokenizerFast.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

from pathlib import Path
def pipeline(file_in: Path, file_out: Path):
  with open(file_in, 'r', encoding='UTF-8') as f:
    lines = f.read()
    lines = lines.replace('\n', ' ')
    chunks, chunk_size = len(lines), len(lines)//256
    input_sequences = [ lines[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]

  task_prefix = "Spell correct: "
  if type(input_sequences) != list: input_sequences = [input_sequences]
  encoded = tokenizer(
    [task_prefix + sequence for sequence in input_sequences],
    padding="longest",
    max_length=MAX_INPUT,
    truncation=True,
    return_tensors="pt",
  ).to(device)

  model.to(device)
  predicts = model.generate(**encoded.to(device))
  result = ' '.join(tokenizer.batch_decode(predicts, skip_special_tokens=True))

  with open(file_out, 'w', encoding='UTF-8') as res:
    res.write(result)

  del input_seqeunces
  del predicts
  del result
  del encoded

Path("./fixed/").mkdir(exist_ok=True)
for filename in Path(".").glob("*.txt"):
  pipeline(filename,
           filename.parent / "fixed" / filename.name)
# pipeline(Path('/content/neologizmy-semanticheskoy-gruppy-vneshnost-cheloveka_out.txt'),
#          Path('/content/fixed/neologizmy-semanticheskoy-gruppy-vneshnost-cheloveka_out.txt'))

