# ENCNTR_CARE_MGMT

> Stores care management fields for an encounter.

**Description:** Encounter Care Management  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CLINICAL_REVIEW_DUE_DT_TM` | DATETIME |  |  | The date and time of when the next clinical review is due for this encounter. |
| 6 | `DISCH_PLAN_DUE_DT_TM` | DATETIME |  |  | The date and time of when the next discharge plan is due for this encounter. |
| 7 | `DISCH_PLAN_STATUS_CD` | DOUBLE | NOT NULL |  | The discharge plan status for this encounter. |
| 8 | `DOCUMENT_REVIEW_DUE_DT_TM` | DATETIME |  |  | The date and time of when the next document review is due for this encounter. |
| 9 | `DOCUMENT_REVIEW_STATUS_CD` | DOUBLE | NOT NULL |  | The document review status for this encounter. |
| 10 | `ENCNTR_CARE_MGMT_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally assigned number. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the Encounter table. It identifies which encounter the care management information is for. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `UTLZTN_MGMT_STATUS_CD` | DOUBLE | NOT NULL |  | The clinical utilization status for this encounter. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

