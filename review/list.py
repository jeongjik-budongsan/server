from db.client import supabase

def fetch_reviews(agency_id: int):
  return supabase.table('reviews')\
    .select("*")\
    .eq('agency_id', agency_id)\
    .execute()