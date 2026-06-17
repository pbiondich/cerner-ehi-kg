# PERSON_RH_PHENO_RESULT

> Stores the results of a person's Rh phenotypings, all of them ever done. Related to the person_rh_phenotype table.

**Description:** Person Rh Phenotype Result table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `DONOR_RH_PHENOTYPE_ID` | DOUBLE | NOT NULL |  | Links to a row on the Donor_Rh_Phenotype table which defines the Rh Phenotype (ex. 'CDE/CDE') identified for a donor through serological testing performed on a specimen of blood from the donor. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 7 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature (the alpha response) used to generate this Rh phenotype, ex. "CDE/CDE". |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 9 | `PERSON_RH_PHENOTYPE_ID` | DOUBLE | NOT NULL | FK→ | Links this row to a row on the Person_Rh_Phenotype table. |
| 10 | `PERSON_RH_PHENO_RS_ID` | DOUBLE | NOT NULL |  | The primary key to this table. An internal system-assigned number that ensures the uniqueness of each row. |
| 11 | `RESULT_ID` | DOUBLE | NOT NULL | FK→ | Links this row to a row on the result table, for which it is the primary key. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PERSON_RH_PHENOTYPE_ID` | [PERSON_RH_PHENOTYPE](PERSON_RH_PHENOTYPE.md) | `PERSON_RH_PHENOTYPE_ID` |
| `RESULT_ID` | [RESULT](RESULT.md) | `RESULT_ID` |

