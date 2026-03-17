from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

def home(request):
    return render(request, 'portfolio/index.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            # Save to database
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
            
            # Send Email
            try:
                subject = f"New Contact Message from {name}"
                body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL], # Send to yourself
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email error: {e}")
                # We still return success because it's saved in DB
            
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'message': 'All fields are required.'}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)
