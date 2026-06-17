# HOLD_RULE_CONDITION

> This table identifies the hold release conditions related to a hold rule.

**Description:** Hold Rule Conditions  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Alias pool code identifies a unique set or list of person identifiers (I.e., numbers). The alias pool code also determines the accept/display format for the unique set of identifiers. |
| 3 | `ASSIGN_AUTHORITY_SYS_CD` | DOUBLE | NOT NULL |  | This field identifies whether the ESI Server received a Person_Alias that was configured for Hold. |
| 4 | `HOLD_RULE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 5 | `OP_ACTIVITY_FLAG` | DOUBLE | NOT NULL |  | This element identifies the type the hold release condition by PERSON, ENCOUNTER, ORDER, or SCH_EVENT type. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The value of the primary identifier of the table to which the phone row is related (i.e., person_id, organization_id, etc.) |
| 7 | `SEQ_NUM` | DOUBLE | NOT NULL |  | This element identifies the sequence of the hold release condition in relation to the Hold Rule ID. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HOLD_RULE_ID` | [HOLD_RULE](HOLD_RULE.md) | `HOLD_RULE_ID` |

