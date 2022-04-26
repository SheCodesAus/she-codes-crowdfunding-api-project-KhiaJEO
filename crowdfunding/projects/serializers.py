from rest_framework import serializers 
from .models import Project, Pledge, Category



class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    # supporter = serializers.CharField(max_length=200)
    support = serializers.ReadOnlyField(source='supporter.id')
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    summary = serializers.CharField(max_length=200)
    image = serializers.URLField()
    goal = serializers.IntegerField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.id')
    pledges = PledgeSerializer(many=True, read_only=True)
    # categories = serializers unsure if i want categories
    issue = serializers.CharField(max_length=600)
    tools = serializers.CharField(max_length=600)
    science = serializers.CharField(max_length=600)
    closing_date = serializers.DateTimeField()
    

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    category_name = serializers.CharField(max_length=200)
    slug = serializers.SlugField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
# and a link within ProjectSerializer
# category = CategorySerializer(many=False, read_only=False)
    