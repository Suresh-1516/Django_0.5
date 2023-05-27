from django.contrib import admin

from .models import Profile
from .models import Save_code
from .models import Premium
from .models import Data
from .models import htmlquestion
from .models import Doubt
from .models import Feedback
from .models import Payment
from .models import Notes


admin.site.register(Profile)
admin.site.register(Save_code)
admin.site.register(Premium)
admin.site.register(Data)
admin.site.register(htmlquestion)
admin.site.register(Doubt)
admin.site.register(Payment)
admin.site.register(Feedback)
admin.site.register(Notes)
