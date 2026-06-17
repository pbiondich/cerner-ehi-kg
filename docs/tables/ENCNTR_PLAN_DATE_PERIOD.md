# ENCNTR_PLAN_DATE_PERIOD

> The encounter health plan date period table is a generic table for storing date range(s) of various components of the encounter health plan data model (e.g. eligibilities and benefits etc...) . Information will typically be obtained from a payer via an X12 transaction but may also be added or modified directly by the end user.

**Description:** Encounter Plan Date Period  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_PLAN_DATE_PERIOD_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `DATE_PERIOD_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of date/time period for this row. |
| 6 | `ENCNTR_PLAN_DATE_PERIOD_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the encntr_plan_date_period table. It's an internally assigned number and generally not revealed to the user. |
| 7 | `FIRST_DATE` | DATETIME |  |  | The first date in the period. Although this column is capable of storing the time component of a date, it should be ignored since date periods from an X12 transaction do not contain a time component. This date should be treated as an absolute date and the standard Millennium practice of UTC/Local time zone translations should not be applied when reading and writing to this column. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent table to which this data belongs. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The upper case name of the parent table to which this data belongs. |
| 10 | `SECOND_DATE` | DATETIME |  |  | The second date in the period. Although this column is capable of storing the time component of a date, it should be ignored since date periods from an X12 transaction do not contain a time component. This date should be treated as an absolute date and the standard Millennium practice of UTC/Local time zone translations should not be applied when reading and writing to this column. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_PLAN_DATE_PRD_HIST](ENCNTR_PLAN_DATE_PRD_HIST.md) | `ENCNTR_PLAN_DATE_PERIOD_ID` |

