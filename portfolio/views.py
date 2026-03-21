from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage, Project

def home(request):
    projects = Project.objects.all().prefetch_related('images')
    return render(request, 'portfolio/index.html', {'projects': projects})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            # Render-এর Free Tier এ SQLite ডেটাবেস অনেক সময় Read-Only হয়ে 500 Error দেয়।
            # তাই ডাটাবেস এরর হলে সেটা ইগনোর করে আমরা অন্তত ইমেইলটা পাঠিয়ে দেব।
            try:
                ContactMessage.objects.create(
                    name=name,
                    email=email,
                    message=message
                )
            except Exception as db_e:
                print(f"Database error (ignored): {db_e}")
                
            try:
                subject = f"New Contact Message from {name}"
                body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                return JsonResponse({'status': 'success'})
            except Exception as e:
                print(f"Server error: {e}")
                return JsonResponse({'status': 'error', 'message': f'Server Error: {str(e)}'}, status=400)
            
        return JsonResponse({'status': 'error', 'message': 'All fields are required.'}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)
