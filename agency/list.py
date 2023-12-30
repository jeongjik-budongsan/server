from db.client import supabase

def fetch_agencies(geo_id: int):
  return supabase.table('agency')\
    .select("*")\
    .eq('geo_id', geo_id)\
    .execute()