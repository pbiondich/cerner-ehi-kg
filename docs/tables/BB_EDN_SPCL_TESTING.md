# BB_EDN_SPCL_TESTING

> This table contains the special testing information from an Electronic Delivery Note message structure for a product.

**Description:** Blood Bank Electronic Delivery Note Special Testing  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BB_EDN_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the Electronic Delivery Note product related to this special test. |
| 2 | `BB_EDN_SPCL_TESTING_ID` | DOUBLE | NOT NULL |  | Uniquely identifies special testing information from an Electronic Delivery Note message structure for a product. |
| 3 | `CONFIRMED_IND` | DOUBLE | NOT NULL |  | Indicates if the product's antigen is confirmed. |
| 4 | `ISBT_SPCL_TEST_BARCODE` | VARCHAR(200) |  |  | Contains the ISBT barcode value for special testing. |
| 5 | `ISBT_SPCL_TEST_BARCODE_TYP_TXT` | VARCHAR(2) |  |  | ISBT Data identifier for the data structure populated in ISBT_SPECIAL_TESTING_BARCODE (i.e., if the format of the barcode is data structure 10, Special testing: General, '&(' is data identifier. This tells the application the expected format of the barcode and how to translate the barcode. |
| 6 | `SPCL_TESTING_CD` | DOUBLE | NOT NULL |  | Contains the product's special testing code value. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BB_EDN_PRODUCT_ID` | [BB_EDN_PRODUCT](BB_EDN_PRODUCT.md) | `BB_EDN_PRODUCT_ID` |

