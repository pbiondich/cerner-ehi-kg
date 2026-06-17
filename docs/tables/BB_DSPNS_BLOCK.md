# BB_DSPNS_BLOCK

> This reference table defines the specific autologous and/or directed products which, when present for the patient, should cause like-allogeneic products to be blocked from dispense.

**Description:** Blood Bank Dispense Block  
**Table type:** REFERENCE  
**Primary key:** `DISPENSE_BLOCK_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALLOW_OVERRIDE_IND` | DOUBLE |  |  | This indicator is set to a value of 1 when the user WILL be allowed to override the warning they receive in Dispense when they try to enter a like-allogeneic product to the autologous or directed product defined on this row. |
| 6 | `DISPENSE_BLOCK_ID` | DOUBLE | NOT NULL | PK | A system-generated number that uniquely identifies every row on this table. |
| 7 | `PRODUCT_CD` | DOUBLE | NOT NULL | FK→ | This code value represents the autologous or directed product that should trigger the blocking of like-allogeneic products being dispensed to the patient. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_CD` | [PRODUCT_INDEX](PRODUCT_INDEX.md) | `PRODUCT_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BB_DSPNS_BLOCK_PRODUCT](BB_DSPNS_BLOCK_PRODUCT.md) | `DISPENSE_BLOCK_ID` |

