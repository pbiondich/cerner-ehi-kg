# UKR_SACT

> Contain information required for the Systemic Anti Cancer Therapy dataset

**Description:** UK Reporting Systemic Anti Cancer Therapy  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `INTENT_OF_TREATMENT_CD` | DOUBLE | NOT NULL | FK→ | Intent of treatment of the given Regimen within the SACT data-set |
| 6 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Links to the diagnosis associated to the given Programme and Regimen within the SACT data-set |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person record related to the given Programme and Regimen within the SACT data-set |
| 8 | `PROGRAMME_NUM` | DOUBLE | NOT NULL |  | Derived integer value to be used as the Programme Number for the given Programme within the SACT data-set |
| 9 | `REGIMEN_ID` | DOUBLE | NOT NULL | FK→ | Links to the Regimen associated to the given Programme and Regimen within the SACT data-set |
| 10 | `REGIMEN_NUM` | DOUBLE | NOT NULL |  | Derived integer value to be used as the Regimen Number for the given Programme and Regimen within the SACT data-set |
| 11 | `UKR_SACT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INTENT_OF_TREATMENT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REGIMEN_ID` | [REGIMEN](REGIMEN.md) | `REGIMEN_ID` |

