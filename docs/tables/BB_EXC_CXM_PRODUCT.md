# BB_EXC_CXM_PRODUCT

> Blood Bank Computer Crossmatch Exception Product

**Description:** Contains products crossmatched with exception for parent BB_EXCEPTION row  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABO_CD` | DOUBLE | NOT NULL |  | Code_Value for ABO of product at the time of the computer crossmatch exception. From Code Set 1641. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BB_EXCEPTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the parent BB EXCEPTION row. |
| 7 | `BB_EXC_CXM_PRODUCT_ID` | DOUBLE | NOT NULL |  | This is the primary key to this file. Uniquely identifies a BB_EXC_CXM_PRODUCT row |
| 8 | `CROSSMATCH_EXPIRE_DT_TM` | DATETIME |  |  | Crossmatch expiration of the computer crossmatch at the time of the exception. |
| 9 | `EVENT_DT_TM` | DATETIME |  |  | Date and Time the Computer Crossmatch was performed. |
| 10 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | Code Value for the product type. From Code Set 1604. |
| 11 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for PRODUCT_EVENT row for crossmatch event. |
| 12 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for product. |
| 13 | `RH_CD` | DOUBLE | NOT NULL |  | Code_Value for Rh of product at the time of the computer crossmatch exception. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BB_EXCEPTION_ID` | [BB_EXCEPTION](BB_EXCEPTION.md) | `EXCEPTION_ID` |
| `PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |

