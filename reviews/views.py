from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Review
# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['message'] = "this works"
        return context
    
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name= "reviews"
    

    
class ReviewDetailsView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    context_object_name = "review"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loded_review.id)
        return context

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect('/reviews/' + review_id)