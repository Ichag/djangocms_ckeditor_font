=======================
djangocms_ckeditor_font
=======================

A django app that adds the font ckeditor plugin (http://ckeditor.com/addon/font) into djangocms's ckeditor.

Installation
============

To get started using ``djangocms_ckeditor_font``:

Todo
====

Add it to pip
- install it with ``pip``::

    $ pip install djangocms_ckeditor_font



- add the app to ``INSTALLED_APPS`` and make sure it's before ``djangocms_text_ckeditor``::

    INSTALLED_APPS = (
        ...
        'djangocms_ckeditor_font',
        'djangocms_text_ckeditor',
        ...
    )

Configuration
=============

You need a ``CKEDITOR_SETTINGS`` in ``settings.py`` that has ``toolbar_CMS`` attribute containing ``Font`` and ``FontSize``

You can copy the following configuration into your ``settings.py``::

    CKEDITOR_SETTINGS = {
        'language': '{{ language }}',
        'toolbar_CMS': [
            [ 'Source', 'Maximize' ],
            [ 'cmsplugins', '-', 'ShowBlocks' ],
            [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ],
            [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ],
            [ 'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField' ],
            [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ],
            [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language' ],
            [ 'Link', 'Unlink', 'Anchor' ],
            [ 'Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe' ],
            [ 'Styles', 'Format', 'Font', 'FontSize' ],
            [ 'TextColor', 'BGColor'],Glyphicons
            [ 'Font' ],
            [ 'FontSize' ]
        ],
        'skin': 'moono',
    }

Now when you edit any text plugin with ckeditor, you can set Font and Fontsize as inline-style.
You can adjust fonts and fontsizes throught the settings:
'font_names' and 'fontSize_sizes'.



Contribute
==========

Pull requests are very welcome!
