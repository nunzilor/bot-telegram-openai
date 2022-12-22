import telebot
import openai

bot = telebot.TeleBot('your telegram token')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    with open('whitelist.txt', 'r') as f:
        if str(user_id) in f.read():
            bot.send_message(message.chat.id, 'Il tuo ID è in whitelist')
            bot.send_message(message.chat.id, 'Grazie, ora puoi utilizzare il bot, chiedimi qualsiasi cosa ')
             bot.send_message(message.chat.id, 'Non chiedermi cose troppo lunghe altrimenti vado in errore massimo  ')
            #Inserire qui la chiave OpenAI
            #openai = OpenAI('YOUR_OPENAI_KEY_HERE')

            openai.api_key = 'your openai api key'

            openai.Engine.list()


            #Crea una funzione per gestire le richieste
            @bot.message_handler(commands=['start', 'help'])
            def send_welcome(message):
                bot.reply_to(message, "Ricordati che le richieste si pagano e che le risposte sono di massimo 4k caratteri!")

            #Crea una funzione per gestire le richieste
            @bot.message_handler(commands=['algo'])
            def send_welcome(message):
                bot.reply_to(message, openai.Engine.list() )     
           
            #Crea una funzione per gestire le richieste
            @bot.message_handler(commands=['clear'])
            def send_welcome(message):
                bot.reply     

            #Crea una funzione per gestire le risposte
            @bot.message_handler(func=lambda message: True)
            def echo_all(message):
                response = openai.Completion.create(
                    #engine='davinci',
                    model='text-davinci-003',
                    prompt=message.text,
                    temperature=0.5,
                    max_tokens=4000
                )
                bot.reply_to(message, response['choices'][0]['text'])
        try:
            # code that might throw an InvalidRequestError
        except openai.error.InvalidRequestError as e:
            # handle the error
            print(e)
        
        else:
            bot.send_message(message.chat.id, 'Inserisci la password')
            bot.register_next_step_handler(message, get_password)

def get_password(message):
    if message.text == 'brs14ap':
        with open('whitelist.txt', 'a') as f:
            f.write(str(message.from_user.id) + '\n')
        bot.send_message(message.chat.id, 'Grazie, il tuo ID è in whitelsit')
    else:
        bot.send_message(message.chat.id, 'Password Errata!')

bot.polling()
