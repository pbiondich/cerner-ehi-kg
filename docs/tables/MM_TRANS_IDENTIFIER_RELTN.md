# MM_TRANS_IDENTIFIER_RELTN

> Holds the barcode information for the performed transaction.

**Description:** Transaction Identifier Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BARCODE_TXT` | VARCHAR(255) |  |  | The text for the item read from the barcode. |
| 3 | `LOT_NUMBER_ID` | DOUBLE |  | FK→ | The lot number that the trans_line is related to. |
| 4 | `MM_TRANS_IDENTIFIER_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that defines a single row on the MM_TRANS_IDENTIFIER_RELTN table. |
| 5 | `MM_TRANS_LINE_ID` | DOUBLE |  | FK→ | The transaction line associated to this serial number, lot number, or item identifier. |
| 6 | `SERIAL_NBR_TXT` | VARCHAR(255) |  |  | Serial number of the item. |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |
| `MM_TRANS_LINE_ID` | [MM_TRANS_LINE](MM_TRANS_LINE.md) | `MM_TRANS_LINE_ID` |

