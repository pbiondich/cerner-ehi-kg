# EEM_PROFILE_POPULATE

> This table will store the populate build data for profiles. The transaction response element will be related to the registration prompt field to determine where each response element should be populated per profile.

**Description:** EEM Profile Populate  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BLANK_OVERRIDE_IND` | DOUBLE | NOT NULL |  | Identifies if the system will populate with a blank value. |
| 4 | `EEM_PROFILE_POPULATE_ID` | DOUBLE | NOT NULL |  | This is the unique primary key of this table. It is an internally generated sequence number. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FIELD` | VARCHAR(255) | NOT NULL |  | Identifies the registration prompt field from pm_flx_prompt. This is the field the data will be populated to. |
| 7 | `POPULATE_ELEMENT_CD` | DOUBLE | NOT NULL |  | Identifies the EEM Populate Element. This is the transaction response element that will be populated. |
| 8 | `PROFILE_ID` | DOUBLE | NOT NULL | FK→ | This is the unique primary identifier of the eem_profile table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROFILE_ID` | [EEM_PROFILE](EEM_PROFILE.md) | `PROFILE_ID` |

