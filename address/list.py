from db.client import supabase

def fetch_addresses():
  response = supabase.table('address').select("*").execute()
  return response