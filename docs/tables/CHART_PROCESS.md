# CHART_PROCESS

> stores chart level information such as allocation date and chart status

**Description:** ProFile chart processing table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABSTRACT_COMPLETE_IND` | DOUBLE |  |  | This indicator is used to identify which charts have been abstracted |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ALLOCATION_DT_FLAG` | DOUBLE |  |  | This flexes how allocation date is calculated |
| 7 | `ALLOCATION_DT_MODIFIER` | DOUBLE |  |  | The number of days to add to an event's date in calculating the allocation date. |
| 8 | `ALLOCATION_DT_TM` | DATETIME |  |  | The date and time that the chart is allocated (or made available) to a physician for completion. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `CHART_PROCESS_ID` | DOUBLE | NOT NULL |  | The unique identifier of the chart process table |
| 11 | `CHART_STATUS_CD` | DOUBLE |  |  | Code for the status of the chart |
| 12 | `CHART_STATUS_DT_TM` | DATETIME |  |  | The date and time the chart status was assigned |
| 13 | `ENCNTR_ID` | DOUBLE |  | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `PERSON_ID` | DOUBLE |  | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

