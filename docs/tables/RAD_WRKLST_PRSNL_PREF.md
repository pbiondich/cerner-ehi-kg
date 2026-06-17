# RAD_WRKLST_PRSNL_PREF

> This table models preferences for a radiologist reading worklist.

**Description:** Radiology Worklist Personnel Preference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `FAV_DISPLAY_SEQ` | DOUBLE | NOT NULL |  | Defines the order in which a favorited worklist is displayed to the user. |
| 6 | `FAV_IND` | DOUBLE | NOT NULL |  | Indicates the personnel has chosen this worklist as a favorite. |
| 7 | `MONITORED_IND` | DOUBLE | NOT NULL |  | Indicattes if the personnel wants to be notified if there are changes to the worklist. |
| 8 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | A foreign key from the prsnl table. It is the id of the person that owns the preference. |
| 9 | `RAD_WRKLST_DEF_ID` | DOUBLE | NOT NULL | FK→ | Identifies the worklist the personnel has as a preference. |
| 10 | `RAD_WRKLST_PRSNL_PREF_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RAD_WRKLST_PRSNL_PREF table. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RAD_WRKLST_DEF_ID` | [RAD_WRKLST_DEF](RAD_WRKLST_DEF.md) | `RAD_WRKLST_DEF_ID` |

