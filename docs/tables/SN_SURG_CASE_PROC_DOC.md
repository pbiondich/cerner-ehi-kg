# SN_SURG_CASE_PROC_DOC

> SurgiNet Surgical Case Procedure Document

**Description:** SN SURG CASE PROC DOC  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CREATE_APPLCTX` | DOUBLE |  |  | Create Application Context |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | Create Date and Time |
| 8 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | Create Personnel ID |
| 9 | `CREATE_TASK` | DOUBLE |  |  | Create TaskColumn |
| 10 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The document type that this procedure and preference card belongs to. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `PICK_LIST_CHG_FLAG` | DOUBLE |  |  | Used when something is changed for a filled case that would directly affect what pick list is needed. |
| 13 | `PREF_CARD_ID` | DOUBLE | NOT NULL | FK→ | The Preference Card ID being used for this procedure and document |
| 14 | `PREF_CARD_SECTIONS` | DOUBLE | NOT NULL |  | The preference Card Sections that are being used |
| 15 | `SURG_CASE_PROC_DOC_ID` | DOUBLE | NOT NULL |  | The unique ID for this table |
| 16 | `SURG_CASE_PROC_ID` | DOUBLE | NOT NULL | FK→ | The Surgical Case Procedure Id for the Procedure and document |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREF_CARD_ID` | [PREFERENCE_CARD](PREFERENCE_CARD.md) | `PREF_CARD_ID` |
| `SURG_CASE_PROC_ID` | [SURG_CASE_PROCEDURE](SURG_CASE_PROCEDURE.md) | `SURG_CASE_PROC_ID` |

