# UCM_KARYOTYPE_CONCEPT

> This table contains the relationships between concept and a karyotype.

**Description:** Unified Case Manager Karyotype Concept  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTOR_CD` | DOUBLE | NOT NULL |  | Identifies the descriptorcode that corresponds to this row. |
| 2 | `DETAILED_FORMAT_IND` | DOUBLE | NOT NULL |  | Indicates if this concept was determined from the karyotype written using the detailed system. |
| 3 | `IMPLIED_IND` | DOUBLE | NOT NULL |  | Indicates that this concept was implied from the karyotype instead of directly specified by the karyotype. |
| 4 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the CBO Concept in the nomenclature table. |
| 5 | `QUESTIONABLE_IND` | DOUBLE | NOT NULL |  | Indicates if this concept was designated as questionable by the karyotype. |
| 6 | `SECTION_NBR` | DOUBLE | NOT NULL |  | Section of the karyotype from where the concept originated . |
| 7 | `UCM_KARYOTYPE_CONCEPT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between concept and a karyotype. |
| 8 | `UCM_KARYOTYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the corresponding karyotype. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `UCM_KARYOTYPE_ID` | [UCM_KARYOTYPE](UCM_KARYOTYPE.md) | `UCM_KARYOTYPE_ID` |

