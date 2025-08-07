from django.http import JsonResponse
from django.shortcuts import render
from ai.supervisor import get_agents_supervisor
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.store.postgres import PostgresStore
from django.views.decorators.csrf import csrf_exempt
from accounts.models import CustomUser
from decouple import config
from django.contrib.auth.decorators import login_required


DB_URI = config('DATABASE_URL',default='')
    
@login_required    
def chatbot_temp(request):
    return render(request, 'chat.html')

with (
    PostgresStore.from_conn_string(DB_URI) as store,
    PostgresSaver.from_conn_string(DB_URI) as checkpointer,
):
    @csrf_exempt
    def chatbot(request):
        user_id = request.user.id
        user_obj = CustomUser.objects.get(pk=user_id)
        user_thread_id = user_obj.thread_id
        message = request.POST.get('message')

        config= {
            "configurable": {
                "thread_id": str(user_thread_id),
                "user_id": str(user_id),
            }
        }

        supervisor = get_agents_supervisor(
            checkpointer=checkpointer,
            store=store
        )

        response = supervisor.invoke(
            {"messages": [{"role": "user", "content": message}]},
            config
        )
        final_response = []
        for msg in response['messages']:
            final_response.append(msg.content)
        print(final_response)
        return JsonResponse({'response': final_response[1]})
