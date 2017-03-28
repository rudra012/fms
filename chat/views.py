from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from db import raw_query as db

from chat.models import ChatMessage
@csrf_exempt
def message_handler(request):
    if request.method == "POST":
        # add new message
        json_data = json.loads(request.body)
        message = json_data.get('message')
        if message:
            msg = ChatMessage(created_by=request.user, message=message)
            msg.save()
            return JsonResponse({'success': True, 'message': 'ok'})

    if request.method == "GET":
        # return messages of public channel limit by 100
        offset = request.GET.get('offset')
        if not offset:
            offset = 0
            raw_sql = "SELECT * FROM chat_chatmessage"
                      # "users_user au on  cm.created_by_id = au.id" \
                      # "(select last_cleared FROM chat_chatclear where cleared_by_id=" + str(
                      #       request.user.id) + ") order by " \
                      #              "created_on limit 100 offset " + str(offset) + ";"
            chat_messages = db.get_all_messages(raw_sql)
        return JsonResponse({'success': True, 'data': chat_messages})
