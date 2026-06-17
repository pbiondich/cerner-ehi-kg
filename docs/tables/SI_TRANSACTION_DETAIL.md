# SI_TRANSACTION_DETAIL

> Metadata details about si transactions or transaction sets

**Description:** System Integration Transaction Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTRIBUTE_NAME` | VARCHAR(12) | NOT NULL |  | Name of non-entity attribute |
| 2 | `ATTRIBUTE_VALUE` | VARCHAR(256) | NOT NULL |  | Value of non-entity attribute |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | PARENT ENTITY |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent entity to which the parent entity id pertains |
| 5 | `SI_TRANSACTION_DETAIL_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `SI_TRANSACTION_ID` | DOUBLE | NOT NULL | FK→ | SI Transaction for which this detail pertains |
| 7 | `SI_TRANSACTION_SET_ID` | DOUBLE | NOT NULL | FK→ | SI Transaction Set for which this detail pertains |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_TRANSACTION_ID` | [SI_TRANSACTION](SI_TRANSACTION.md) | `SI_TRANSACTION_ID` |
| `SI_TRANSACTION_SET_ID` | [SI_TRANSACTION_SET](SI_TRANSACTION_SET.md) | `SI_TRANSACTION_SET_ID` |

