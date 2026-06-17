# BB_RH_PHENO_TESTING

> A reference table that is a child table to the bb_rh_phenotype table. For every Rh Phenotype defined, it identifies the actual antigens represented by the Rh phenotype

**Description:** Blood Bank Rh Phenotype Testing  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `RH_PHENOTYPE_ID` | DOUBLE | NOT NULL | FK→ | This column links the rows on this table to a row on the bb_rh_phenotype table, the parent table. For every row on the bb_rh_phenotype table, there will be many rows on this table for that rh_phenotype_id. |
| 6 | `RH_PHENO_TESTING_ID` | DOUBLE | NOT NULL |  | An internal system-assigned number that ensures the uniqueness of each row on this table. |
| 7 | `SEQUENCE` | DOUBLE | NOT NULL |  | An internal number used to sequence the antigens properly in the Special Testing Tool. |
| 8 | `SPECIAL_TESTING_CD` | DOUBLE | NOT NULL |  | This code value represents the antigen into which the Rh phenotype translates, e.g., "C+", or "e-". |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RH_PHENOTYPE_ID` | [BB_RH_PHENOTYPE](BB_RH_PHENOTYPE.md) | `RH_PHENOTYPE_ID` |

