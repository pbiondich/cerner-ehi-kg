# PERSON_RH_PHENOTYPE

> Defines the Rh Phenotype (ex. 'CDE/CDE') identified for a person through serological testing performed on a specimen of blood from the person.

**Description:** Person Rh Phenotype  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_RH_PHENOTYPE_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Represents the nomenclature of the result entered for this Rh Phenotype (ex. "CDE/CDE"). |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 7 | `PERSON_RH_PHENOTYPE_ID` | DOUBLE | NOT NULL | PK | An internal system-assigned number that ensures the uniqueness of each row on this table. |
| 8 | `RESULT_ID` | DOUBLE | NOT NULL | FK→ | Defines the result entered for this Rh Phenotype (ex. "CDE/CDE"). Links this row to the row on the result table for result correction purposes. |
| 9 | `RH_PHENOTYPE_ID` | DOUBLE | NOT NULL | FK→ | Links this row to the bb_rh_phenotype table where the Rh Phenotype is defined, and where its translation into specific antigens is defined. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RESULT_ID` | [RESULT](RESULT.md) | `RESULT_ID` |
| `RH_PHENOTYPE_ID` | [BB_RH_PHENOTYPE](BB_RH_PHENOTYPE.md) | `RH_PHENOTYPE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PERSON_ANTIGEN](PERSON_ANTIGEN.md) | `PERSON_RH_PHENOTYPE_ID` |
| [PERSON_RH_PHENO_RESULT](PERSON_RH_PHENO_RESULT.md) | `PERSON_RH_PHENOTYPE_ID` |

