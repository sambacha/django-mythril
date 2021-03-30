from rest_framework import serializers

from analysis.models import Analysis


class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ("submission_type", "bytecode", "uuid", "result")


class AnalysisStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ("result", "uuid")


class AnalysisReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ("issues", "error", "uuid")
