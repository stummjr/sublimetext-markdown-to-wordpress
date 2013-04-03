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
import wordpresslib
import sublime_plugin
from markdown2 import markdown


class MarkdownToWordpressCommand(sublime_plugin.TextCommand):

    url = "http:// .wordpress.com/xmlrpc.php"
    user = ''
    passwd = ''

    def run(self, edit):
        wp = wordpresslib.WordPressClient(self.url, self.user, self.passwd)
        region = sublime.Region(0, self.view.size())
        post = wordpresslib.WordPressPost()
        post.title = self.get_title(self.view.substr(region))
        post.description = unicode(self.markdown_to_html(self.view.substr(region)))
        wp.newPost(post, True)

    def markdown_to_html(self, markdown_text):
        markdown_html = markdown(markdown_text, extras=['toc', 'fenced-code-blocks'])
        toc_html = markdown_html.toc_html
        if toc_html:
            toc_markers = ['[toc]', '[TOC]', '<!--TOC-->']
            for marker in toc_markers:
                markdown_html = markdown_html.replace(marker, toc_html)
        return markdown_html

    def get_title(self, markdown_text):
        """ The first line of the post is its title.
        """
        return markdown_text.split('\n')[0]
