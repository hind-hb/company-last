from .models import Employee
from .Serializers import EmpSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import mixins


class EmpListView(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):

    serializer_class = EmpSerializer
    queryset = Employee.objects.all()
    lookup_field = 'id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)

    def post(self,request,id=None):
        return self.create(request,id)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id=None):
        return self.destroy(request,id)


@api_view(['GET'])
def EmpListapi(request):
    all_Emp = Employee.objects.all()
    data = EmpSerializer(all_Emp,many=True).data
    return Response({'data':data})



#class Emp_list(generics.ListCreateAPIView):
  #  model = Employee
  #  queryset = Employee.objects.all()
  #  serializer_class = EmpSerializer

#class Emp_list2(generics.RetrieveUpdateDestroyAPIView):

   # serializer_class = EmpSerializer
   # queryset = Employee.objects.all()
   # lookup_field = 'id'






