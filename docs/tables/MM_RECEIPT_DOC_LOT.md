# MM_RECEIPT_DOC_LOT

> This table stores the EDI lot details for the T3 documentation. A new line is created for each lot.

**Description:** Receipt Document Line  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXP_DT_TM` | DATETIME |  |  | The date/time the lot expires. |
| 2 | `LOT_NUMBER_ID` | DOUBLE |  | FK→ | FK reference of the lot_number table. |
| 3 | `LOT_NUMBER_TXT` | VARCHAR(100) |  |  | Character description of the lot number as defined by the manufacturer of the lot. |
| 4 | `LOT_QTY` | DOUBLE |  |  | The quantity of the item on the line item in the particular lot. |
| 5 | `MFR_ADDR` | VARCHAR(300) |  |  | Stores the address of the manufacturer who has manufactured the supply item. |
| 6 | `MFR_NAME` | VARCHAR(60) |  |  | The manufacturer of the item. |
| 7 | `MM_RECEIPT_DOC_LINE_ID` | DOUBLE |  | FK→ | The line item that this lot is a part of. |
| 8 | `MM_RECEIPT_DOC_LOT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MM_RECEIPT_DOC_LOT table. |
| 9 | `NDC_TXT` | VARCHAR(255) |  |  | The National Drug Identifier for a medication definition item. |
| 10 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |
| `MM_RECEIPT_DOC_LINE_ID` | [MM_RECEIPT_DOC_LINE](MM_RECEIPT_DOC_LINE.md) | `MM_RECEIPT_DOC_LINE_ID` |

