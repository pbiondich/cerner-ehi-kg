# TIME_ZONE_R

> Contains relationships between entities like locations and Ops jobs and in what time zones they are located.

**Description:** Time zone relationship table.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique id from the table stored in parent_entity_name. E.g. the location_cd or ops_job_id which isassociated with the time_zone. |
| 2 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Table from which the parent_entity_id comes. E.g. "LOCATION" or "OPS_JOB". |
| 3 | `TIME_ZONE` | VARCHAR(100) |  |  | Time zone string from the datertl that the parent_entity_name/id is associated with. E.g. 'America/Phoenix'. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

