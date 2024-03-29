from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from user.models import Profile, Following
from blog.models import Post


class ProfilePostView(ListView):
    template_name = 'profile.html'      # <app>/<model>_<viewtype>.html

    def get_queryset(self):
        self.user_profile = get_object_or_404(Profile, handle = self.kwargs['handle'])    # from the url
        return Post.objects.filter(id = self.user_profile.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.user_profile
        context['posts'] = Post.objects.filter(author = self.user_profile.id).order_by('-created_at')
        return context


class ProfileRepliesView(ProfilePostView):
    template_name = 'profile_withReplies.html'


class ProfileMediaView(ProfilePostView):
    template_name = 'profile_media.html'


class ProfileLikesView(ProfilePostView):
    template_name = 'profile_likes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.user_profile.liked_posts.order_by('-created_at')
        return context


class ProfileFollowersView(ProfilePostView):
    template_name = 'profile_followers.html'


class ProfileFollowingView(ProfilePostView):
    template_name = 'profile_following.html'


class ProfileFollowersYouKnowView(ProfilePostView):
    template_name = 'profile_followersYouKnow.html'


class ProfileSuggestedView(ProfilePostView):
    template_name = 'profile_suggested.html'


class ProfileListsView(ProfilePostView):
    template_name = 'profile_lists.html'


class ProfileTopicsView(ProfilePostView):
    template_name = 'profile_topics.html'


class ProfileMomentsView(ProfilePostView):
    template_name = 'profile_moments.html'



@login_required
@require_POST
def follow(request, handle):
    counterpart = Profile.objects.get(handle = handle)
    currentuser = Profile.objects.get(handle = request.user.profile.handle)
    if counterpart not in currentuser.following.all():
        currentuser.following.add(counterpart)
        return redirect(request.META['HTTP_REFERER'])


@login_required
@require_POST
def unfollow(request, handle):
    counterpart = Profile.objects.get(handle = handle)
    currentuser = Profile.objects.get(handle = request.user.profile.handle)
    if counterpart in currentuser.following.all():
        currentuser.following.remove(counterpart)
        return redirect(request.META['HTTP_REFERER'])