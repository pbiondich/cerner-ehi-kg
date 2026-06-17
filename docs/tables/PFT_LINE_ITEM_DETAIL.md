# PFT_LINE_ITEM_DETAIL

> Additional information related to Line_item is saved in pft_line_item_details table.

**Description:** ProFit Line Item Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 3 | `LINE_ITEM_DETAIL_TXT` | VARCHAR(250) | NOT NULL |  | Contains additional information about the claim line item |
| 4 | `PFT_LINE_ITEM_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PFT_LINE_ITEM_DETAIL table. |
| 5 | `PFT_LINE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the PFT_LINE_ITEM table. |
| 6 | `TYPE_CD` | DOUBLE | NOT NULL |  | Type code identified for the claim |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_LINE_ITEM_ID` | [PFT_LINE_ITEM](PFT_LINE_ITEM.md) | `PFT_LINE_ITEM_ID` |

