# RX_MED_PROD_DESC

> Stores drug descriptors (such as color, flavor, markings, etc.)

**Description:** Pharmacy Medical Product Description  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FIELD_TYPE_CD` | DOUBLE | NOT NULL |  | Type of descriptor - example color, flavor, markings. |
| 2 | `FIELD_VALUE_STR_TXT` | VARCHAR(255) | NOT NULL |  | The description of a given type. |
| 3 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Stored image of a medication |
| 4 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | Unique, generated key of MED_PRODUCT. |
| 5 | `MED_PROD_DESC_ID` | DOUBLE | NOT NULL |  | Unique, generated key for RX_MED_PROD_DESC. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |
| `MED_PRODUCT_ID` | [MED_PRODUCT](MED_PRODUCT.md) | `MED_PRODUCT_ID` |

