# PRODUCT_RH_PHENOTYPE

> This table contains the Rh phenotype tested on the product.

**Description:** Product Rh Phenotype  
**Table type:** ACTIVITY  
**Primary key:** `PRODUCT_RH_PHENOTYPE_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Links this row for this product's Rh phenotype to the actual nomenclature (alpha response) entered, e.g., "CDE/CDE". |
| 6 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | Links this row to the actual product for which this Rh phenotype is being stored. It is the primary key to the Product table. |
| 7 | `PRODUCT_RH_PHENOTYPE_ID` | DOUBLE | NOT NULL | PK | The primary key to this table. An internal system-assigned number that ensures the uniqueness of each row. |
| 8 | `RH_PHENOTYPE_ID` | DOUBLE | NOT NULL | FK→ | Links this row to the reference table on which Rh phenotypes are defined by the user. An example is "CDE/CDE". This column is the primary key to the bb_Rh_phenotype table. |
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
| `RH_PHENOTYPE_ID` | [BB_RH_PHENOTYPE](BB_RH_PHENOTYPE.md) | `RH_PHENOTYPE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SPECIAL_TESTING](SPECIAL_TESTING.md) | `PRODUCT_RH_PHENOTYPE_ID` |

