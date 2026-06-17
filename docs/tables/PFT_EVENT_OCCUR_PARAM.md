# PFT_EVENT_OCCUR_PARAM

> Used to store the parameters for a published event on pft_event_occur_log.

**Description:** ProFit Event Occurrence Parameter  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATE_VALUE` | DATETIME |  |  | The date value of the parameter. |
| 2 | `DOUBLE_VALUE` | DOUBLE | NOT NULL |  | The double value of the parameter. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key reference to another table that relates to this parameter. The parent entity name will identify on which table this ID originated. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Uniquely identifies the parent table related to this row. |
| 5 | `PFT_EVENT_OCCUR_LOG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related PFT_EVENT_OCCUR_LOG record. |
| 6 | `PFT_EVENT_OCCUR_PARAM_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the pftevent_occur_params table. |
| 7 | `PFT_EVENT_PARAM_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the value for the event parameter. Uses code set # 24454. |
| 8 | `STRING_VALUE` | VARCHAR(500) | NOT NULL |  | String value of the parameter. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_EVENT_OCCUR_LOG_ID` | [PFT_EVENT_OCCUR_LOG](PFT_EVENT_OCCUR_LOG.md) | `PFT_EVENT_OCCUR_LOG_ID` |

