SELECT
    r.reseller_id,
    r.reseller_name,
    r.city,
    r.region
FROM resellers r
LEFT JOIN orders o
    ON r.reseller_id = o.reseller_id
WHERE o.order_id IS NULL;