# OMF_STUDY_GROUP_TYPE

> Study group types.

**Description:** Holds study group types such as PHYSICIAN, PATIENT, etc.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(255) |  |  | Description of what this study group type is used for. |
| 2 | `DISPLAY_FUNCTION` | VARCHAR(255) |  |  | Function which can be used to re-display the ID - e.g. omf_get_pers_full for PATIENT and PHYSICIAN. |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(255) |  |  | Parent table for IDs that will be stored in this study group. |
| 4 | `SG_TYPE` | VARCHAR(50) | NOT NULL |  | Study group type. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

