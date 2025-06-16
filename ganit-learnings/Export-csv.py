import csv
import traceback
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from projects.managers.AllocationManager import CommonFilters
from users.models import Employee
from django.db.models import Q
from rest_framework.response import Response
from django.http import HttpResponse, StreamingHttpResponse

from utility.datetime_utility import get_formatted_datetime

class Echo:
    def write(self, value):
        return value
    
class ExportCSV(APIView):

    def get_queryset(self):

        queryset = get_user_model().objects.all()

        filters = CommonFilters(filters=self.request.data, queryset=queryset)  
        _status,queryset = filters.filters_for_allocations()
        return queryset
    
    def get_project_manager(self,project_object):
        project_manager :str = "NA"
        if project_object.project_managers_list:
            project_manager = ", ".join(
        map(
            lambda emp_code: f'{Employee.objects.filter(employee_code=emp_code).first().display_name}',
            project_object.project_managers_list,
        )
    )
        return project_manager

    def get_allocation_type(self,allocation_type):
        if allocation_type:
            if allocation_type == "1":
                return "Soft"
            return "Hard"
        return "NA"
    def generate_csv(self,data,headers):
        # Query all employees and their allocations
        try:
            employees = data.prefetch_related('employees_allocated')
            
            # Create streaming response
            def csv_generation_stream():
                try:
                    pseudo_buffer = Echo()
                    writer = csv.writer(pseudo_buffer)
                
                    # Write header row
                    yield writer.writerow(headers)

                    index = 1 # Start index at 1
                    for employee in employees:
                        allocations = employee.employees_allocated.all()
                        num_allocations = allocations.count()
                        row:dict = {
                                    "Index" : index,
                                    "Employee Code" : employee.employee_code if employee.employee_code else "NA",
                                    "Employee Name" : employee.display_name if employee.display_name else "NA",
                                    "Email" : employee.email if employee.email else "NA",
                                    "Job Title" : employee.job_title if employee.job_title else "NA" ,
                                    "Department" : employee.department.department_name if employee.department else "NA",
                                    "Sub Department": employee.sub_department.sub_department_name if employee.sub_department else "NA",
                                    "Manager":  employee.manager.display_name if employee.manager else "NA",
                                    "Dotted Line Manager": employee.dotted_line_manager.display_name if employee.dotted_line_manager else "NA",
                                    "Project Name": "NA",
                                    "Project Manager":"NA",
                                    "Client Name":"NA",
                                    "Client Code":"NA",
                                    "Engagement Manager Name":"NA",
                                    "Allocation Start Date":"NA",
                                    "Allocation End Date" : "NA",
                                    "Allocation Percentage":"NA",                        
                                    "Status" :"NA",
                                    "Allocation Type" :"NA"
                                    }
                        if num_allocations > 0:
                            for allocation in allocations:
                                index=index+1
                                row["Project Name"]= allocation.project_object.project_name if allocation.project_object else "NA" 
                                row["Project Manager"]=  self.get_project_manager(project_object=allocation.project_object) if allocation.project_object else "NA"
                                row["Client Name"]= allocation.project_object.client.client_name if allocation.project_object and allocation.project_object.client else "NA"
                                row["Client Code"]= allocation.project_object.client.client_acronym if allocation.project_object and allocation.project_object.client else "NA"
                                row["Engagement Manager Name"]= allocation.project_object.client.engagement_manager if allocation.project_object and allocation.project_object.client else "NA"
                                row["Allocation Start Date"]= get_formatted_datetime(allocation.allocation_start_date)
                                row["Allocation End Date"]= get_formatted_datetime(allocation.allocation_end_date)
                                row["Allocation Percentage"]= allocation.allocation_percentage if allocation.allocation_percentage else "NA"
                                row["Status"] = "Allocated"
                                row["Allocation Type"] = self.get_allocation_type(allocation.allocation_type) 
                                
                                yield writer.writerow(list(row.values()))
                        else:
                            yield writer.writerow(list(row.values()))
                        index = index+1
                except Exception as e:
                    traceback.print_exc()
                    raise e
            # Return response with CSV data streamed directly to the client
            response = StreamingHttpResponse(csv_generation_stream(), content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename="employee_allocations.csv"'
            return response, True        

        except Exception as e:
            traceback.print_exc()
            return str(e),False
    def post(self, request):
        
        try:
           
            queryset = self.get_queryset()
            user:Employee = request.user
            queryset1,queryset2 = [None]*2
            if user:
                admin_group = user.groups.filter(name = "AdminGroup")
                resource_manager_group = user.groups.filter(name = "ResourceManagerGroup").first()
                if not admin_group.exists():
                    employee = get_user_model().objects.filter(id = user.pk).first()
                    queryset1 = queryset.filter(employees_allocated__isnull = False, employees_allocated__allocation_approved = True,employees_allocated__allocation_denied = False).filter(
                                                Q(employees_allocated__project_object__project_managers_list__contains = [employee.employee_code]) | 
                                                Q(employees_allocated__project_object__engagement_manager = employee)|
                                                Q(employees_allocated__project_object__client__engagement_manager = employee)
                                               )
                if resource_manager_group:
                    queryset2 = queryset.filter(Q(requests__sub_departments__contains = [employee.sub_department.sub_department_name]))
                if queryset1 is not None and queryset2 is not None:
                    queryset = (queryset1 | queryset2).distinct()
                elif queryset1 is not None:
                    queryset = queryset1
                elif queryset2 is not None:
                    queryset = queryset2
            
            
            headers:list = [
                "Index",
                "Employee Code",
                "Employee Name",
                "Email",
                "Job Title",
                "Department",
                "Sub Department",
                "Manager",
                "Dotted Line Manager",
                "Project Name",
                "Project Manager",
                "Client Name",
                "Client Code",
                "Engagement Manager Name",
                "Allocation Start Date",
                "Allocation End Date",
                "Allocation Percentage",
                "Status",
                "Allocation Type"
            ]
            

            if not len(queryset):
                return Response({"data": None, "message":"No data available!", "errors": []}, status=200)
            print("headers")

            response, csv_status = self.generate_csv(data=queryset, headers=headers)
            
            if not csv_status:
                return Response(
                    data={
                        "data": None, 
                        "message": "Something went wrong while exporting CSV", 
                        "errors": [response]
                    }, 
                    status=500
                )
            
           
            return response
        
        
        except Exception as e:
            traceback.print_exc()
            print("Something went wrong while trying to export to CSV!", e)
            return Response(data={
                "data": None, 
                "message": "Something went wrong while trying to export to CSV!", 
                "errors": [str(e)]
            }, status=500)


