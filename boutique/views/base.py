

class BaseViewSet:
	create_serializer_class = None
	list_serializer_class = None
	detail_serializer_class = None
	update_serializer_class = None
	permission_classes = None

	def get_serializer_class(self):
		SERIALIZER_CLASSES = {
			"create": self.create_serializer_class,
			"list": self.list_serializer_class,
			"retrieve": self.detail_serializer_class,
			"update": self.update_serializer_class,
			"partial_update": self.update_serializer_class,
		}

		ser_class = SERIALIZER_CLASSES.get(self.action)
		
		if ser_class is not None:
			return ser_class

		return super().get_serializer_class()