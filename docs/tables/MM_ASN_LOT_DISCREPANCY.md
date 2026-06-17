# MM_ASN_LOT_DISCREPANCY

> To log the quantity discrepancy between the ASN and physically received lot for the line item.

**Description:** Advanced Shipment Notification Lot Discrepancy  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASN_LOT_IND` | DOUBLE |  |  | This field will say whether the given lot exists in ASN (Advanced Shipping Notification) |
| 2 | `ASN_LOT_QTY` | DOUBLE |  |  | Numeric value of units mentioned in the advanced shipment notification for the corresponding lot number. |
| 3 | `LOT_NBR_TEXT` | VARCHAR(255) | NOT NULL |  | Identifies the lot number of the line item which is having either lot number or lot quantity discreapncy. |
| 4 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | The code value(Code set 221) representing the manufacturer for the lot. This can be 0. |
| 5 | `MM_ASN_LINE_DISCREPANCY_ID` | DOUBLE | NOT NULL | FK→ | Used to map a lot to the respective line item. Originates on MM_ASN_LINE_DISCREPANCY.MM_ASN_LINE_DISCREPANCY_ID. |
| 6 | `MM_ASN_LOT_DISCREPANCY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MM_ASN_LOT_DISCREPANCY table. |
| 7 | `RECEIVED_LOT_QTY` | DOUBLE |  |  | Numeric value of units physically recevied for the corresponding lot number. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MM_ASN_LINE_DISCREPANCY_ID` | [MM_ASN_LINE_DISCREPANCY](MM_ASN_LINE_DISCREPANCY.md) | `MM_ASN_LINE_DISCREPANCY_ID` |

