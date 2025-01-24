from django.shortcuts import render
from django.http import HttpResponse
from .utils import Website, summarize_text

def summarize_website(request):
    summary = None
    error = None

    if request.method == "POST":
        url = request.POST.get("url")
        try:
            # Process the website and get its content
            website = Website(url)
            summary = summarize_text(website.text)
        except Exception as e:
            error = f"Error summarizing website: {e}"

    return render(request, "summarizer/home.html", {"summary": summary, "error": error})
# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Website Summarizer!")