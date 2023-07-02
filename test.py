import g4f


print(g4f.Provider.Ails.params) # supported args

# Automatic selection of provider



# streamed completion
messageComplete = ''
response = g4f.ChatCompletion.create(model=g4f.Model.gpt_4, provider=g4f.Provider.Bing, messages=[
                                     {"role": "user", "content": "Me forneça em topicos 5 ultimas noticias importante sobre o mercado de cripto, responda em portugues"}], stream=True)

for message in response:
    messageComplete +=message
    print(message)

print('Mensagem completa ==>',messageComplete )
# # normal response
# response = g4f.ChatCompletion.create(model=g4f.Model.gpt_4, messages=[
#                                      {"role": "user", "content": "Qual foi o ultimo jogo do Gremio do Brasil?"}]) # alterative model setting

# print(response)


# # Set with provider
# response = g4f.ChatCompletion.create(model='gpt-3.5-turbo', provider=g4f.Provider.ChatgptLogin, messages=[
#                                      {"role": "user", "content": "Hello world"}], stream=True)

# for message in response:
#     print(message)


#Bing,GetGpt,DeepAi