# SPECIAL_TESTING_RESULT

> Contains all special testing results performed and verified on a product. This includes antigen typings as well as any other special testing, e.g., CMV negative, etc.

**Description:** Special Testing Result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BB_RESULT_ID` | DOUBLE | NOT NULL |  | An internal system-assigned number (but not a primary key to any table). Since multiple instances of the same procedure can be resulted on the same patient, same accession, and same product, the BB_RESULT_ID is used to make these instances unique. |
| 6 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the PRODUCT table. An internal system-assigned number. On this table, it identifies the product for which the special testing result was verified. |
| 7 | `RESULT_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the RESULT table. An internal system-assigned number. On this table, it provides a link to the actual result that was performed and verified on this product to arrive at this special testing result recorded on this table. |
| 8 | `SPECIAL_TESTING_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the SPECIAL_TESTING table. An internal system-assigned number. On this table, it provides a link back to the row on the special_testing table for this antigen or attribute. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |
| `RESULT_ID` | [RESULT](RESULT.md) | `RESULT_ID` |
| `SPECIAL_TESTING_ID` | [SPECIAL_TESTING](SPECIAL_TESTING.md) | `SPECIAL_TESTING_ID` |

