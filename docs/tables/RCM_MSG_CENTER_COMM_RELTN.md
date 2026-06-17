# RCM_MSG_CENTER_COMM_RELTN

> Links the Message Center communication recorded on the RCM_MSG_CENTYER_COMM table with one or more recipients.

**Description:** RevWorks Care Management - Message Center Communication Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RCM_MSG_CENTER_COMM_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the RCM_MSG_CENTER_COMM table. |
| 2 | `RCM_MSG_CENTER_COMM_RELTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between the RCM_MSG_CENTER_COMM table and one or more recipients. |
| 3 | `RECIPIENT_CC_IND` | DOUBLE | NOT NULL |  | The indicator of the carbon copy recipient. |
| 4 | `RECIPIENT_PRSNL_GROUP_ID` | DOUBLE | NOT NULL |  | Identifies the personnel group to which this record is related. |
| 5 | `RECIPIENT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the recipient of the message that was sent. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RCM_MSG_CENTER_COMM_ID` | [RCM_MSG_CENTER_COMM](RCM_MSG_CENTER_COMM.md) | `RCM_MSG_CENTER_COMM_ID` |
| `RECIPIENT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

