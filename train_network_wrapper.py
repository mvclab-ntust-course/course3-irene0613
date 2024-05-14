try:
    from train_network import setup_parser, train
    from library.train_util import read_config_from_file
    import os
    os.environ['WANDB_MODE'] = 'offline'
    import wandb
    wandb.login()
    parser = setup_parser()
    args = parser.parse_args()
    args = read_config_from_file(args, parser)
    wandb.init(
      project="mvc_hw3",
      mode= "online",
      config={
          "learning_rate": 5e-4,
          "architecture": "LoRA",
          "batch_size": 2,
          "epochs": 20
      }
    )
    train(args)
    wandb.finish()
    print("\n\033[1m✅ Done! Go download your Lora from Google Drive.\nThere will be several files, you should try the latest version (the file with the largest number next to it)")

except BaseException:
    import traceback
    import re
    from pygments import formatters, highlight, lexers
    from dracula import DraculaStyle

    tb = traceback.format_exc().split("\n")
    error_index = len(tb)
    for i, line in enumerate(tb):
      if re.match(r"^[A-Za-z-_]+Error:", line):
        error_index = i
        break
    tb_text = "\n".join(tb[:error_index])

    lexer = lexers.get_lexer_by_name("pytb", stripall=True)
    formatter = formatters.Terminal256Formatter(style=DraculaStyle)
    tb_colored = highlight(tb_text, lexer, formatter)

    print(f"\n{tb_colored}")
    if error_index < len(tb):
      tb_error = "\n".join(tb[error_index:])
      print(f"\033[0;31m\033[1m{tb_error}\n")
