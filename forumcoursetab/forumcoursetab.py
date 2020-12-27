from courseware.tabs import ExternalLinkCourseTab


class ForumCourseTab(ExternalLinkCourseTab):
    """A new course tab."""

    name = "forumcoursetab"
    title = "Fórum"
    is_hideable = True
    link_value = "https://forum.treetree2.school"
