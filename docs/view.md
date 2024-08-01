i want like the dynamic js thing for the homepage website

- make it monthly rainfall & annual rainfall data
- add the graphs done
- add the models no need
- add the data??? no need
- adding model trained 
- add javascripts smthng to make it look pretty good

- check rest of bootstrap
- one for alert msgs!

01082023 todo 
- model result
- javascript
- deployment


copypaste
### why do we add [] in the {{}} in form validation in html files


In Jinja2 templating, which is used in Flask, the {{ }} syntax is used to render variables. When you use {{ error }} inside the span tag, it will render the error message as a plain text.

The [] brackets are added around the {{ error }} to make it clear that the text is an error message, and to distinguish it from the surrounding text. This is a common convention in HTML to indicate that a piece of text is an error message or a warning.

However, in this case, the [] brackets are not strictly necessary, and you could simply use {{ error }} without them. The error message would still be rendered correctly.

But, by adding the [] brackets, you are making it explicit that the text is an error message, which can be helpful for accessibility and usability reasons. For example, screen readers may announce the text inside the [] brackets as an error message, which can be helpful for users with visual impairments.

So, while the [] brackets are not required, they are a nice touch to make the error messages more explicit and user-friendly.