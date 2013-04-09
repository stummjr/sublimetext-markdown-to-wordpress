# markdown_to_wordpress: plugin to publish markdown to Wordpress
# Copyright (C) 2013  Valdir Stumm Junior - <stummjr@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import sublime
import xmlrpclib
import wordpresslib
import sublime_plugin
from markdown2 import markdown


class MarkdownToWordpressCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = sublime.active_window()
        window.show_input_panel("Password: ", "", self.on_done, None, None)

    def on_done(self, password):
        settings = sublime.load_settings('MarkdownToWordpress.sublime-settings')
        url = "http://%s/xmlrpc.php" % (settings.get('blog_address'))
        username = settings.get('username')
        wp = wordpresslib.WordPressClient(url, username, password)
        region = sublime.Region(0, self.view.size())
        post = wordpresslib.WordPressPost()
        markdown_text = self.view.substr(region)
        # the first line of the post is its title
        post.title = markdown_text.split('\n')[0]
        post.description = unicode(markdown_to_html(markdown_text))
        try:
            wp.newPost(post, True)
        except xmlrpclib.Fault:
            sublime.error_message("Wrong wordpress username/password.")


def markdown_to_html(markdown_text):
    markdown_html = markdown(markdown_text, extras=['toc', 'fenced-code-blocks'])
    toc_html = markdown_html.toc_html
    if toc_html:
        toc_markers = ['[toc]', '[TOC]', '<!--TOC-->']
        for marker in toc_markers:
            markdown_html = markdown_html.replace(marker, toc_html)
    return markdown_html
