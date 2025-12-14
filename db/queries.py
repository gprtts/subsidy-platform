SELECT_PROGRAMS = """
SELECT id, title, region, business_type, amount, source_url
FROM programs
WHERE (%s IS NULL OR region = %s)
  AND (%s IS NULL OR business_type = %s)
ORDER BY id DESC
LIMIT 100;
"""
