from db.client import supabase

def fetch_geo():
  return supabase.table('geo').select("*").execute()