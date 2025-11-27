-- In stream Analytics under "Job topology" input "goodevents" that has events sorted and sent from function app, output "BeltsAlert" and "goode"
-- Sends events back to event hub to output "BeltsAlert"
SELECT * 
INTO BeltsAlert
FROM goodevents
WHERE Buckled = 'NO'

-- Sends all other records to the "goode"
Select *
INTO goode
from goodevents
