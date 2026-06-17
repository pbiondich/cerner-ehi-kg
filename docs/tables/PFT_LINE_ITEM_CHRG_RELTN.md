# PFT_LINE_ITEM_CHRG_RELTN

> Stores the relationship of charges to line items.

**Description:** ProFit Line Item Charge Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PFT_CHARGE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the relationship to the PFT_CHARGE table |
| 2 | `PFT_LINE_ITEM_CHRG_RELTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the charge for a specific line item |
| 3 | `PFT_LINE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the relationship to the PFT_LINE_ITEM table |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_CHARGE_ID` | [PFT_CHARGE](PFT_CHARGE.md) | `PFT_CHARGE_ID` |
| `PFT_LINE_ITEM_ID` | [PFT_LINE_ITEM](PFT_LINE_ITEM.md) | `PFT_LINE_ITEM_ID` |

