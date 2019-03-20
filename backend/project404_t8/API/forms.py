from django import forms

# This must support markdown
# Maybe have a button that tells the post to display it in markdown
# When the user selects 2/shared author, another HTML form should become unhidden
# I assume we would use JavaScript for this, possibly vue
privacyOptions = [
    ("1", "Just Me"), 
    ("2","One other person"), 
    ("3", "Friends"), 
    ("4", "Friends of Friends"),
    ("5", "Only Friends on Connectify"),
    ("6","Public"),
    ("7","Unlisted")]

    # unlisted posts should generate a random post ID (check its not taken first)
    # large scale could be done better, for now can do it more simply

class uploadForm(forms.Form):
    # Need an invisible field that sends the user ID
    # Alternatively could just post infer it when the user posts the form in the view
    # Furthermore, a post should require at least a summary or an image
    title = forms.CharField(label='Title', max_length=24)
    body = forms.CharField(label='Body', max_length=250, required = False, widget=forms.Textarea)
    markdown = forms.BooleanField(required = False)
    imageLink = forms.ImageField(label="Image",required = False)
    privacy = forms.CharField(label='Privacy', widget=forms.Select(choices=privacyOptions))
    # If we wanted to get fancy, this could autofill from the user's friends
    sharedAuthor = forms.CharField(label='Shared Author', required = False)

class friendRequestForm(forms.Form):
    # Basically will just be a char field
    # Actually, this should just be a button that appears on a users profile
    # So to be even more honest we might not even need a form for this, but its
    # not a big deal right now
    friendToAdd = forms.CharField(label="Username", max_length=255)