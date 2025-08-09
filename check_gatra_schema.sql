-- Query to check your existing SIEM events table schema
-- Run this in BigQuery to see what columns are available

-- Check table schema
SELECT column_name, data_type, is_nullable, description
FROM `chronicle-dev-2be9.gatra_database.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'siem_events'
ORDER BY ordinal_position;

-- Check sample data (first 5 rows)
SELECT *
FROM `chronicle-dev-2be9.gatra_database.siem_events`
LIMIT 5;

-- Get basic statistics
SELECT 
    COUNT(*) as total_rows,
    COUNT(DISTINCT DATE(timestamp)) as days_of_data,
    MIN(timestamp) as earliest_event,
    MAX(timestamp) as latest_event
FROM `chronicle-dev-2be9.gatra_database.siem_events`
WHERE timestamp IS NOT NULL;

-- Check what columns might be available for severity/priority
SELECT 
    column_name,
    COUNT(DISTINCT column_name) as distinct_values
FROM `chronicle-dev-2be9.gatra_database.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'siem_events'
  AND LOWER(column_name) LIKE '%sever%' 
   OR LOWER(column_name) LIKE '%prior%'
   OR LOWER(column_name) LIKE '%level%'
   OR LOWER(column_name) LIKE '%risk%'
GROUP BY column_name;
