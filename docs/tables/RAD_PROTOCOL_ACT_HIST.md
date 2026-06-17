# RAD_PROTOCOL_ACT_HIST

> Stores the old protocol information about an order. The data on the table is not active.

**Description:** RadNet Protocol Activity History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPROVED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person that approved the protocol for this radiology order. |
| 2 | `COMMENT_TXT` | VARCHAR(512) | NOT NULL |  | Protocolling comments entered by the user. |
| 3 | `LAST_UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time this row was last updated by personnel. |
| 4 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person that last updated this row. |
| 5 | `MODIFICATION_REASON_CD` | DOUBLE | NOT NULL |  | The reason the protocol details were modified for an order. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The radiology order that the protocol is for. |
| 7 | `PROTOCOL_ID` | DOUBLE | NOT NULL | FK→ | The protocol that is pertinent for this radiology order. |
| 8 | `RAD_PROTOCOL_ACT_HIST_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a row in the RAD_PROTOCOL_ACT_HIST table. |
| 9 | `RAD_PROTOCOL_ACT_ID` | DOUBLE | NOT NULL | FK→ | The active Rad Protocol Activity row that this history record is a version of. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPROVED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_ID` | [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |
| `PROTOCOL_ID` | [RAD_PROTOCOL_DEFINITION](RAD_PROTOCOL_DEFINITION.md) | `RAD_PROTOCOL_DEFINITION_ID` |
| `RAD_PROTOCOL_ACT_ID` | [RAD_PROTOCOL_ACT](RAD_PROTOCOL_ACT.md) | `RAD_PROTOCOL_ACT_ID` |

