import telebot, wikipedia

bot = telebot.TeleBot("")
wikipedia.set_lang("ru")

if __name__ == "__main__":
    def getwiki(s):
        try:
            ny = wikipedia.page(s)
            wikitext = ny.content[:1000]
            wikimas = wikitext.split(".")
            wikimas = wikimas[:-1]
            wikitext2 = ""
            for x in wikimas:
                if not ("==" in x):
                    if (len((x.strip())) > 3):
                        wikitext2 = wikitext2 + x + "."
                else:
                    break
            return wikitext2
        except Exception as e:
            return "В энциклопедии нет информации об этом"


    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        bot.send_message(m.chat.id, "Отправьте мне любое слово, и я найду его значение на Wikipedia")


    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        bot.send_message(message.chat.id, getwiki(message.text))


    bot.polling(none_stop=True, interval=0)
