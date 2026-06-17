# MM_XFI_ASN_LOT

> To store the advanced shipment notification for lot information

**Description:** ADVANCED SHIPMENT NOTIFICATION LOT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXP_DT_TM` | DATETIME |  |  | The date/time an item will expire. |
| 2 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the existing lot in the system. If the value is zero, then a new lot is being passed for the asn line item item. Originates on LOT_NUMBER_INFO. LOT_NUMBER_ID. |
| 3 | `LOT_NUMBER_TXT` | VARCHAR(100) |  |  | Character description of the lot number as defined by the manufacturer of the lot. |
| 4 | `LOT_QTY` | DOUBLE |  |  | Numeric value of units shipped in manufacturer's shipping units for the corresponding lot number. |
| 5 | `MANF_DT_TM` | DATETIME |  |  | Date and time this item in the lot was manufactured. |
| 6 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | The code value(Code set 221) representing the manufacturer for the lot |
| 7 | `MANUFACTURER_NAME` | VARCHAR(100) |  |  | Manufacturer¿s name for the respective lot number that is being passed as the part of asn line item. |
| 8 | `NDC_TXT` | VARCHAR(255) |  |  | Drug Identifier for medication definition item. Drug Identifier is mandatory for medication definition items having lot tracking set as Incoming lot level and ;Lot level. |
| 9 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MM_XFI_ASN_LOT table. |
| 10 | `TRANS_LINE_ID` | DOUBLE | NOT NULL | FK→ | Maps a lot to the respective asn line item. Originates on MM_XFI_ASN_LINE.transaction_id. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |
| `TRANS_LINE_ID` | [MM_XFI_ASN_LINE](MM_XFI_ASN_LINE.md) | `TRANSACTION_ID` |

