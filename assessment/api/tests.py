from django.test import TestCase

# Create your tests here.
# loan request 
# class LoanRequest(APIView):
#     def post(self, request):
#         my_token = uc.userkey(request.META['HTTP_AUTHORIZATION'][7:])
#         if my_token:
#             check_status = Account.objects.filter(uid=my_token['id']).first()
#             if check_status.blocked == False:
#                 serializer = LoanSerializer(data=request.data)
#                 if serializer.is_valid():
#                     amount = serializer.validated_data['amount']
                    
#                     if amount % 500 != 0:
#                         return Response({"status": False, "message": "Loan amount must be a multiple of 500."})

#                     # Get the start and end of the current day
#                     today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
#                     next_day = today + timedelta(days=1)

#                     # Check if the user has already created a loan request today
#                     existing_loan = loan.objects.filter(userdetails=check_status, date_gte=today, date_lt=next_day).first()
#                     if existing_loan:
#                         return Response({"status": False, "message": "You have already created a loan request today."})

#                     data = serializer.save(amount=amount, date=datetime.now(), userdetails=check_status)
#                     return Response({"status": True, "message": "Loan request successfully sent."})
#                 else:
#                     return Response(serializer.errors, status=400)
#             else:
#                 return Response({"status": False, "message": "You cannot request a loan."})
#         else:
#             return Response({"status": False, "message": "Unauthorized."})