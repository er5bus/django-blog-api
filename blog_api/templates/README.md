Templates
=========

We recommend keeping all your templates in this directory unless you plan on including your application in multiple projects (or developing it as a open source “reusable” application).

Please note, that these templates may be taken before any templates in application folders.

### Naming

Django’s generic views provide an excellent pattern for naming templates. Following design patterns already found in Django can be helpful for a couple reasons.

They have been well thought out and tested.
It makes your code immediately understandable to new developers picking up your Django code.
Most generic view templates are named in the format:

```text
[application]/[model]_[function].html
```
For example, creating a template to list all of the contacts (Contact model) in my address book (address_book application), I would use the following template:

```text
address_book/contact_list.html
```
Similarly, a detail view of a contact would use:

```text
address_book/contact_detail.html
```

Not every template you create will map so closely to a single model, however. In those cases, you’re on your own for naming, but should still keep your templates in a directory with the same name as your application.

When using inclusion tags or other other functionality to render partial templates, keep them in an includes directory inside the application template directory. For example, if I had an inclusion tag to render a contact form inside my address book application, I would create a template for it at:

```text
address_book/includes/contact_form.html
```
There is no rule (anymore) that templates must have an html file extension. If you are rendering something else (plain text, JSON, XML, etc), your templates file extension should match that of the content you are generating.

