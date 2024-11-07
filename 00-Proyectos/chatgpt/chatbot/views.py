from django.shortcuts import render
import openai

# Create your views here.

def home(request):
  

    #PROCESAR EL FORMULARIO
    if request.method == "POST":
        vpregunta = request.POST['pregunta']

        # TRABAJO CON OPENAI
        openai.api_key = "..."

        #crear una instancia de openai
        openai.Model.list()

        #Realizar el completion - Dar respuesta mediante Openai
        response = openai.ChatCompletion.create(
             model = 'gpt-3.5-turbo',
             messages = [ # Change the prompt parameter to messages parameter
                {'role': 'user', 'content': vpregunta }],
             temperature = 0,
             max_tokens = 60,
             top_p = 1.0,
             frequency_penalty = 0.0,
             presence_penalty = 0.0
            )

        response = response.choices[0].message.content

        return render(request, 'home.html', {'dpregunta': vpregunta,'dresponse': response})

    return render(request, 'home.html',{})
