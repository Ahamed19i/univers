
# context_processors.py
from .models import Etudiant

def etudiant_context(request):
    if request.user.is_authenticated and hasattr(request.user, 'etudiant'):
        etudiant = request.user.etudiant
    else:
        etudiant = None
    return {
        'etudiant': etudiant,
    }
