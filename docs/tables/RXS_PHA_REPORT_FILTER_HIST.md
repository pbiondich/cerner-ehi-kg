# RXS_PHA_REPORT_FILTER_HIST

> History of filters used while executing a reports

**Description:** RxStation Pharmacy Report Filter History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILTER_VALUE` | VARCHAR(100) | NOT NULL |  | Actual value set for the filter |
| 2 | `PARENT_ENTITY_ID` | DOUBLE |  |  | identifier for the filter in the report like item_id, code_value,person_id, personnel id, work-list id etc. |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Table name that the value in column parent_entity_id originates. |
| 4 | `PHA_BATCH_REPORT_ACT_ID` | DOUBLE | NOT NULL | FK→ | The report run activity identifier this filter is associated with. |
| 5 | `REPORT_FILTER_CD` | DOUBLE | NOT NULL |  | The type of report filter. |
| 6 | `RXS_PHA_REPORT_FILTER_HIST_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RXS_PHA_REPORT_FILTER_HIST table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PHA_BATCH_REPORT_ACT_ID` | [PHA_BATCH_REPORT_ACT](PHA_BATCH_REPORT_ACT.md) | `PHA_BATCH_REPORT_ACT_ID` |

