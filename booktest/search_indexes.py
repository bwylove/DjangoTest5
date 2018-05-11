# coding=utf-8
from haystack import indexes
from models import test


class testIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return test

    def index_queryset(self, using=None):
        return self.get_model().objects.all()