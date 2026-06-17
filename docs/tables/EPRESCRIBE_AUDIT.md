# EPRESCRIBE_AUDIT

> This table contains order related information for every prescription order that is electronically routed to a pharmacy.

**Description:** Eprescribe Audit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EPRESCRIBE_AUDIT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the EPRESCRIBE_AUDIT table. |
| 2 | `FORMULARY_BENEFIT_IND` | DOUBLE | NOT NULL |  | Indicates if the formulary benefit information was made available to the provider. |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the order being audited. |
| 4 | `PHARMACY_IDENT` | VARCHAR(100) |  |  | External pharmacy identifier to which the order has been routed. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

