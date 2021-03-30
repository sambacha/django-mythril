import uuid as uu

import celery.states
import rest_framework.status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from analysis.models import Analysis
from analysis.serializers import *
from analysis.tasks import myth_task


@api_view(["GET", "POST"])
def bytecode_submission(request):
    """
        Submits a new analysis with a smart contract bytecode
        """
    if request.method == "GET":
        all_analysis = Analysis.objects.all()
        serializer = AnalysisSerializer(all_analysis, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = AnalysisSerializer(data=request.data)
        if serializer.is_valid():
            submission = serializer.save()
            t = myth_task.apply_async(
                [submission.bytecode], task_id=str(submission.uuid)
            )
            return Response(
                serializer.data, status=rest_framework.status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=rest_framework.status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def status(request, uuid):
    """
        Returns the status of an analysis for a given UUID.
        """
    try:
        analysis = Analysis.objects.filter(uuid=uuid).first()
        if analysis:
            task_async = myth_task.AsyncResult(str(analysis.uuid))
            # analysis.error = task_async.result['stderr']
            # analysis.issues = task_async.result['stdout']
            analysis.result = task_async.status
            analysis.save()
            serializer = AnalysisStatusSerializer(analysis)
            return Response(serializer.data, status=rest_framework.status.HTTP_200_OK)
        else:
            return Response(status=rest_framework.status.HTTP_204_NO_CONTENT)
    except BaseException:
        return Response(status=rest_framework.status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def report(request, uuid):
    """
        Returns the report of the issues found in an analysis for a given UUID.
        """
    try:
        analysis = Analysis.objects.filter(uuid=uuid).first()
        if analysis:
            task_async = myth_task.AsyncResult(str(analysis.uuid))
            if task_async.status == celery.states.SUCCESS:
                analysis.error = task_async.result["stderr"]
                analysis.issues = task_async.result["stdout"]
                analysis.save()
                serializer = AnalysisReportSerializer(analysis)
                return Response(
                    serializer.data, status=rest_framework.status.HTTP_200_OK
                )
        return Response(status=rest_framework.status.HTTP_204_NO_CONTENT)
    except BaseException:
        return Response(status=rest_framework.status.HTTP_400_BAD_REQUEST)
