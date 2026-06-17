# RCA_CONV_GROUP_CONV_R

> Stores the relationship between conversation groups and conversations.

**Description:** Revenue Cycle Ambulatory Conversation Group Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RCA_CONVERSATION_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier that identifies a single row on the RCA_CONVERSATION table across domains that is related to the conversation group on this row. |
| 2 | `RCA_CONV_GROUP_CONV_R_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RCA_CONV_GROUP_CONV_R table. |
| 3 | `RCA_CONV_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier that identifies a single row on the RCA_CONVERSATION_GROUP table across domains that is related to the conversation on this row. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RCA_CONVERSATION_ID` | [RCA_CONVERSATION](RCA_CONVERSATION.md) | `RCA_CONVERSATION_ID` |
| `RCA_CONV_GROUP_ID` | [RCA_CONV_GROUP](RCA_CONV_GROUP.md) | `RCA_CONV_GROUP_ID` |

