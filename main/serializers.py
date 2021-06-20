from rest_framework import serializers

from .models import Product, Category, Tag, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'image')

    def validate_title(self, title):
        if self.Meta.model.objects.filter(title=title).exists():
            raise serializers.ValidationError('Заголовок не может повторяться')
        return title


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title', )

    def validate_title(self, title):
        if self.Meta.model.objects.filter(title=title).exists():
            raise serializers.ValidationError('Заголовок не может повторяться')
        return title


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('text', 'product', 'rating', "user")

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError('Укажите рейтинг от 1 до 5')
        return rating

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = Comment.objects.create(user=user, **validated_data)
        return comment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'category', 'tags')

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        product = Product.objects.create(**validated_data)
        product.tags.add(*tags)
        return product

    def _get_image_url(self, obj):
        request = self.context.get('request')
        image_obj = obj.images.first()
        if image_obj is not None and image_obj.image:
            url = image_obj.image.url
            if request is not None:
                url = request.build_absolute_uri(url)
            return url
        return ''

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        representation['categories'] = CategorySerializer(instance.category, context=self.context).data
        representation['tags'] = TagSerializer(instance.tags.all(), many=True, context=self.context).data
        representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        representation['likes_count'] = instance.likes.count()
        return representation


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def _get_image_url(self, obj):
        request = self.context.get('request')
        image_obj = obj.images.first()
        if image_obj is not None and image_obj.image:
            url = image_obj.image.url
            if request is not None:
                url = request.build_absolute_uri(url)
            return url
        return ''

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        representation['categories'] = CategorySerializer(instance.categories.all(), many=True).data
        representation['tags'] = TagSerializer(instance.tags.all(), many=True, context=self.context).data
        representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        representation['likes_count'] = instance.likes.count()
        return representation
