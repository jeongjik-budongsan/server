from db.client import supabase

def average(reviews):
  if len(reviews) == 0:
    return 0
  return sum([review['point'] for review in reviews]) / len(reviews)

def fetch_agencies(geo_id: int):
  agencies =  supabase.table('agency')\
    .select("*")\
    .eq('geo_id', geo_id)\
    .execute()
  
  agency_ids = [agency['id'] for agency in agencies.data]
  reviews = supabase.table('reviews')\
    .select("*")\
    .in_('agency_id', agency_ids)\
    .execute().data
  
  for agency in agencies.data:
    reviews = [review for review in reviews if review['agency_id'] == agency['id']]
    agency['review'] = {
      'items': reviews,
      'average': average(reviews)
    }
  
  return agencies