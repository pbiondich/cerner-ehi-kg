# LH_CNT_REHAB_EVENT

> This table will store rehab productivity events as defined in bedrock.

**Description:** LH_CNT_REHAB_EVENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EVAL_EVENT_FLAG` | DOUBLE | NOT NULL |  | This field indicates whether the event is an evaluation, re-evaluation, or neither. 0 - Neither , 1 - Evaluation, 2 - Reevaluation. |
| 3 | `EVENT_END_DT_TM` | DATETIME |  |  | Date/time that the event occurred. |
| 4 | `EVENT_ID` | DOUBLE | NOT NULL |  | Event_ID of the rehab productivity event from clinical_event. |
| 5 | `LH_CNT_REHAB_EVENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_REHAB_EVENT table. |
| 6 | `MISSED_IND` | DOUBLE | NOT NULL |  | Designates an event as a 'units lost' event. |
| 7 | `PERFORM_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person_ID of the personnel who performed the event. |
| 8 | `REASON_EVENT_ID` | DOUBLE | NOT NULL |  | Event_ID of the rehab productivity reason from clinical_event. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERFORM_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

