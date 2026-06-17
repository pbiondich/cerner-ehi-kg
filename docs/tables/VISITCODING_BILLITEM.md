# VISITCODING_BILLITEM

> The subtable for audit trail serving as a pointer to the list of bill items that were selected during professional coding.

**Description:** Coding Audit Bill Items  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | foreign key from BILL_ITEM |
| 2 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 3 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 4 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 6 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `VISITCODING_AUDIT_ID` | DOUBLE | NOT NULL | FK→ | FOREIGN KEY TO TRACKING AUDIT |
| 8 | `VISITCODING_BILLITEM_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 9 | `VISITCODING_DX_ID` | DOUBLE | NOT NULL | FK→ | FOREIGN KEY VALUE FROM VISITCODING_DX |
| 10 | `VISITCODING_MODIFIER_ID` | DOUBLE | NOT NULL | FK→ | FOREIGN KEY VALUE FROM VISITCODING_MODIFIER |
| 11 | `VISITCODING_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | FOREIGN KEY VALUE FROM VISITCODING_PROVIDER |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILL_ITEM_ID` | [BILL_ITEM](BILL_ITEM.md) | `BILL_ITEM_ID` |
| `VISITCODING_AUDIT_ID` | [VISITCODING_AUDIT](VISITCODING_AUDIT.md) | `VISITCODING_AUDIT_ID` |
| `VISITCODING_DX_ID` | [VISITCODING_DX](VISITCODING_DX.md) | `VISITCODING_DX_ID` |
| `VISITCODING_MODIFIER_ID` | [VISITCODING_MODIFIER](VISITCODING_MODIFIER.md) | `VISITCODING_MODIFIER_ID` |
| `VISITCODING_PROVIDER_ID` | [VISITCODING_PROVIDER](VISITCODING_PROVIDER.md) | `VISITCODING_PROVIDER_ID` |

