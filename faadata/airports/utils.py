from faadata.airports.models import Airport

def decide_k(airport_code):
    """A function to decide if a leading 'K' is throwing off an airport match and return the correct code."""

    if airport_code[:1].upper() == 'K':
        try: # if there's a match without the K that's likely what it is.
            return Airport.objects.get(location_identifier__iexact=airport_code[1:]).location_identifier
        except Airport.DoesNotExist:
            return airport_code
    else:
        return airport_code
