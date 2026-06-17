# RC_CONT_MODEL_EVENT_RELTN

> This table stores the relation between an event happening in the system and the workflow model.

**Description:** Revenue Cycle Continuity Model Event Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `EVENT_CD` | DOUBLE | NOT NULL |  | Stores information about the automated system or user event that happens in the system. |
| 4 | `EVENT_MODEL_RELTN_TYPE_FLAG` | DOUBLE | NOT NULL |  | Stores information about how a particular event is related to the model. The relationship can be a pause, resume, cancel or reset. Based on these relations, the system will take appropriate action. |
| 5 | `RC_CONT_MODEL_EVENT_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RC_CONT_MODEL_EVENT_RELTN table. |
| 6 | `RC_CONT_MODEL_ID` | DOUBLE | NOT NULL | FK→ | Stores the link to the table which stores workflow model reference data. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RC_CONT_MODEL_ID` | [RC_CONT_MODEL](RC_CONT_MODEL.md) | `RC_CONT_MODEL_ID` |

