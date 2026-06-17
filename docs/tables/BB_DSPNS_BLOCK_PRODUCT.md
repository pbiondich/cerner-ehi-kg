# BB_DSPNS_BLOCK_PRODUCT

> This reference table defines the allogeneic products that should be blocked from being dispensed, when like-autologous or like-directed poducts exist for the patient

**Description:** Dispense Block Product  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BLOCK_PRODUCT_ID` | DOUBLE | NOT NULL |  | A system-generated number that uniquely identifies every row on this table. |
| 6 | `DISPENSE_BLOCK_ID` | DOUBLE | NOT NULL | FK→ | This value in this column links the row on the bb_dspns_block table to the row on this table. It links the autologous or directed product defined on the bb_dspns_block table to the allogeneic (homologous) product defined on this row. |
| 7 | `PRODUCT_CD` | DOUBLE | NOT NULL | FK→ | This code value represents the allogeneic product that should be blocked from being dispensed to the patient, when the autologous or directed product (product_cd column on bb_dspns_block table) associated with this row (through the bb_dspns_block column on bb_dspns_block table). |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_BLOCK_ID` | [BB_DSPNS_BLOCK](BB_DSPNS_BLOCK.md) | `DISPENSE_BLOCK_ID` |
| `PRODUCT_CD` | [PRODUCT_INDEX](PRODUCT_INDEX.md) | `PRODUCT_CD` |

