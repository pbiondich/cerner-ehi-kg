# PERSON_TRIBAL_AFLTN_HIST

> Stored historical information specific to person tribal affiliation details.

**Description:** Person Tribal Affiliation History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHANGE_BIT` | DOUBLE |  |  | Identifies which columns have had a change. |
| 6 | `ENROLLED_TRIBAL_MEMBER_IND` | DOUBLE |  |  | Determine whether patient is enrolled or not for tribal member. |
| 7 | `PERSON_TRIBAL_AFLTN_HIST_ID` | DOUBLE | NOT NULL |  | Stored historical information specific to person tribal affiliation details. |
| 8 | `PERSON_TRIBAL_AFLTN_ID` | DOUBLE |  | FK→ | Person Tribal Affiliation Id that uniquely identifies a single row on the person tribal affiliation table. |
| 9 | `PM_HIST_TRACKING_ID` | DOUBLE |  | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 10 | `TRACKING_BIT` | DOUBLE |  |  | Identifies which columns are being tracked for history. |
| 11 | `TRIBAL_ENTITY_NOMENCLATURE_ID` | DOUBLE |  | FK→ | Nomenclature Id that uniquely identifies a single row on the nomenclature table. |
| 12 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_TRIBAL_AFLTN_ID` | [PERSON_TRIBAL_AFLTN](PERSON_TRIBAL_AFLTN.md) | `PERSON_TRIBAL_AFLTN_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |
| `TRIBAL_ENTITY_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

