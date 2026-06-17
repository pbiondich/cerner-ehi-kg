# IB_RX_REQ_ACTION

> Contains actions taken on prescription requests from a foreign pharmacy system.

**Description:** Inbound Rx Request Action  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | The date and time there match was made either by the system or by a user. |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who took the action. Actions can also be taken by the system, so in that case, this field will have a zero. |
| 3 | `ACTION_SEQ_NBR` | DOUBLE | NOT NULL |  | The sequence number for the order the actions were taken. |
| 4 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `APPROVED_ORDER_ID` | DOUBLE |  | FK→ | The approved order identifier that replaces the originally referenced order. |
| 6 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The time at which the action was taken. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `IB_RX_REQ_ACTION_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies an individual row on the IB_RX_REQ_ACTION table. |
| 9 | `IB_RX_REQ_ID` | DOUBLE | NOT NULL | FK→ | The related inbound prescription request. |
| 10 | `PROPOSED_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter that is currently related to the inbound prescription request. |
| 11 | `PROPOSED_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The patient that is currently related to the inbound prescription request. |
| 12 | `REQ_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the prescription request. Examples of code meanings are: UNMATCHED, SYS_MATCH_P, SYS_MATCH_O, VERIFIED, ACCEPTED, REJECTED, REPLACED. |
| 13 | `TRANS_IDENT` | VARCHAR(255) |  |  | The unique transaction identifier for an outbound rx change deny or approve call to the foreign system. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `APPROVED_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `IB_RX_REQ_ID` | [IB_RX_REQ](IB_RX_REQ.md) | `IB_RX_REQ_ID` |
| `PROPOSED_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PROPOSED_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

