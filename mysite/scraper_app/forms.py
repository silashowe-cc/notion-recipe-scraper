from django import forms

emoji_choices = (
    ("🍇", "🍇"),("🍈", "🍈"),("🍊", "🍊"),("🍋", "🍋"),("🍌", "🍌"),
    ("🍍", "🍍"),("🥭", "🥭"),("🍎", "🍎"),("🍏", "🍏"),("🍉", "🍉"),
    ("🍐", "🍐"),("🍑", "🍑"),("🍒", "🍒"),("🍓", "🍓"),("🥝", "🥝"),
    ("🍅", "🍅"),("🥥", "🥥"),("🥑", "🥑"),("🍆", "🍆"),("🥔", "🥔"),
    ("🥕", "🥕"),("🌽", "🌽"),("🌶", "🌶"),("🥒", "🥒"),("🥬", "🥬"),
    ("🥦", "🥦"),("🍄", "🍄"),("🥜", "🥜"),("🌰", "🌰"),("🍞", "🍞"),
    ("🥐", "🥐"),("🥖", "🥖"),("🥨", "🥨"),("🥯", "🥯"),("🥞", "🥞"),
    ("🧀", "🧀"),("🍖", "🍖"),("🍗", "🍗"),("🥩", "🥩"),("🥓", "🥓"),
    ("🍔", "🍔"),("🍟", "🍟"),("🍕", "🍕"),("🌭", "🌭"),("🥪", "🥪"),
    ("🌮", "🌮"),("🌯", "🌯"),("🥙", "🥙"),("🥚", "🥚"),("🍳", "🍳"),
    ("🥘", "🥘"),("🍲", "🍲"),("🥣", "🥣"),("🥗", "🥗"),("🍿", "🍿"),
    ("🧂", "🧂"),("🥫", "🥫"),("🍱", "🍱"),("🍘", "🍘"),("🍙", "🍙"),
    ("🍛", "🍛"),("🍜", "🍜"),("🍝", "🍝"),("🍠", "🍠"),("🍢", "🍢"),
    ("🍣", "🍣"),("🍤", "🍤"),("🍥", "🍥"),("🥮", "🥮"),("🍡", "🍡"),
    ("🥟", "🥟"),("🥠", "🥠"),("🥡", "🥡"),("🦀", "🦀"),("🦞", "🦞"),
    ("🦐", "🦐"),("🦑", "🦑"),("🍦", "🍦"),("🍧", "🍧"),("🍨", "🍨"),
    ("🍩", "🍩"),("🍪", "🍪"),("🎂", "🎂"),("🍰", "🍰"),("🧁", "🧁"),
    ("🥧", "🥧"),("🍫", "🍫"),("🍬", "🍬"),("🍭", "🍭"),("🍮", "🍮"),
    ("🍯", "🍯"),("🍼", "🍼"),("🥛", "🥛"),("☕", "☕"),("🍵", "🍵"),
    ("🍶", "🍶"),("🍾", "🍾"),("🍷", "🍷"),("🍸", "🍸"),("🍹", "🍹"),
    ("🍺", "🍺"),("🍻", "🍻"),("🥂", "🥂"),("🥃", "🥃"),("🥤", "🥤"),
    ("🥢", "🥢"),("🍽", "🍽"),("🍴", "🍴"),("🥄", "🥄"),("🔪", "🔪"),
    ("🏺", "🏺")
)
class ScraperForm(forms.Form):
    token = forms.CharField(max_length=100)
    dbid = forms.CharField(max_length=100)
    recipe_url = forms.URLField()
    icon = forms.ChoiceField(choices = emoji_choices)