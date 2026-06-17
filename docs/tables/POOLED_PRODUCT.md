# POOLED_PRODUCT

> A reference of the new types of products that can be created by pooled, by a site.

**Description:** Pooled Product  
**Table type:** REFERENCE  
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
| 5 | `POOL_NBR` | DOUBLE | NOT NULL |  | The incremental number used to generate a unique product number for the newly pooled product created by the PoolProducts application. This number begins at 1 and increments by 1 every time this type of pooled product is created. |
| 6 | `POOL_OPTION_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the POOL_OPTION table. An internal system-assigned number. On this table, it is used to associate the product number generated with the appropriate pooling option. |
| 7 | `POOL_OPTION_NBR_ID` | DOUBLE | NOT NULL |  | The primary key of this table. An internal system-assigned number that ensures the uniqueness of each row. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `YEAR` | DOUBLE |  |  | The year that should be used to generate the pooled product number. This is provided so that sites will know how many pooled products of a certain type have been created for that year. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `POOL_OPTION_ID` | [POOL_OPTION](POOL_OPTION.md) | `OPTION_ID` |

