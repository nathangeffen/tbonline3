from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.contrib import messages

from notifications.models import CommentNotification, PostNotification, AlreadyNotifiedError


def notify(email, NotificationType, name,
           login_msg=_('You need to login to receive notifications.'),
           success_msg=_("You will receive emails alerting you to new posts. But first you must confirm your subscription via email."),
           already_msg=_("You already receive notifications for new posts"),
           *args):
    '''
    Common method for processing different types of notification view.
    '''
    if not email:
        return dict(
            success=False,
            error=True
        )

    try:
        c = NotificationType()
        c.add_user(name, email, *args)
        # messages.info(request, success_msg)
    except AlreadyNotifiedError:
        return dict(
            success=False,
            error=False
        )
    except (ValueError, KeyError):
        return dict(
            success=False,
            error=True
        )

    return dict(
        success=True,
        error=False
    )

def notify_post(request):
    '''Process notification request, typically after user submits form requesting to be
    notified of new comments on a post. 
    
    '''
    print request.POST
    try:
        name = request.POST['name']
        email = request.POST['recipient_email']
    except:
        name = 'post'

    notify_result = notify(email, PostNotification, name)

    return render(
        request,
        template_name='notification_confirmation.html',
        dictionary=notify_result
    )


def notify_comment(request):
    '''Process notification request, typically after user submits form requesting to be
    notified of new comments on a post. 
    
    '''
    try:
        name = request.POST['name']
    except:
        name = 'post'

    return notify(request, CommentNotification, name,
                  None,
                  _("You will receive emails notifying you of new comments on this post."),
                  _("You already receive emails notifying you of new comments on this post."), 
                  request.POST['app_label'], 
                  request.POST['model'], int(request.POST['pk']))   
    

def remove_notification(request, NotificationType, name, 
                        login_msg=_('You need to login to stop notifications.'),
                        success_msg=_('You will no longer receive emails notifying you of new posts.'), 
                        already_msg=_('You do not get emailed notifications of new posts.'), 
                        *args):

    # if not request.user.is_authenticated:
    #     messages.warning(request, login_msg)
    # else:
    try:
        try:
            notification = NotificationType.objects.get(name=name)
        except:
            notification = NotificationType()

        notification.remove_user(request.user, *args)
        # messages.info(request, success_msg)
    except:
        pass
        # messages.info(request, already_msg)

    try:     
        return HttpResponseRedirect(request.GET['next'])
    except:
        raise Http404    


def remove_post_notification(request):
    try:
        name = request.POST['name']
    except:
        name = 'post'
        
    return remove_notification(request, PostNotification, name)


def remove_comment_notification(request):
    try:
        name = request.POST['name']
    except:
        name = 'comment'
    
    return remove_notification(request, CommentNotification, name,
                                    None,
                                    _('You will no longer receive emails notifying you of new comments on this post.'),
                                    _('You do not receive emails notifying you of new comments on this post.'), 
                                    request.POST['app_label'],
                                    request.POST['model'],
                                    int(request.POST['pk']))
