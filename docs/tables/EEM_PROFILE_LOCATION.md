# EEM_PROFILE_LOCATION

> This table is used to store profile information that varies by location.

**Description:** EEM Profile Location  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EEM_PROFILE_LOCATION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the EEM_PROFILE_LOCATION table. |
| 2 | `FACILITY_IDENT` | VARCHAR(15) |  |  | Third party assigned identifier for a facility. |
| 3 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Location identifier for which the profile information is being stored. |
| 4 | `PROFILE_ID` | DOUBLE | NOT NULL | FK→ | The ID of the profile associated to the location. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `USER_IDENT` | VARCHAR(15) |  |  | Third party assigned identifier for a user. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PROFILE_ID` | [EEM_PROFILE](EEM_PROFILE.md) | `PROFILE_ID` |

