from telegram import Bot, Update
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater

def start(text, mode):
    def _start(update: Update, context: CallbackContext):
        # In the future the text to reply would be take from DB for convenience
        update.message.reply_text(text + mode(update))
        return _start

class Server():
    def __init__(self, t_token) -> None:
        self.TOKEN = t_token
        self.updater = Updater(self.TOKEN, use_context=True)
        self.DB = None
        # mode - functional object, which return scecial property of update
        self.mode = []

    def assembly(self):
        # assembly updater
        self.updater.dispatcher.add_handler(CommandHandler('start'), start("Hello", self.mode[0]))
        
    def run(self):
        self.updater.start_polling()