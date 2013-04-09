MarkdownToWordpress
===================

This ST2 plugin takes Markdown contents as its input, converts it to HTML and publish the HTML into a user-defined Wordpress weblog.


# How to configure
After installation, you should add your wordpress credentials and weblog address into the file `MarkdownToWordpress.sublime-settings`, located at the plugin folder. If your weblog address is `myblog.mydomain.com`, and your credentials are `johndoe` for username and `anypasssword` for password, your configuration file should looks like:

    {
        "username": "johndoe",
        "blog_address": "myblog.mydomain.com" // no http prefix here!
    }

Now, make sure your wordpress blog has the XML-RPC module enabled (`.wordpress.com` blogs have it enabled by default).


# Security concerns
I am aware that typing our password in a text input field is not the best approach to provide the password. So, I'm looking for another approach to authenticate users to remove this shortcoming. And remember, I am not responsible for your password. :)
