# RX_AUTO_VERIFY_ING_AUDIT

> The table is used to log order ingredient information relevant to auto verification decision.

**Description:** Pharmarcy auto verify ingredient audit table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL | FK→ | ID of the order sentence that matches order detail information on the ingredient. |
| 2 | `RX_AUTO_VERIFY_AUDIT_ID` | DOUBLE | NOT NULL | FK→ | Rx auto verification audit ID to which this record is associated. |
| 3 | `RX_AUTO_VERIFY_ING_AUDIT_ID` | DOUBLE | NOT NULL |  | Unique identifier for rx auto verification audit at ingredient level. |
| 4 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Order catalog synonym id to which the ingredient is associated. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_SENTENCE_ID` | [ORDER_SENTENCE](ORDER_SENTENCE.md) | `ORDER_SENTENCE_ID` |
| `RX_AUTO_VERIFY_AUDIT_ID` | [RX_AUTO_VERIFY_AUDIT](RX_AUTO_VERIFY_AUDIT.md) | `RX_AUTO_VERIFY_AUDIT_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

