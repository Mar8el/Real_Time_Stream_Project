create or ALTER view dbo.badalerts
as
select * FROM
    OPENROWSET (
        bulk 'https://adlslivedata2025.dfs.core.windows.net/azure-webjobs-eventhub/iot/badalerts/*.parquet',
        format = 'parquet'
    ) as [result]





create or ALTER view dbo.goodevents
as
select * FROM
    OPENROWSET (
        bulk 'https://adlslivedata2025.dfs.core.windows.net/azure-webjobs-eventhub/iot/iotdata/*.parquet',
        format = 'parquet'
    ) as [result]




create or ALTER view dbo.driversbeltsalert
as
select * FROM
    OPENROWSET (
        bulk 'https://adlslivedata2025.dfs.core.windows.net/azure-webjobs-eventhub/iot/belts/DriverBelts/*.parquet',
        format = 'parquet'
    ) as [result]


