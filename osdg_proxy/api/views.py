import requests
from django.http import JsonResponse, HttpResponseNotFound

from rest_framework import viewsets

from osdg_proxy import settings


def get_osdg_results(task_id):
    return requests.post(settings.OSDG_BASE_URL + "retrieve-results",
                          data={
                              "token": settings.OSDG_TOKEN,
                              "task_id": task_id,
                          }
                          ).json()


class TaskViewSet(viewsets.ViewSet):
    def create(self, request):
        reply = requests.post(settings.OSDG_BASE_URL + "text-upload",
                      data={"token": settings.OSDG_TOKEN,
                            "text": request.data["text"]
                            }
                      )
        task_id = reply.json()
        return JsonResponse({"task_id": task_id})

    def retrieve(self, request, pk=None):
        results = get_osdg_results(pk)
        if results["status"] == "ERROR - Unrecognised 'task_id' key":
            return HttpResponseNotFound()
        results["task_id"] = pk
        return JsonResponse(results)
