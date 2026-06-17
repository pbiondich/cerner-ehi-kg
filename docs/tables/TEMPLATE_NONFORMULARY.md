# TEMPLATE_NONFORMULARY

> Order model tables for storing off adhoc orderables.

**Description:** TEMPLATE NONFORMULARY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | Action sequence of order. |
| 2 | `COST` | DOUBLE |  |  | Cost associated with a given formulary item |
| 3 | `DESCRIPTION` | VARCHAR(100) |  |  | Free-text description of the non-formulary item |
| 4 | `LEGAL_STATUS_CD` | DOUBLE | NOT NULL |  | Legal Status Code value |
| 5 | `NDC` | VARCHAR(50) |  |  | National Drug Code (US FDA) number assigned to this product |
| 6 | `PKG_DISP_MORE_IND` | DOUBLE | NOT NULL |  | Indicates whether or not to dispense more than needed, when using Package Supply dispensing method. |
| 7 | `PKG_QTY_PER_PKG` | DOUBLE | NOT NULL |  | Indicates quantity of the product within a single package. |
| 8 | `SHELL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Item_id of the non-formulary template. |
| 9 | `TNF_ID` | DOUBLE | NOT NULL |  | Unique identifier for this non-formulary item |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SHELL_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |

