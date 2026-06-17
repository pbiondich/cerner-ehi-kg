# ORG_PER_TIMEZONE_GTTD

> This Global Temporary table will be used to load the organizations in a particular time zone which will be used for processing in the GSR jobs.

**Description:** Organizations Per Time Zone Global Temporary Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOGICAL_DOMAIN_ID` | DOUBLE |  |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 2 | `ORGANIZATION_ID` | DOUBLE |  |  | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 3 | `TIME_ZONE` | VARCHAR(100) |  |  | Time zone string from the datertl that the parent_entity_name/id is associated with. E.g. 'America/Phoenix'. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

