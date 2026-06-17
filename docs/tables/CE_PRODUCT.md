# CE_PRODUCT

> Clinical Events Product Table

**Description:** ce product  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABO_CD` | DOUBLE | NOT NULL |  | Description of the ABO blood type. |
| 2 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the clinical event table. |
| 3 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | Description of a product by code |
| 4 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the product table. Foreign key: XFK2 - (product) |
| 5 | `PRODUCT_NBR` | VARCHAR(40) | NOT NULL |  | Product number |
| 6 | `PRODUCT_QUANTITY` | DOUBLE |  |  | The number of products tested |
| 7 | `PRODUCT_QUANTITY_UNIT_CD` | DOUBLE | NOT NULL |  | CODE SET:54 The unit of the number of products tested, could be 'bag','unit', 'vials', etc. |
| 8 | `PRODUCT_STATUS_CD` | DOUBLE | NOT NULL |  | Status of product |
| 9 | `PRODUCT_STRENGTH` | DOUBLE |  |  | The concentration of the product |
| 10 | `PRODUCT_STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | CODE SET:54 The unit of the concentration of the product |
| 11 | `PRODUCT_VOLUME` | DOUBLE |  |  | The volume of the product tested |
| 12 | `PRODUCT_VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | CODE SET:54 The unit of the volume for the product tested |
| 13 | `RH_CD` | DOUBLE | NOT NULL |  | Description of the Rh value. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when this row is valid. |
| 20 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the "End Point" of when this row is valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |

