# ABO_TESTING

> Contains information for every time an ABO/Rh procedure was resulted on a product.

**Description:** ABO Testing  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABO_GROUP_CD` | DOUBLE | NOT NULL |  | The ABO group that was found present in the blood product through the testing performed on it (ex. "A", "B", "O", or "AB"). |
| 2 | `ABO_TESTING_ID` | DOUBLE | NOT NULL |  | Uniquely identifies information for every time an ABO/Rh procedure was resulted on a product. |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `CURRENT_UPDATED_IND` | DOUBLE |  |  | Defines whether or not the blood product's current ABORh type was updated due to the results of the testing performed. |
| 8 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | This column will be updated if the ABORh testing performed was the testing that confirmed the product's ABORh. If so, the product_event_id will be the key to the product_event table for the "confirmed" event. |
| 9 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The product_id for the blood product tested, from the product table. |
| 10 | `RESULT_ID` | DOUBLE | NOT NULL | FK→ | The result_ID of the results performed on the blood product, from the result table. |
| 11 | `RH_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the Rh type of the blood product tested (ex. "Pos" or "Neg"). If only the ABO group of the blood product was tested, this column will be zero. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |
| `PRODUCT_ID` | [BLOOD_PRODUCT](BLOOD_PRODUCT.md) | `PRODUCT_ID` |
| `RESULT_ID` | [RESULT](RESULT.md) | `RESULT_ID` |

