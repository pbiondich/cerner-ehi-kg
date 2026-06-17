# RCA_CONV_GROUP_POSITION_R

> Defines the relationship between a Conversation Group and a list of one to many user positions.

**Description:** Revenue Cycle Ambulatory Conversation Group Position Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position code that has a relationship with the conversation group. |
| 2 | `RCA_CONV_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier that identifies a single row on the RCA_CONV_GROUP table across domains and has a relationship with the position code on this row. |
| 3 | `RCA_CONV_GROUP_POSITION_R_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RCA_CONV_GROUP_POSITION_R table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RCA_CONV_GROUP_ID` | [RCA_CONV_GROUP](RCA_CONV_GROUP.md) | `RCA_CONV_GROUP_ID` |

