import json

from django import template
from django.urls import reverse
from django.utils.html import format_html

from adhocracy4.rules.discovery import NormalUser

register = template.Library()


@register.simple_tag(takes_context=True)
def react_questions(context, obj):
    request = context['request']

    user = request.user
    is_moderator = user.has_perm('a4_candy_questions.moderate_questions', obj)
    categories = [category.name for category in obj.category_set.all()]
    questions_api_url = reverse('questions-list', kwargs={'module_pk': obj.pk})

    like_permission = 'a4_candy_likes.add_like_model'
    has_liking_permission = user.has_perm(
        like_permission, obj)
    would_have_liking_permission = NormalUser().would_have_perm(
        like_permission, obj
    )

    ask_permissions = 'a4_candy_questions.propose_question'
    has_ask_questions_permissions = user.has_perm(ask_permissions, obj)
    would_have_ask_questions_permission = NormalUser().would_have_perm(
        ask_permissions, obj)

    attributes = {
        'information': obj.description,
        'questions_api_url': questions_api_url,
        'isModerator': is_moderator,
        'categories': categories,
        'hasLikingPermission': (has_liking_permission
                                or would_have_liking_permission),
        'hasAskQuestionsPermission': (has_ask_questions_permissions
                                      or would_have_ask_questions_permission),
        'askQuestionUrl': reverse('question-create', kwargs={'slug': obj.slug})
    }

    return format_html(
        '<div data-speakup-widget="questions" '
        'data-attributes="{attributes}"></div>',
        attributes=json.dumps(attributes)
    )


@register.simple_tag(takes_context=True)
def react_questions_present(context, obj):

    categories = [category.name for category in obj.category_set.all()]
    questions_api_url = reverse('questions-list', kwargs={'module_pk': obj.pk})
    request = context['request']
    url = obj.project.get_absolute_url()
    full_url = request.build_absolute_uri(url)

    attributes = {
        'questions_api_url': questions_api_url,
        'categories': categories,
        'url': full_url,
        'title': obj.project.name
    }

    return format_html(
        '<div data-speakup-widget="present" '
        'data-attributes="{attributes}"></div>',
        attributes=json.dumps(attributes)
    )
