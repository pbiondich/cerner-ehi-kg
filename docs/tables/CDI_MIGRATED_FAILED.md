# CDI_MIGRATED_FAILED

> This table contains identifier of objects that failed to migrate from CAMM 6 to CAMM 7

**Description:** cdi_migrated_failed  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_MIGRATED_FAILED_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the cdi_migrated_failed table. |
| 2 | `FAILED_TS` | DATETIME(6) |  |  | The timestamp that the object was attempted to be migrated |
| 3 | `FROM_LOCATION` | VARCHAR(128) |  |  | The intended source url |
| 4 | `OBJECT_IDENT` | VARCHAR(128) |  |  | The CAMM object identifier of the CAMM object that failed to migrate |
| 5 | `REASON_TEXT` | VARCHAR(4000) |  |  | The reason for the failure |
| 6 | `TO_LOCATION` | VARCHAR(128) |  |  | The intended destination url |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

