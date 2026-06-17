# ORDER_PRODUCT_DOSE

> Stores doses assigned to a particular order product.

**Description:** Order Product Dose  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL | FK→ | A sequence number used to identify the order of the actions. |
| 2 | `DOSE_QUANTITY` | DOUBLE | NOT NULL |  | The number of units to be administered to the patient. The dosage amount given, if given 500 mg of drug X, but there are only 250 mg tabs, then the dose quantity is 2 in order to get the dosage up to the amount of the order. |
| 3 | `DOSE_QUANTITY_UNIT_CD` | DOUBLE | NOT NULL |  | Unit to apply to the dose quantity |
| 4 | `INGRED_SEQUENCE` | DOUBLE | NOT NULL | FK→ | A sequence number used to identify the order of ingredients. |
| 5 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Reference to the formulary item pharmacy product. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order this dose pertains to. |
| 7 | `ORDER_PRODUCT_DOSE_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the ORDER_PRODUCT_DOSE table. |
| 8 | `SCHEDULE_SEQ` | DOUBLE | NOT NULL |  | The sequence of the related frequency schedule which the order ingredient dose instance represents. |
| 9 | `TNF_ID` | DOUBLE | NOT NULL | FK→ | Key to template_non-formulary table |
| 10 | `UNROUNDED_DOSE_QTY` | DOUBLE | NOT NULL |  | Product's quantity per dose prior to rounding. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_SEQUENCE` | [ORDER_PRODUCT](ORDER_PRODUCT.md) | `ACTION_SEQUENCE` |
| `INGRED_SEQUENCE` | [ORDER_PRODUCT](ORDER_PRODUCT.md) | `INGRED_SEQUENCE` |
| `ITEM_ID` | [ORDER_PRODUCT](ORDER_PRODUCT.md) | `ITEM_ID` |
| `ORDER_ID` | [ORDER_PRODUCT](ORDER_PRODUCT.md) | `ORDER_ID` |
| `TNF_ID` | [ORDER_PRODUCT](ORDER_PRODUCT.md) | `TNF_ID` |

